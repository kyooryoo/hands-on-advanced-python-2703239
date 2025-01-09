import json
import pprint

def is_bad_day(d):
    # your code goes here
    prec = d['prcp']>0.7 or d['snow']>0.7
    avg_temp = (d['tmin']+d['tmax'])/2< 45
    return prec and avg_temp and d['awnd']>10

with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


bad_days = list(filter(is_bad_day, weatherdata))
pprint.pp(bad_days)
print(f"{len(bad_days)} out of {len(weatherdata)} days are bad")