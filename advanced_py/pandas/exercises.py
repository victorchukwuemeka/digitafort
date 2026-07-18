# =============================================================================
# Pandas Exercises — Practice What You've Learned
# =============================================================================
# Run this file to check your answers.
# Try to solve each exercise BEFORE looking at the solution.
#
# Usage:
#   python exercises.py
# =============================================================================

import pandas as pd
import numpy as np

# =============================================================================
# Setup: Load the sample data
# =============================================================================
print("="*60)
print("  PANDAS EXERCISES")
print("="*60)

df = pd.read_csv("example.csv")
print("\nUsing this DataFrame:")
print(df.head(10))
print(f"\nTotal rows: {len(df)}, Columns: {df.columns.tolist()}\n")


# =============================================================================
# EXERCISE 1: Exploration (5 min)
# =============================================================================
print("\n--- EXERCISE 1: Exploration ---")
print("Task: Use df.info() and df.describe() to answer:")
print("  1. How many employees are there?")
print("  2. What is the average salary?")
print("  3. What are the unique cities?\n")

# YOUR CODE HERE:
# print(df.info())
# print(df.describe())
# print(df["City"].unique())

# SOLUTION:
print("SOLUTION:")
print(f"  1. Total employees: {len(df)}")
print(f"  2. Average salary: ${df['Salary'].mean():,.0f}")
print(f"  3. Unique cities: {df['City'].unique().tolist()}")


# =============================================================================
# EXERCISE 2: Filtering (5 min)
# =============================================================================
print("\n--- EXERCISE 2: Filtering ---")
print("Tasks:")
print("  a) Filter employees older than 30")
print("  b) Filter Engineering employees earning more than $90,000")
print("  c) Filter employees in NYC OR earning more than $100,000\n")

# YOUR CODE HERE:
# older_than_30 = df[df["Age"] > 30]
# high_earning_engineers = df[(df["Department"] == "Engineering") & (df["Salary"] > 90000)]
# nyc_or_high_salary = df[(df["City"] == "New York") | (df["Salary"] > 100000)]

# SOLUTION:
print("SOLUTION:")
print("a) Employees older than 30:")
print(df[df["Age"] > 30])
print("\nb) Engineering employees earning > $90k:")
print(df[(df["Department"] == "Engineering") & (df["Salary"] > 90000)])
print("\nc) NYC OR salary > $100k:")
print(df[(df["City"] == "New York") | (df["Salary"] > 100000)])


# =============================================================================
# EXERCISE 3: Adding Columns (5 min)
# =============================================================================
print("\n--- EXERCISE 3: Adding Columns ---")
print("Tasks:")
print("  a) Add a 'Salary_K' column (salary in thousands)")
print("  b) Add a 'Senior' column (Yes if Age > 30, else No)")
print("  c) Add a 'Years_Experience' column (2024 - start year)\n")

# YOUR CODE HERE:
# df["Salary_K"] = df["Salary"] / 1000
# df["Senior"] = np.where(df["Age"] > 30, "Yes", "No")
# df["Start_Date"] = pd.to_datetime(df["Start_Date"])
# df["Years_Experience"] = 2024 - df["Start_Date"].dt.year

# SOLUTION:
print("SOLUTION:")
df_sol = df.copy()
df_sol["Salary_K"] = df_sol["Salary"] / 1000
df_sol["Senior"] = np.where(df_sol["Age"] > 30, "Yes", "No")
df_sol["Start_Date"] = pd.to_datetime(df_sol["Start_Date"])
df_sol["Years_Experience"] = 2024 - df_sol["Start_Date"].dt.year
print(df_sol[["Name", "Salary_K", "Senior", "Years_Experience"]])


# =============================================================================
# EXERCISE 4: Grouping (10 min)
# =============================================================================
print("\n--- EXERCISE 4: Grouping ---")
print("Tasks:")
print("  a) Average salary by department")
print("  b) Count of employees by city")
print("  c) For each department, find the highest and lowest salary")
print("  d) Which city has the most Engineering employees?\n")

# YOUR CODE HERE:
# print(df.groupby("Department")["Salary"].mean())
# print(df["City"].value_counts())
# print(df.groupby("Department")["Salary"].agg(["min", "max"]))
# df[df["Department"] == "Engineering"].groupby("City").size().idxmax()

# SOLUTION:
print("SOLUTION:")
print("a) Average salary by department:")
print(df.groupby("Department")["Salary"].mean())
print("\nb) Count by city:")
print(df["City"].value_counts())
print("\nc) Min and max salary by department:")
print(df.groupby("Department")["Salary"].agg(["min", "max"]))
print("\nd) City with most Engineering employees:")
eng_by_city = df[df["Department"] == "Engineering"].groupby("City").size()
print(f"  {eng_by_city.idxmax()} ({eng_by_city.max()} engineers)")


