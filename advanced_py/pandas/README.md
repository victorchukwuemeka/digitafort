# Pandas — Data Analysis in Python

Pandas is the go-to library for working with tabular data in Python. If you've used Excel or SQL, you already know the kind of problems Pandas solves — except Pandas handles millions of rows fast.

```bash
pip install pandas
```

The convention is always `import pandas as pd`. Don't fight it.

---

## 1. Creating a DataFrame

A DataFrame is a table with rows and columns. The most common way to create one is from a dictionary:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "City": ["NYC", "LA", "Chicago", "NYC"],
    "Salary": [70000, 80000, 120000, 90000]
})
```

Each key becomes a column. All lists must be the same length or you'll get a `ValueError`.

---

## 2. Exploring Your Data

The first thing you do with any new dataset:

```python
print(df.shape)              # (4, 4) — rows x columns
print(df.head())             # first 5 rows
print(df.info())             # column types, non-null counts ← run this first
print(df.describe())         # stats for numeric columns (mean, std, min, max)
print(df.isnull().sum())     # missing values per column
print(df["City"].value_counts())  # how many times each city appears
```

`info()` tells you everything: how much data you have, which columns have missing values, and whether the data types make sense. Run it before doing anything else.

---

## 3. Selecting Data

Pandas has two selection methods — and you need to know the difference:

```python
# Columns
df["Name"]              # single column → Series
df[["Name", "Age"]]     # multiple columns → DataFrame

# .loc[] — by label (inclusive on both ends!)
df.loc[0, "Name"]                  # "Alice"
df.loc[0:2, ["Name", "Age"]]      # rows 0, 1, 2 (inclusive!)

# .iloc[] — by position (exclusive at the end, like normal Python)
df.iloc[0]                 # first row
df.iloc[0:2, 0:2]         # first 2 rows, first 2 columns
```

**Remember:** `loc` = labels (inclusive), `iloc` = positions (exclusive). Mixing them up is the #1 source of bugs.

---

## 4. Filtering Rows

Filter rows by giving Pandas a boolean condition:

```python
# Single condition
df[df["Age"] > 30]

# Multiple conditions — wrap each in parentheses, use & or |
df[(df["Age"] > 25) & (df["City"] == "NYC")]
df[(df["City"] == "NYC") | (df["City"] == "LA")]

# .isin() — check against a list
df[df["City"].isin(["NYC", "Chicago"])]

# .query() — cleaner for complex conditions
df.query("Age > 25 and City == 'NYC'")
```

The parentheses around conditions are mandatory — Python's operator precedence will break your code without them.

---

## 5. Missing Data

Real data has gaps. Pandas uses `NaN` for missing values.

```python
# How much is missing per column
df.isnull().sum()

# Drop rows with any missing value
df.dropna()

# Drop only in specific columns
df.dropna(subset=["Age"])

# Fill with a value
df.fillna(0)

# Fill different columns differently
df.fillna({"Age": df["Age"].mean(), "Salary": 0})

# Forward fill (use previous row's value — common for time series)
df["Salary"].ffill()
```

**Don't blindly `dropna()`** — if 30% of rows have any NaN somewhere, you lose 30% of your data. Always check how much you're losing first.

---

## 6. Adding and Modifying Columns

```python
# Add a new column
df["Tax"] = df["Salary"] * 0.1

# Conditional column
import numpy as np
df["Senior"] = np.where(df["Age"] > 30, "Yes", "No")

# Row-by-row logic with .apply() (slower, use for complex logic)
df["Bracket"] = df["Salary"].apply(lambda x: "High" if x > 100000 else "Low")

# Rename columns
df = df.rename(columns={"Name": "Full_Name"})

# Drop columns
df = df.drop("Tax", axis=1)
```

Prefer vectorized operations (`df["col"] * 2`) over `.apply()` — they're 10-100x faster. Use `np.where()` for simple if/else.

---

## 7. Sorting

```python
df.sort_values("Age")                            # ascending
df.sort_values("Salary", ascending=False)         # descending
df.sort_values(["City", "Salary"], ascending=[True, False])  # multi-column

df.nlargest(3, "Salary")    # top 3 earners — cleaner than sort + head
df.nsmallest(2, "Age")      # 2 youngest
```

Note: `sort_values` returns a new DataFrame. Assign it back: `df = df.sort_values(...)`.

---

## 8. Grouping and Aggregation

The most powerful Pandas pattern. Split data into groups, compute something per group, get results:

```python
# Average salary by city
df.groupby("City")["Salary"].mean()

# Multiple stats at once
df.groupby("City").agg(
    avg_age=("Age", "mean"),
    total_salary=("Salary", "sum"),
    headcount=("Name", "count")
)

# Group by multiple columns
df.groupby(["City", "Department"])["Salary"].mean()
```

After a multi-column groupby, use `.reset_index()` to get a regular DataFrame back.

---

## 9. Merging DataFrames

Combine tables like SQL joins:

```python
employees = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"], "Dept_ID": [101, 102, 101]})
departments = pd.DataFrame({"Dept_ID": [101, 102, 104], "Dept_Name": ["Eng", "Mkt", "Sales"]})

pd.merge(employees, departments, on="Dept_ID")                    # inner join (default)
pd.merge(employees, departments, on="Dept_ID", how="left")        # keep all from left
pd.merge(employees, departments, on="Dept_ID", how="outer")       # keep everything
```

**Inner** = only matches. **Left** = all from left + matches. **Outer** = everything, NaN where no match.

---

## 10. Dates

```python
# Convert strings to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract parts
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Set as index and slice by date range
df.set_index("Date", inplace=True)
df["2024-02"]          # all rows from February 2024
```

Always convert date strings to datetime objects — string sorting ("2024-02-01" vs "2024-01-15") doesn't work chronologically.

---

## 11. String Operations

Use the `.str` accessor to work with text columns:

```python
df["Name"].str.lower()
df["Name"].str.strip()
df["Name"].str.contains("li")         # True/False
df["Name"].str.split(" ").str[0]      # first name
df["Name"].str.len()
```

---

## 12. Saving and Loading Data

```python
# Read
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", usecols=["Name", "Age"])   # only specific columns
df = pd.read_excel("data.xlsx")                          # needs openpyxl

# Write
df.to_csv("output.csv", index=False)     # index=False skips row numbers
df.to_excel("output.xlsx", index=False)
```

CSV is universal and human-readable. For large datasets, Parquet (`pd.read_parquet` / `to_parquet`) is much faster and smaller.

---

## Common Gotchas

1. **Parentheses in filtering:** `df[(df["Age"] > 30) & (df["City"] == "NYC")]` — missing parentheses = error
2. **`loc` is inclusive:** `df.loc[0:2]` includes row 2. `iloc[0:2]` does not.
3. **Numbers stored as strings:** If `df["age"].dtype` is `object`, fix with `pd.to_numeric(df["age"], errors="coerce")`
4. **Forgetting `.copy()`:** `subset = df[df["Age"] > 30]` then `subset["X"] = 1` may not work. Use `.copy()` explicitly.
5. **`sort_values` doesn't modify in place:** You must assign: `df = df.sort_values("Age")`

---

## What's Next?

- **Visualization**: `matplotlib`, `seaborn`
- **Machine learning**: `scikit-learn`
- **Big data**: `Polars`, `Dask`

*Run `python pandas_examples.py` for runnable examples of everything above.*
*Try `python exercises.py` to practice.*
