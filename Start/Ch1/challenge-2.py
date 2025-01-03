import json
import pprint

def get_day_temp_descriptions():
    # Your code goes 
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def CWH(d):
        evg_temp = (d['tmin'] + d['tmax']) / 2
        if evg_temp <= 60:
            return "code"
        elif evg_temp >= 80:
            return "hot"
        else:
            return "warm"

    result = list(map(lambda d:(d['date'],CWH(d)), weatherdata))
    return result

result = get_day_temp_descriptions()
pprint.pp(result[:5])