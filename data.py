import csv
import glob
import os


class weatherdata:
    def get_files_data(self):
        path_data = "C:\\Users\\kcs\\Desktop\\Assignment 1\\weatherdata\\ *.txt"
        os.chdir('weatherdata')

# yearly


def yearly(weather_data, year):
    return [weather_info for weather_info in weather_data if weather_info['date'].year == year]

# monthly


def monthly(weather_data, year, month):
    return [weather_info for weather_info in weather_data
            if weather_info['date'].year == year and weather_info['date'].month == month]


def parse_date(date):
    return date.strftime('%B'), date.strftime('%d')