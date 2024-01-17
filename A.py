import pandas as pd
from datetime import timedelta

# Read the Excel file
data = pd.read_excel("./Assignment_Timecard.csv")

# Convert the 'Time' column to datetime format
data['Time'] = pd.to_datetime(data['Time'], errors='coerce', format='%m-%d-%Y %I:%M %p')

# Drop rows with NaT values in the 'Time' column
data = data.dropna(subset=['Time'])

# Sort the dataframe by 'Employee Name' and 'Time'
data.sort_values(['Employee Name', 'Time'], inplace=True)

# Define a function to check if a list of dates is consecutive
def are_consecutive_dates(date_list):
    return all(date_list[i] + timedelta(days=i) == date_list[i + 1] for i in range(len(date_list) - 1))

# Create a set to store unique employees who were present for 7 consecutive days
consecutive_days_set = set()

# Iterate through unique employees
for employee in data['Employee Name'].unique():
    employee_data = data[data['Employee Name'] == employee]
    
    # Iterate through unique dates for the employee
    for date in employee_data['Time'].dt.date.unique():
        date_list = pd.date_range(date, periods=7, freq='D')
        
        # Check if the employee was present for 7 consecutive days
        if are_consecutive_dates(employee_data[employee_data['Time'].dt.date.isin(date_list)]['Time'].dt.date):
            consecutive_days_set.add(employee)

# Convert the set to a list
consecutive_days_list = list(consecutive_days_set)

# Write 'Position Status' and 'Employee Name' for the unique employees to 'output.txt'
with open("output.txt", "w") as file:
    for employee in consecutive_days_list:
        employee_data = data[data['Employee Name'] == employee]
        position_status = employee_data['Position Status'].iloc[0]
        print(f"Position Status: {position_status}, Employee Name: {employee}", file=file)

print("Output written to 'output.txt'")
