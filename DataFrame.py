import pandas as pd

# 1. Create a sample dataset
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rahul", "Rohit"],
    "Age": [21, 22, None, 23, 21, 24],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR"],
    "Salary": [35000, 30000, 40000, None, 35000, 32000]
}

# Create DataFrame
df = pd.DataFrame(data)

# 2. Explore the dataset
print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 3. Check DataFrame and Series
print("\nDataFrame:")
print(df)

print("\nSalary Series:")
print(df["Salary"])

# 4. Filter data
print("\nEmployees with Salary greater than 32000:")
print(df[df["Salary"] > 32000])

# 5. Select specific columns
print("\nName and Department:")
print(df[["Name", "Department"]])

# 6. Sort data
print("\nEmployees sorted by Salary:")
print(df.sort_values("Salary", ascending=False))

# 7. Handle missing/null values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nAfter handling missing values:")
print(df)

# 8. Remove duplicate records
df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df)

# 9. GroupBy and Aggregation
print("\nAverage salary by department:")
print(df.groupby("Department")["Salary"].mean())

print("\nDepartment-wise statistics:")
print(
    df.groupby("Department")["Salary"].agg(["mean", "max", "min", "count"])
)

# 10. Derived column
df["Annual_Salary"] = df["Salary"] * 12

print("\nFinal DataFrame:")
print(df)

# 11. Basic insights
highest_salary = df["Salary"].max()
average_salary = df["Salary"].mean()

print("\nHighest Salary:", highest_salary)
print("Average Salary:", average_salary)



import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
# Display the entire DataFrame
print(df)