# =============================================================================
# EXERCISE 5: Missing Data (10 min)
# =============================================================================
print("\n--- EXERCISE 5: Missing Data ---")
print("Tasks:")
print("  1. Create a copy of df and set 3 salaries to NaN")
print("  2. Fill the NaN values with the department average salary")
print("  3. Verify no NaN values remain\n")

# YOUR CODE HERE:
# df_missing = df.copy()
# df_missing.loc[[0, 5, 10], "Salary"] = np.nan
# df_missing["Salary"] = df_missing.groupby("Department")["Salary"].transform(
#     lambda x: x.fillna(x.mean())
# )
# print(df_missing.isnull().sum())

# SOLUTION:
print("SOLUTION:")
df_missing = df.copy()
df_missing.loc[[0, 5, 10], "Salary"] = np.nan
print("Before filling:")
print(df_missing[["Name", "Department", "Salary"]].head(12))

df_missing["Salary"] = df_missing.groupby("Department")["Salary"].transform(
    lambda x: x.fillna(x.mean())
)
print("\nAfter filling with department averages:")
print(df_missing[["Name", "Department", "Salary"]].head(12))
print(f"\nRemaining NaN: {df_missing.isnull().sum().sum()}")


# =============================================================================
# EXERCISE 6: Merging (10 min)
# =============================================================================
print("\n--- EXERCISE 6: Merging ---")
print("Tasks:")
print("  1. Create a departments DataFrame with department budgets")
print("  2. Merge it with the employee DataFrame")
print("  3. Find which departments are over budget")
print("     (total salaries > budget)\n")

# YOUR CODE HERE:
# budgets = pd.DataFrame({
#     "Department": ["Engineering", "Marketing", "HR"],
#     "Budget": [350000, 250000, 200000]
# })
# merged = pd.merge(df, budgets, on="Department")
# dept_totals = merged.groupby("Department").agg(
#     total_salary=("Salary", "sum"),
#     budget=("Budget", "first")
# )
# over_budget = dept_totals[dept_totals["total_salary"] > dept_totals["budget"]]
# print(over_budget)

# SOLUTION:
print("SOLUTION:")
budgets = pd.DataFrame({
    "Department": ["Engineering", "Marketing", "HR"],
    "Budget": [350000, 250000, 200000]
})
merged = pd.merge(df, budgets, on="Department")
dept_totals = merged.groupby("Department").agg(
    total_salary=("Salary", "sum"),
    budget=("Budget", "first")
).reset_index()
dept_totals["over_budget"] = dept_totals["total_salary"] > dept_totals["budget"]

print(dept_totals)
print(f"\nDepartments over budget: {dept_totals[dept_totals['over_budget']]['Department'].tolist()}")


# =============================================================================
# EXERCISE 7: String Operations (5 min)
# =============================================================================
print("\n--- EXERCISE 7: String Operations ---")
print("Tasks:")
print("  a) Create a column with all-lowercase names")
print("  b) Create a column with just the first name")
print("  c) Find employees whose last name starts with 'S'\n")

# YOUR CODE HERE:
# df["Name_Lower"] = df["Name"].str.lower()
# df["First_Name"] = df["Name"].str.split(" ").str[0]
# df["Last_Name"] = df["Name"].str.split(" ").str[-1]
# print(df[df["Last_Name"].str.startswith("S")])

# SOLUTION:
print("SOLUTION:")
df_str = df.copy()
df_str["Name_Lower"] = df_str["Name"].str.lower()
df_str["First_Name"] = df_str["Name"].str.split(" ").str[0]
df_str["Last_Name"] = df_str["Name"].str.split(" ").str[-1]
print(df_str[["Name", "First_Name", "Last_Name"]])
print("\nEmployees with last name starting with 'S':")
print(df_str[df_str["Last_Name"].str.startswith("S")][["Name", "Last_Name"]])


# =============================================================================
# EXERCISE 8: Sorting and Ranking (5 min)
# =============================================================================
print("\n--- EXERCISE 8: Sorting ---")
print("Tasks:")
print("  a) Find the 3 youngest employees")
print("  b) Sort employees by department (A-Z), then by salary (high to low)")
print("  c) Add a 'Salary_Rank' column ranking employees by salary within each department\n")

# YOUR CODE HERE:
# print(df.nsmallest(3, "Age"))
# print(df.sort_values(["Department", "Salary"], ascending=[True, False]))
# df["Salary_Rank"] = df.groupby("Department")["Salary"].rank(ascending=False)

