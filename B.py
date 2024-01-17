import pandas as pd

# Read the Excel file
data = pd.read_excel("./Assignment_Timecard.csv")

# Convert 'Timecard Hours (as Time)' column to a new timedelta column
data['Timecard Duration'] = pd.to_timedelta(data['Timecard Hours (as Time)'].apply(lambda x: f"{x}:00"), errors='coerce')

# Filter the data based on Timecard Duration
filtered_data = data[(data['Timecard Duration'] > pd.Timedelta(hours=1)) & (data['Timecard Duration'] < pd.Timedelta(hours=10))]

# Drop duplicate entries based on 'Employee Name'
filtered_data_unique = filtered_data.drop_duplicates(subset='Employee Name')

# Display Employee Name and Position Status for the filtered and unique data
result = filtered_data_unique[['Employee Name', 'Position Status']]

# Append the result to 'output.txt'
with open("output.txt", "a") as file:
    print("\nAppended Data:\n", file=file)
    print(result, file=file)

print("Output appended to 'output.txt'")
