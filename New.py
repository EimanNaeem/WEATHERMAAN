import csv
import os


class Reading:

    def __init__ (self, min_temp, max_temp, date, max_humidity):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.date = date
        self.max_humidity = max_humidity


class FileHandler:
    def __init__ (self):
        self.dir_name = 'weatherdata'


def read_data(self, file_name, readings):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            reading = Reading(row['PKT'], row['Max TemperatureC'], row['Min TemperatureC'], row['Max Humidity'])
            readings.append(reading)


def get_yearly_data(self, year):
    file_names = os.listdir(self.dir_name)
    chosen_files = []
    for file_name in file_names:
        if file_name.contains(str(year)):
            chosen_files.append(file_name)

            readings = []
            for file_name in chosen_files:
                self.read_data(file_name, readings)
                return readings


def get_max_temp(data):
    max_temp = float('-inf')
    for i in data:
        if max_temp < i['Max TemperatureC']:
            max_temp = i['Max TemperatureC']


def get_min_temp(data):
    min_temp = float('inf')
    for i in data:
        if min_temp > i['Min TemperatureC']:
           min_temp = i['Min TemperatureC']


def get_max_humidity(data):
    max_humidity = float('-inf')
    for i in data:
        if max_humidity < i['Max Humidity']:
           max_humidity = i['Max Humidity']


def main():
    file_handler = FileHandler()
    yearly_data = file_handler.get_yearly_data('2002')


if __name__ == '__main__'
        main()
