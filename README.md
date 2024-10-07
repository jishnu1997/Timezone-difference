Overview:
This Python script calculates the difference in UTC offsets between a list of timezones and specific cities (with predefined timezones). The results are saved in a CSV file for easy reference. The core functionality utilizes the pytz library to handle timezone conversions, and the output is presented as a CSV file with rows representing timezones and columns representing the cities.

Requirements:
Python 3.x
Required Libraries:
pytz: For handling timezone data.
pandas: For creating and manipulating the CSV file.
datetime: For fetching the current date and time.
You can install the necessary libraries via:

bash
Copy code
pip install pytz pandas
File Output:
The script generates a CSV file named timezone_differences_with_cities.csv, which contains the UTC offset differences between the timezones and the listed cities.
How to Run:
Ensure all required libraries are installed.
Run the Python script. It will calculate the timezone differences and save the results in a CSV file.
Adding New Timezones:
To add more timezones for comparison, follow these steps:

Update the timezones list:
Add any valid timezone from the IANA Time Zone Database to the timezones list. The timezones must be in string format and match the names from the pytz library. Example:

python
Copy code
timezones.append("America/Toronto")
Update the cities dictionary (Optional):
If you want to compare with more cities, update the cities dictionary by adding new city names and their respective timezones. Example:

python
Copy code
cities["Toronto"] = "America/Toronto"
