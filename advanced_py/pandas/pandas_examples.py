# =============================================================================
# Pandas Course — Runnable Examples
# =============================================================================
# To run this example:
#   1. Install the required packages: pip install -r requirements.txt
#   2. Run the script: python pandas_examples.py
#
# This script covers all the topics from the README.md with practical,
# runnable examples. Each section prints its output so you can follow along.
# =============================================================================

import pandas as pd
import numpy as np

# Helper to print section headers
def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

# =============================================================================
# 1. CREATING DATAFRAMES
# =============================================================================
section("1. Creating DataFrames")

# From a dictionary (most common)
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 30, 35, 28, 32],
    "City": ["NYC", "LA", "Chicago", "NYC", "LA"],
    "Salary": [70000, 80000, 120000, 90000, 95000],
    "Department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"]
})

print("DataFrame created from dictionary:")
print(df)

# From a list of dictionaries
records = [
    {"Name": "Frank", "Age": 40, "City": "Chicago"},
    {"Name": "Grace", "Age": 27, "City": "NYC"},
]
df_records = pd.DataFrame(records)
print("\nDataFrame from list of dictionaries:")
print(df_records)


# =============================================================================
# 2. EXPLORING YOUR DATA
# =============================================================================
section("2. Exploring Your Data")

print("--- df.head(3) ---")
print(df.head(3))

print("\n--- df.info() ---")
df.info()

print("\n--- df.describe() ---")
print(df.describe())

print("\n--- df.shape ---")
print(df.shape)

print("\n--- df.columns ---")
print(df.columns.tolist())

print("\n--- df.dtypes ---")
print(df.dtypes)

print("\n--- df.isnull().sum() ---")
print(df.isnull().sum())

print("\n--- df['City'].value_counts() ---")
print(df["City"].value_counts())


# =============================================================================
# 3. SELECTING DATA
# =============================================================================
section("3. Selecting Data")

# Single column (returns Series)
print("--- df['Name'] (Series) ---")
print(df["Name"])

print("\n--- Type of df['Name'] ---")
print(type(df["Name"]))

# Multiple columns (returns DataFrame)
print("\n--- df[['Name', 'Age']] (DataFrame) ---")
print(df[["Name", "Age"]])

# .loc — by label
print("\n--- df.loc[0] ---")
print(df.loc[0])

print("\n--- df.loc[0:2, ['Name', 'Age']] ---")
print(df.loc[0:2, ["Name", "Age"]])

# .iloc — by position
print("\n--- df.iloc[0] ---")
print(df.iloc[0])

print("\n--- df.iloc[0:3, 0:2] ---")
print(df.iloc[0:3, 0:2])

# .at — single value by label
print("\n--- df.at[2, 'Name'] ---")
print(df.at[2, "Name"])

# .iat — single value by position
print("\n--- df.iat[2, 0] ---")
print(df.iat[2, 0])


# =============================================================================
# 4. FILTERING ROWS
# =============================================================================
section("4. Filtering Rows")

# Single condition
print("--- df[df['Age'] > 30] ---")
print(df[df["Age"] > 30])

# Multiple conditions with & (AND)
print("\n--- df[(df['Age'] > 25) & (df['City'] == 'NYC')] ---")
print(df[(df["Age"] > 25) & (df["City"] == "NYC")])

# Multiple conditions with | (OR)
print("\n--- df[(df['City'] == 'NYC') | (df['City'] == 'LA')] ---")
print(df[(df["City"] == "NYC") | (df["City"] == "LA")])

# Using .isin()
print("\n--- df[df['City'].isin(['NYC', 'Chicago'])] ---")
print(df[df["City"].isin(["NYC", "Chicago"])])

# Using .query()
print("\n--- df.query(\"Age > 25 and City == 'NYC'\") ---")
print(df.query("Age > 25 and City == 'NYC'"))


# =============================================================================
# 5. HANDLING MISSING DATA
# =============================================================================
section("5. Handling Missing Data")

# Create DataFrame with missing values
df_missing = df.copy()
df_missing.loc[5] = ["Frank", None, "LA", None, "Engineering"]
df_missing.loc[6] = ["Grace", 27, None, 65000, None]

print("--- DataFrame with missing values ---")
print(df_missing)

print("\n--- df_missing.isnull().sum() ---")
print(df_missing.isnull().sum())

# Drop rows with any NaN
print("\n--- df_missing.dropna() ---")
print(df_missing.dropna())

# Drop only in specific columns
print("\n--- df_missing.dropna(subset=['Age']) ---")
print(df_missing.dropna(subset=["Age"]))

# Fill all NaN with 0
print("\n--- df_missing.fillna(0) ---")
print(df_missing.fillna(0))

