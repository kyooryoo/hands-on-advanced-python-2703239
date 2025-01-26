import json
from functools import reduce

def miserable_day():
    """ find the most miserable day in the data set """
    with open("../../sample-weather-history.json", "r", encoding="utf-8") as weatherfile:
        weatherdata = json.load(weatherfile)
    return reduce(day_rank, weatherdata)

def day_rank(acc, elem):
    """ rank the day to find the most miserable one """
    return acc if misery_score(acc) >= misery_score(elem) else elem

def misery_score(day):
    """ define how to score the miserable day """
    wind = 0 if day['awnd'] is None else day['awnd']
    temp = day['tmax'] * .8
    rain = day['prcp'] * 10

    return (temp + rain + wind) / 3

result = miserable_day()
print(result)