# SOLUTION:
print("SOLUTION:")
print("a) 3 youngest employees:")
print(df.nsmallest(3, "Age"))
print("\nb) Sorted by department, then salary desc:")
print(df.sort_values(["Department", "Salary"], ascending=[True, False]))
print("\nc) Salary rank within department:")
df_ranked = df.copy()
df_ranked["Salary_Rank"] = df_ranked.groupby("Department")["Salary"].rank(ascending=False)
print(df_ranked[["Name", "Department", "Salary", "Salary_Rank"]])


# =============================================================================
# EXERCISE 9: Window Functions (10 min)
# =============================================================================
print("\n--- EXERCISE 9: Window Functions ---")
print("Tasks:")
print("  1. Create a DataFrame with 12 months of sales data")
print("  2. Calculate a 3-month moving average")
print("  3. Calculate cumulative revenue")
print("  4. Calculate month-over-month percentage change\n")

# YOUR CODE HERE:
# sales = pd.DataFrame({
#     "Month": pd.date_range("2024-01-01", periods=12, freq="MS"),
#     "Revenue": [15000, 18000, 16500, 22000, 25000, 23000,
#                 28000, 31000, 27000, 35000, 33000, 40000]
# })
# sales["MA_3"] = sales["Revenue"].rolling(3).mean()
# sales["Cumulative"] = sales["Revenue"].cumsum()
# sales["Pct_Change"] = sales["Revenue"].pct_change()

# SOLUTION:
print("SOLUTION:")
sales = pd.DataFrame({
    "Month": pd.date_range("2024-01-01", periods=12, freq="MS"),
    "Revenue": [15000, 18000, 16500, 22000, 25000, 23000,
                28000, 31000, 27000, 35000, 33000, 40000]
})
sales["MA_3"] = sales["Revenue"].rolling(3).mean()
sales["Cumulative"] = sales["Revenue"].cumsum()
sales["Pct_Change"] = sales["Revenue"].pct_change()
print(sales)


# =============================================================================
# EXERCISE 10: Method Chaining (10 min)
# =============================================================================
print("\n--- EXERCISE 10: Method Chaining ---")
print("Tasks:")
print("  Write a single chained pipeline that:")
print("  1. Takes the original employee DataFrame")
print("  2. Filters to only employees earning more than $75,000")
print("  3. Adds a 'Tax' column (20% of salary)")
print("  4. Renames 'Salary' to 'Annual_Pay'")
print("  5. Sorts by Tax descending")
print("  6. Selects only Name, Department, Annual_Pay, Tax columns\n")

# YOUR CODE HERE:
# result = (df.copy()
#     .query("Salary > 75000")
#     .assign(Tax=lambda x: x["Salary"] * 0.20)
#     .rename(columns={"Salary": "Annual_Pay"})
#     .sort_values("Tax", ascending=False)
#     [["Name", "Department", "Annual_Pay", "Tax"]]
# )
# print(result)

# SOLUTION:
print("SOLUTION:")
result = (df.copy()
    .query("Salary > 75000")
    .assign(Tax=lambda x: x["Salary"] * 0.20)
    .rename(columns={"Salary": "Annual_Pay"})
    .sort_values("Tax", ascending=False)
    [["Name", "Department", "Annual_Pay", "Tax"]]
)
print(result)


# =============================================================================
# BONUS CHALLENGE
# =============================================================================
print("\n--- BONUS CHALLENGE ---")
print("Task: Create a complete analysis pipeline that:")
print("  1. Loads example.csv")
print("  2. Adds a 'Years_Experience' column")
print("  3. Groups by Department to get avg salary and avg experience")
print("  4. Merges with a budget DataFrame")
print("  5. Adds a 'ROI' column (Salary / Budget * 100)")
print("  6. Sorts by ROI descending")
print("  7. Saves the result to 'department_analysis.csv'\n")

# YOUR CODE HERE:

# SOLUTION:
print("SOLUTION:")
bonus = (pd.read_csv("example.csv")
    .assign(
        Start_Date=lambda x: pd.to_datetime(x["Start_Date"]),
        Years_Experience=lambda x: 2024 - pd.to_datetime(x["Start_Date"]).dt.year
    )
    .groupby("Department")
    .agg(
        avg_salary=("Salary", "mean"),
        avg_experience=("Years_Experience", "mean"),
        headcount=("Name", "count")
    )
    .reset_index()
    .merge(pd.DataFrame({
        "Department": ["Engineering", "Marketing", "HR"],
        "Budget": [350000, 250000, 200000]
    }), on="Department")
    .assign(ROI=lambda x: round(x["avg_salary"] / x["Budget"] * 100, 1))
    .sort_values("ROI", ascending=False)
)
print(bonus)
bonus.to_csv("department_analysis.csv", index=False)
print("\nSaved to department_analysis.csv")


# =============================================================================
print(f"\n{'='*60}")
print("  All exercises completed!")
print("  Run 'python pandas_examples.py' to see all examples in action.")
print(f"{'='*60}")
