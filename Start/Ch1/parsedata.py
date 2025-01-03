# Example file for Advanced Python: Hands On by Joe Marini
# Load and parse a JSON data file and determine some information about it

import json
import pprint

# TODO: open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as file:
    data = json.load(file)

# TODO: make sure the data loaded correctly by printing the length of the dataset
print(len(data))

# TODO: let's also take a look at the first item in the data
pprint.pp(data[0])

# TODO: How many days of data do we have for each year?
years = {}

for d in data:
    key = d['date'][:4]
    if key in years:
        years[key] += 1
    else:
        years[key] = 1 

pprint.pp(years, width=5)
