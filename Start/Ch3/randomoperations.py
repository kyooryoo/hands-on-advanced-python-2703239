# Example file for Advanced Python: Hands On by Joe Marini

import json
import random
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# get the first 30 days in the dataset
month_data = weatherdata[0:30]

# TODO: the shuffle() function will randomly shuffle a list in-place
pprint.pp(month_data[:3])
print("-"*40)
random.shuffle(month_data)
pprint.pp(month_data[:3])
print("-"*40)
random.shuffle(month_data)
pprint.pp(month_data[:3])

# TODO: use choice() and choices() to get random items, but beware that
# these functions can produce duplicate results
print("-"*40)
rnd_day = random.choice(month_data)
pprint.pp(rnd_day)
print("-"*40)
rnd_days = random.choices(month_data, k=3)
pprint.pp(rnd_days)

# TODO: the sample() function will choose random items with no duplicates
print("-"*40)
smp_days = random.sample(month_data, k=3)
pprint.pp(smp_days)