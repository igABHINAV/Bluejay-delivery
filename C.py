import pandas as pd

# Read the Excel file
data = pd.read_excel("./Assignment_Timecard.csv")

# Convert 'Timecard Hours (as Time)' column to a new timedelta column
data['Timecard Duration'] = pd.to_timedelta(data['Timecard Hours (as Time)'].apply(lambda x: f"{x}:00"), errors='coerce')

filtered_data2 = data[(data['Timecard Duration'] > pd.Timedelta(hours=14))]
filtered_data_unique2 = filtered_data2.drop_duplicates(subset='Employee Name')
result = filtered_data_unique2[['Employee Name', 'Position Status']]

# Append the result to 'output.txt'
with open("output.txt", "a") as file:
    print("\nAppended Data2:\n", file=file)
    print(result, file=file)

print("Output2 appended to 'output.txt'")
