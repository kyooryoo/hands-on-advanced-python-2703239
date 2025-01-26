import json
import pprint
import random

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

year = "2020"
month = "12"

def select(d):
    if year+"-"+month in d['date']:
        return True
    return False
days = list(filter(select, weatherdata))
for d in random.sample(days, k=5):
    print(d['date'])