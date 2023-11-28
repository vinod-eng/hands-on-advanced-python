# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r", encoding="utf-8") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warmestday = max(weatherdata, key = lambda x:x['tmax'])
print(f"The warmest day in the weatherdata is {warmestday['tmax']} degrees on {warmestday['date']}")

# TODO: What was the coldest day in the data set?
coldestday = min(weatherdata, key= lambda x:x['tmin'])
print(f"The coldest day was {coldestday['tmin']} degrees on {coldestday['date']}")

# TODO: How many days had snowfall?
# snowdays = 0
# for date in weatherdata:
#     if date['snow']>0:
#         snowdays += 1 
snowdays = [date for date in weatherdata if date['snow']>0]

print(f"The total number of snow days in weatherdata is {len(snowdays)} ")
pprint.pprint(f"The snowdays are {snowdays}")
