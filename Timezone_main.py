import pytz  # Library to handle timezone conversions
from datetime import datetime  # For fetching the current time
import pandas as pd  # To handle dataframes and CSV creation

# List of timezones to compare against cities
timezones = [
    "America/New_York", "America/Chicago", "America/Los_Angeles", 
    # ... (more timezones) 
    "America/Indiana/Winamac"
]

# Cities and their respective timezones for comparison
cities = {
    "Auckland": "Pacific/Auckland",
    "Austin": "America/Chicago",
    # ... (more cities) 
    "Atlanta": "America/New_York"
}

# Function to calculate the UTC offset difference between a target timezone and a reference timezone
def calculate_utc_offset_difference(tz_name, reference_tz):
    try:
        # Get the timezone object for the target timezone
        target_timezone = pytz.timezone(tz_name)
        
        # Get the UTC offset for the reference timezone
        reference_offset = reference_tz.utcoffset(datetime.now()).total_seconds() / 3600
        
        # Get the UTC offset for the target timezone
        target_offset = target_timezone.utcoffset(datetime.now()).total_seconds() / 3600
        
        # Return the difference in hours, rounded to 2 decimal places
        return round(target_offset - reference_offset, 2)
    except Exception as e:
        return None  # Return None if there's any error with the timezone

# List to store the result of timezone differences
data = []

# Loop through each timezone to compare with all cities
for tz in timezones:
    city_diffs = {}
    
    # For each city, calculate the offset difference
    for city_name, city_tz in cities.items():
        city_diffs[city_name] = calculate_utc_offset_difference(tz, pytz.timezone(city_tz))
    
    # Append the timezone and differences to the data list
    data.append([tz] + list(city_diffs.values()))

# Convert the data into a Pandas DataFrame for easy manipulation and CSV export
columns = ['Timezone'] + list(cities.keys())  # Column names: Timezone and city names
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
csv_file_path = 'timezone_differences_with_cities.csv'
df.to_csv(csv_file_path, index=False)  # Save without the index column

# Output the CSV file path
print(f"CSV file created: {csv_file_path}")
