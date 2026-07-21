import pandas as pd

# Create a dictionary
student_data = {
    "Name": ["Varsha", "Priya", "Rahul", "Arun", "Divya"],
    "Age": [20, 21, 22, 20, 23],
    "Department": ["CSE", "IT", "ECE", "CSE", "IT"],
    "Marks": [85, 90, 78, 88, 95]
}

# Create DataFrame
df = pd.DataFrame(student_data)

# Display the DataFrame
print("Student Data")
print(df)

# Display first 3 rows
print("\nFirst 3 Rows")
print(df.head(3))

# Display last 2 rows
print("\nLast 2 Rows")
print(df.tail(2))

# Display DataFrame information
print("\nDataFrame Info")
print(df.info())

# Display statistical summary
print("\nStatistics")
print(df.describe())

# Display column names
print("\nColumn Names")
print(df.columns)

# Display only Name and Marks columns
print("\nName and Marks")
print(df[["Name", "Marks"]])

# Find students with marks greater than 85
print("\nStudents with Marks > 85")
print(df[df["Marks"] > 85])

# Average marks
print("\nAverage Marks")
print(df["Marks"].mean())

# Maximum marks
print("\nHighest Marks")
print(df["Marks"].max())

# Minimum marks
print("\nLowest Marks")
print(df["Marks"].min())