# Example file for Advanced Python: Hands On by Joe Marini
# Transform data from one format to another

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the map() function is used to transform data from one form to another
# TODO: Let's convert the weather data from imperial to metric units
def ToC(f):
    f = 0 if f is None else f
    return (f - 32) * 5/9


def ToMM(i):
    i = 0 if i is None else i
    return i * 25.4


def ToKPH(s):
    s = 0 if s is None else s
    return s * 1.60934


def ToMetric(wd):
    new_wd = copy.copy(wd)
    new_wd['tmin'] = ToC(new_wd['tmin'])
    new_wd['tmax'] = ToC(new_wd['tmax'])
    new_wd['snow'] = ToMM(new_wd['snow'])
    new_wd['prcp'] = ToMM(new_wd['prcp'])
    new_wd['snwd'] = ToMM(new_wd['snwd'])
    new_wd['awnd'] = ToKPH(new_wd['awnd'])

    return new_wd


    

# TODO: Use map() to call ToMetric and convert weatherdata to metric
# dataset = list(map(ToMetric, weatherdata))

# pprint.pp(weatherdata[0])
# pprint.pp(dataset[0])

# TODO: use the map() function to convert objects to tuples
# in this case, create tuples with a date and the average of tmin and tmax
Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0
def tupleTrans(d):
    
    return (d['date'],Avg_Temp(d['tmin'],d['tmax']))

tupleData = list(map(tupleTrans, weatherdata))

pprint.pp(len(tupleData))