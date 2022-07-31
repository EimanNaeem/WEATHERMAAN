from colorama import Fore

from readings import Readings
from data import monthly
from data import yearly


class main:

    def __init__(self):
        self.readings = Readings()

    def for_yearly(self, weather_data, year):
        whole_weather_data = yearly(weather_data, year)
        max_temperature, (month_max, day_max) = self.readings.find_max_temp(whole_weather_data)
        min_temperature, (month_min, day_min) = self.readings.find_min_temp(whole_weather_data)
        humidity, (month, day) = self.readings.find_max_humidity(whole_weather_data)

        print("Year", year)
        print("Highest:", f"{max_temperature}C On", month_max, day_max)
        print("Lowest:", f"{min_temperature}C On", month_min, day_min)
        print("Humidity:", f"{humidity}% On", month, day)

    def for_monthly(self, weather_data, year, month):
        whole_weather_data = monthly(weather_data, year, month)
        avg_max_temp, avg_min_temp, avg_mean_humidity = self.readings.find_average_temp(whole_weather_data)

        print("Highest Average", f"{avg_max_temp}C")
        print("Lowest Average", f"{avg_min_temp}C")
        print("Average Mean Humidity:", f"{avg_mean_humidity}%")

    def bar_chart(self, weather_data, year, month):
        whole_weather_data = monthly(weather_data, year, month)

        for weather_info in whole_weather_data:
            print(Fore.RED, weather_info['date'].day, (weather_info['max_temperature']) * '+',
                  f"{weather_info['min_temperature']} C")
            print(Fore.BLUE, weather_info['date'].day, (weather_info['min_temperature']) * '+',
                  f"{weather_info['min_temperature']}C")