# Fill with column-specific values
print("\n--- df_missing.fillna({'Age': df_missing['Age'].mean(), 'City': 'Unknown'}) ---")
print(df_missing.fillna({"Age": df_missing["Age"].mean(), "City": "Unknown"}))


# =============================================================================
# 6. ADDING, MODIFYING, AND REMOVING COLUMNS
# =============================================================================
section("6. Adding, Modifying, and Removing Columns")

df2 = df.copy()

# Add new column
df2["Tax"] = df2["Salary"] * 0.1
print("--- After adding 'Tax' column ---")
print(df2)

# Add column with logic using np.where (fast)
df2["Senior"] = np.where(df2["Age"] > 30, "Yes", "No")
print("\n--- After adding 'Senior' column ---")
print(df2)

# Add column with .apply() (for complex logic)
df2["Age_Group"] = df2["Age"].apply(lambda x: "Young" if x < 28 else "Mid" if x < 33 else "Senior")
print("\n--- After adding 'Age_Group' column ---")
print(df2)

# Rename columns
df2 = df2.rename(columns={"Name": "Full_Name", "Age": "Years"})
print("\n--- After renaming columns ---")
print(df2.columns.tolist())

# Drop columns
df2 = df2.drop(["Tax", "Senior"], axis=1)
print("\n--- After dropping 'Tax' and 'Senior' ---")
print(df2)


# =============================================================================
# 7. SORTING
# =============================================================================
section("7. Sorting")

# Ascending
print("--- df.sort_values('Age') ---")
print(df.sort_values("Age"))

# Descending
print("\n--- df.sort_values('Salary', ascending=False) ---")
print(df.sort_values("Salary", ascending=False))

# Multi-column sort
print("\n--- df.sort_values(['City', 'Salary'], ascending=[True, False]) ---")
print(df.sort_values(["City", "Salary"], ascending=[True, False]))

# Top 3 earners
print("\n--- df.nlargest(3, 'Salary') ---")
print(df.nlargest(3, "Salary"))


# =============================================================================
# 8. GROUPING AND AGGREGATION
# =============================================================================
section("8. Grouping and Aggregation")

# Basic groupby
print("--- Average salary by city ---")
print(df.groupby("City")["Salary"].mean())

# Multiple aggregations with .agg()
print("\n--- Multiple aggregations ---")
print(df.groupby("City").agg(
    avg_age=("Age", "mean"),
    max_salary=("Salary", "max"),
    headcount=("Name", "count")
))

# Groupby with multiple columns
print("\n--- Groupby City and Department ---")
print(df.groupby(["City", "Department"]).agg(
    avg_salary=("Salary", "mean"),
    count=("Name", "count")
).reset_index())


# =============================================================================
# 9. MERGING DATAFRAMES
# =============================================================================
section("9. Merging DataFrames")

employees = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Dept_ID": [101, 102, 101, 103]
})

departments = pd.DataFrame({
    "Dept_ID": [101, 102, 104],
    "Dept_Name": ["Engineering", "Marketing", "Sales"]
})

print("--- Employees ---")
print(employees)
print("\n--- Departments ---")
print(departments)

# Inner join
print("\n--- Inner join ---")
print(pd.merge(employees, departments, on="Dept_ID"))

# Left join
print("\n--- Left join ---")
print(pd.merge(employees, departments, on="Dept_ID", how="left"))

# Outer join
print("\n--- Outer join ---")
print(pd.merge(employees, departments, on="Dept_ID", how="outer"))


# =============================================================================
# 10. WORKING WITH DATES
# =============================================================================
section("10. Working with Dates")

df_dates = pd.DataFrame({
    "Date": pd.date_range("2024-01-01", periods=5, freq="ME"),
    "Sales": [1500, 1800, 2200, 1900, 2500]
})

print("--- DataFrame with dates ---")
print(df_dates)

# Extract date parts
df_dates["Year"] = df_dates["Date"].dt.year
df_dates["Month"] = df_dates["Date"].dt.month
df_dates["Day_Name"] = df_dates["Date"].dt.day_name()

print("\n--- Date parts ---")
print(df_dates)

# Set date as index and slice by date
df_dates.set_index("Date", inplace=True)
print("\n--- All rows from March onward ---")
print(df_dates[df_dates.index >= "2024-03-01"])

# Resample to quarterly
print("\n--- Quarterly average (resample) ---")
print(df_dates.resample("QE")["Sales"].mean())


# =============================================================================
# 11. STRING OPERATIONS
# =============================================================================
section("11. String Operations")

df_str = pd.DataFrame({
    "Name": ["  Alice Smith ", "BOB JONES", "charlie brown", "Diana Prince"],
    "Email": ["alice@gmail.com", "bob@yahoo.com", "charlie@hotmail.COM", "diana@gmail.com"]
})

