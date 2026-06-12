# Pandas — Data Analysis in Python

## 1. What is Pandas?
Pandas is a library for working with tabular data (like spreadsheets or SQL tables). It gives you two structures: **Series** (a single column) and **DataFrame** (a table with rows and columns). Let's create our first DataFrame:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "City": ["NYC", "LA", "Chicago", "NYC"],
    "Salary": [70000, 80000, 120000, 90000]
}
df = pd.DataFrame(data)
```

## 2. Exploring Your Data
Before analyzing, understand what you're working with:

```python
print(df.head())       # first 5 rows
print(df.info())       # column types and non-null counts
print(df.describe())   # summary stats for numeric columns
print(df.shape)        # (4, 4)
print(df.columns)      # Index(['Name', 'Age', 'City', 'Salary'])
print(df.dtypes)       # data type per column
```

`info()` is always the first thing to call — it shows if any columns have missing data or wrong types.

## 3. Selecting Data
Pandas has two selection methods: `.loc[]` for labels and `.iloc[]` for positions:

```python
# Columns
print(df["Name"])              # single column as Series
print(df[["Name", "Age"]])     # multiple columns as DataFrame

# Rows by position
print(df.iloc[0])              # first row
print(df.iloc[0:3])            # first 3 rows

# Rows by index label
print(df.loc[0])               # row where index = 0
print(df.loc[0:2, ["Name", "Age"]])  # rows 0-2, Name and Age only

# Single value
print(df.at[0, "Name"])        # Alice — fast single-value access
```

## 4. Filtering
Filter rows using conditions. Each condition must be in parentheses:

```python
# Single condition
print(df[df["Age"] > 30])
#      Name  Age      City  Salary
# 2  Charlie   35  Chicago  120000

# Multiple conditions with & (and), | (or)
print(df[(df["Age"] > 25) & (df["City"] == "NYC")])

# Filter by list
print(df[df["Name"].isin(["Alice", "Diana"])])

# SQL-like query — cleaner for complex conditions
print(df.query("Age > 25 and City == 'NYC'"))
```

The `query` method is often easier to read when you have multiple conditions.

## 5. Handling Missing Data
Real data has missing values — Pandas represents them as `NaN`:

```python
# First, detect missing values
print(df.isnull().sum())

# Add a row with missing data to demonstrate
df2 = df.copy()
df2.loc[4] = ["Eve", None, "LA", None]  # Age and Salary are missing

# Drop missing values
print(df2.dropna())           # drops rows with any NaN
print(df2.dropna(subset=["Age"]))  # drops only if Age is NaN

# Fill missing values
print(df2.fillna(0))                    # replace NaN with 0
print(df2.fillna({"Age": df2["Age"].mean(), "Salary": 0}))
```

## 6. Adding and Modifying Columns
```python
# Add derived column
df["Tax"] = df["Salary"] * 0.1

# Create column with logic
df["Age_Group"] = df["Age"].apply(lambda x: "Young" if x < 30 else "Senior")

# Rename
df.rename(columns={"Name": "Full_Name"}, inplace=True)

# Drop
df.drop("Tax", axis=1, inplace=True)
```

## 7. Grouping and Aggregation
`groupby` splits data into groups, applies a function, and combines results (split-apply-combine):

```python
# Average salary by city
print(df.groupby("City")["Salary"].mean())

# Multiple aggregations
print(df.groupby("City").agg({
    "Age": ["mean", "max", "min"],
    "Salary": ["sum", "mean"]
}))

# Named aggregations (cleaner output)
print(df.groupby("City").agg(
    avg_salary=("Salary", "mean"),
    count=("Name", "count")
))
```

This is the most powerful Pandas pattern — it's the equivalent of SQL's `GROUP BY`.

## 8. Sorting
```python
print(df.sort_values("Age"))                     # ascending
print(df.sort_values("Age", ascending=False))    # descending
print(df.sort_values(["City", "Age"]))           # multi-column
```

## 9. Merging DataFrames
Combine DataFrames like SQL joins:

```python
df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})
df2 = pd.DataFrame({"ID": [1, 2, 4], "Score": [85, 92, 78]})

# Inner join — only matching IDs
print(pd.merge(df1, df2, on="ID"))
#    ID     Name  Score
# 0   1    Alice     85
# 1   2      Bob     92

# Left join — all from df1
print(pd.merge(df1, df2, on="ID", how="left"))

# Stack rows
print(pd.concat([df1, df2], axis=0))
```

## 10. Working with Dates
```python
df["Date"] = pd.to_datetime(["2024-01-01", "2024-02-15", "2024-03-20", "2024-04-10"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df.set_index("Date", inplace=True)
```

## 11. Loading Real Data
```python
df = pd.read_csv("example.csv")
print(df.head())
```

Most real-world work starts with `read_csv`. The typical workflow is: **load → explore → clean → transform → analyze → visualize**.
