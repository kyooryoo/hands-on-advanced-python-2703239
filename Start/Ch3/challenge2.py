import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r", encoding="utf-8") as weatherfile:
    weatherdata = json.load(weatherfile)

def average_temp(day):
    """ get the average temprature based on the min and max temperatures of the day """
    return (day['tmin'] + day['tmax']) / 2

# define the winter months
winter = ["-12-","-01-","-02-"]
# get the winter days out from the weather dataset
winter_days = [d for d in weatherdata if any([month in d['date'] for month in winter])]
# get the average temperature of the winter days
mean_temps = [average_temp(d) for d in winter_days]
# define the outlier value based on the mean temperature of each day
outlier = statistics.mean(mean_temps) + statistics.stdev(mean_temps) * 2
# get the days that have mean temperature above the outlier value
mean_outlier = [t for t in mean_temps if t >= outlier]
# calculate the number of days that have mean temperature above the outlier value
print(f"There are {len(mean_outlier)} warm days in winter.")
