import json
import pprint

def get_day_temp_descriptions():
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def CWH(d):
        avg_temp = (d['tmin'] + d['tmax']) / 2
        desc = ""
        if avg_temp <= 60:
            desc = "code"
        elif avg_temp > 60 and avg_temp < 80:
            desc = "warm"
        else:
            desc = "hot"
        return (d['date'], desc)

    return list(map(CWH, weatherdata))

result = get_day_temp_descriptions()
pprint.pp(result[:5])