print("--- Original ---")
print(df_str)

# String methods
df_str["Name_Clean"] = df_str["Name"].str.strip().str.title()
df_str["Domain"] = df_str["Email"].str.split("@").str[1].str.lower()
df_str["Name_Length"] = df_str["Name_Clean"].str.len()

print("\n--- After string operations ---")
print(df_str)

# Filtering by string pattern
print("\n--- Names containing 'a' (case-insensitive) ---")
print(df_str[df_str["Name_Clean"].str.lower().str.contains("a")])


# =============================================================================
# 12. PIVOT TABLES
# =============================================================================
section("12. Pivot Tables")

sales = pd.DataFrame({
    "Date": ["2024-01", "2024-01", "2024-02", "2024-02", "2024-03", "2024-03"],
    "Product": ["A", "B", "A", "B", "A", "B"],
    "Revenue": [100, 150, 200, 120, 180, 160]
})

print("--- Sales data ---")
print(sales)

pivot = sales.pivot_table(values="Revenue", index="Date", columns="Product", aggfunc="sum")
print("\n--- Pivot table ---")
print(pivot)

# Crosstab
print("\n--- Crosstab ---")
print(pd.crosstab(sales["Product"], sales["Date"], margins=True))


# =============================================================================
# 13. WINDOW FUNCTIONS
# =============================================================================
section("13. Window Functions (Rolling & Expanding)")

stock = pd.DataFrame({
    "Date": pd.date_range("2024-01-01", periods=10),
    "Price": [100, 102, 101, 105, 103, 107, 110, 108, 112, 115]
})

# Rolling (3-day moving average)
stock["MA_3"] = stock["Price"].rolling(window=3).mean()
stock["MA_3_NoNaN"] = stock["Price"].rolling(window=3, min_periods=1).mean()

# Expanding (cumulative max)
stock["Cum_Max"] = stock["Price"].expanding().max()

# Percent change
stock["Pct_Change"] = stock["Price"].pct_change()

print("--- Stock with window functions ---")
print(stock)


# =============================================================================
# 14. METHOD CHAINING
# =============================================================================
section("14. Method Chaining")

result = (pd.read_csv("example.csv")
    if pd.read_csv("example.csv").shape[0] > 0
    else df.copy()
)

# Chaining example with the employee DataFrame
result = (df.copy()
    .query("Age > 25")
    .assign(Salary_K=lambda x: x["Salary"] / 1000)
    .rename(columns={"Name": "Employee"})
    .sort_values("Salary", ascending=False)
)

print("--- Chained pipeline result ---")
print(result)


# =============================================================================
# 15. SAVING AND LOADING DATA
# =============================================================================
section("15. Saving and Loading Data")

# Save to CSV
df.to_csv("output_example.csv", index=False)
print("Saved to output_example.csv")

# Read it back
df_loaded = pd.read_csv("output_example.csv")
print("\n--- Loaded back from CSV ---")
print(df_loaded)

# Save to Excel (requires openpyxl)
try:
    df.to_excel("output_example.xlsx", index=False, sheet_name="Employees")
    print("\nSaved to output_example.xlsx")
except ImportError:
    print("\nSkipping Excel save (openpyxl not installed)")

# Save to JSON
df.to_json("output_example.json", orient="records", indent=2)
print("Saved to output_example.json")


# =============================================================================
# 16. COMMON GOTCHAS DEMO
# =============================================================================
section("16. Common Gotchas")

# Gotcha 1: Chained indexing warning
print("--- Gotcha 1: SettingWithCopyWarning ---")
subset = df[df["Age"] > 30].copy()  # .copy() avoids the warning
subset["Test"] = "ok"
print(subset)

# Gotcha 2: String vs numeric
print("\n--- Gotcha 2: String vs Numeric ---")
df_mixed = pd.DataFrame({"Value": ["1", "2", "3", "not_a_number"]})
df_mixed["Value_Clean"] = pd.to_numeric(df_mixed["Value"], errors="coerce")
print(df_mixed)

# Gotcha 3: reset_index after groupby
print("\n--- Gotcha 3: reset_index after groupby ---")
grouped = df.groupby("City")["Salary"].mean()
print("Without reset_index:")
print(grouped)
print("\nWith reset_index:")
print(grouped.reset_index())


# =============================================================================
# Clean up
# =============================================================================
import os
for f in ["output_example.csv", "output_example.json"]:
    if os.path.exists(f):
        os.remove(f)
if os.path.exists("output_example.xlsx"):
    os.remove("output_example.xlsx")

print(f"\n{'='*60}")
print("  All examples completed! Check the README.md for the full course.")
print(f"{'='*60}")
