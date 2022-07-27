import zipfile
import datetime
weatherdata = zipfile.ZipFile('C:\\Users\\kcs\\Desktop\\Assignment 1\\weatherdata.zip')

files = weatherdata.namelist()
print(files)

weatherdata = open('C:\\Users\\kcs\\Desktop\\Assignment 1\\lahore_weather_1996_Dec.txt', ' r')
print(weatherdata.read())
weather_data = weatherdata.readlines()
print(weather_data)
print(type(weather_data))

whole_data = []
keys = []


for i in range(len(weather_data)):
    if i == 0:
        keys = weather_data[i].split(',')
    else:
        print(i)
        whole_data.append(dict(zip(keys, weather_data[i].split(','))))
print(whole_data)

index = 0
temperature = 0
date_max = ''
print(whole_data[0]['PKT'][5:7])
for i in range(len(whole_data)):
    if whole_data[i]['Max TemperatureC'] != '':
        if int(whole_data[i]['Max TemperatureC']) > temperature:
            index = i
            temperature = int(whole_data[i]['Max TemperatureC'])
            date_max = whole_data[i]['PKT']
# print('Date: {0}, tem: {1}'.format(index+1, temperature))
print(date_max)
min_temperature = temperature
index_min = 0
date_min = ''
for i in range(len(whole_data)):
    if whole_data[i]['Min TemperatureC'] != '':
        if int(whole_data[i]['Min TemperatureC']) < min_temperature:
            index_min = i
            min_temperature = int(whole_data[i]['Min TemperatureC'])
            date_min = whole_data[i]['PKT']
print(date_min)
humidity = 0
humidity_index = 0

for i in range(len(whole_data)):
    if whole_data[i]['Max Humidity'] != '':
        if int(whole_data[i]['Max Humidity']) > humidity:
            humidity_index = i
            humidity = int(whole_data[i]['Max Humidity'])

# Display Highest , Lowest and Humidity

date_max = datetime.datetime.strptime(date_max, "%Y-%m-%d").strftime("%B")
day_max = datetime.datetime.strptime(date_max, "%Y-%m-%d").strftime("%d")
date_main = datetime.datetime.strptime(date_min, "%Y-%m-%d").strftime("%B")


print("Highest: ", temperature, "C on", date_max, day_max)
print("Lowest: ", min_temperature, "C on", date_min, index_min+1)
print("Humidity: ", humidity, "% on", date_max, humidity_index+1)

print(type(whole_data))
