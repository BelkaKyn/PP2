1.
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Five days ago:", new_date.strftime("%Y-%m-%d"))
2.
from datetime import datetime, timedelta

current_date = datetime.now()

yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

3.
from datetime import datetime

current_datetime_with_microseconds = datetime.now()

current_datetime_without_microseconds = current_datetime_with_microseconds.replace(microsecond=0)

print("Original datetime with microseconds:", current_datetime_with_microseconds)
print("Datetime with microseconds dropped:", current_datetime_without_microseconds)

4.
from datetime import datetime

def date_difference_in_seconds(date1, date2):
    difference = date2 - date1
    
    difference_seconds = difference.total_seconds()
    
    return difference_seconds

date_format = "%Y-%m-%d %H:%M:%S"

date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

difference_seconds = date_difference_in_seconds(date1, date2)

print("Difference between the two dates in seconds:", difference_seconds)

