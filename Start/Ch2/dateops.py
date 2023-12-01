# Example file for Advanced Python: Hands On by Joe Marini
# Working with date values

import json
from datetime import date, timedelta


# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# TODO: The datetime module converts strings into dates fairly easily
# dateobj = date.fromisoformat(weatherdata[0]['date'])
# print(dateobj)


# # TODO: Date objects give us information such as day of week (0=Monday, 6=Sunday)
# print(dateobj.weekday())


# # TODO: what was the warmest weekend day in the dataset?
# def is_weekend(d):
    
#     return (date.fromisoformat(d['date']).weekday() == 5 or date.fromisoformat(d['date']).weekday() == 6)

# weekend_list = list(filter(is_weekend, weatherdata))
# warmest_weekend = max(weekend_list, key= lambda d:d['tmax'])
# print(f"The warmest day is {date.fromisoformat(warmest_weekend['date']).strftime('%A, %Y %B %d')}, at {warmest_weekend['tmax']}")

# The timedelta object provides an easy way of performing date math
# find the coldest day of the year and get the average temp for the following week
coldest_day = min(weatherdata, key=lambda d: d['tmin'])
# convert the date to a Python date
coldest_date = date.fromisoformat(coldest_day['date'])
print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']})")

# TODO: Look up the next 7 days
avg_temp = 0.0
next_date = coldest_date

for _ in range(7):
    next_date +=timedelta(days=1)
    wd = next((day for day in weatherdata if day['date']==str(next_date)),None)
    avg_temp += (wd['tmin']+wd['tmax'])/2

avg_temp = avg_temp/7

print(f"Average temprature from the day of coldest date is {avg_temp} degrees.")
