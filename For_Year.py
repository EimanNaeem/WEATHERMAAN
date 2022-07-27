import datetime


def given_year(complete_data, year):
    temperature = 0
    min_temperature = 0
    humidity = 0
    date = ''
    date_min = ''
    date_humidity = ''

    list_of_dict = []
    for dictionaries in complete_data:

        if 'PKT' in dictionaries:
            if dictionaries['PKT'][0:4] == year:
                list_of_dict.append(dictionaries)

                for i in range(len(list_of_dict)):
                    if list_of_dict[i]['Max TemperatureC'] != '':
                        if int(list_of_dict[i]['Max TemperatureC']) > temperature:
                            temperature = int(list_of_dict[i]['Max TemperatureC'])
                            date = list_of_dict[i]['PKT']
                            min_temperature = temperature
                        elif int(list_of_dict[i]['Max TemperatureC']) < min_temperature:
                            min_temperature = int(list_of_dict[i]['Max TemperatureC'])
                            date_min = list_of_dict[i]['PKT']
                        elif int(list_of_dict[i]['Max Humidity']) > humidity:
                            humidity = int(list_of_dict[i]['Max Humidity'])
                            date_humidity = list_of_dict[i]['PKT']

    date_month_max = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%B")
    date_month_min = datetime.datetime.strptime(date_min, "%Y-%m-%d").strftime("%B")
    day_max = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d")
    day_min = datetime.datetime.strptime(date_min, "%Y-%m-%d").strftime("%d")
    month_humidity = datetime.datetime.strptime(date_humidity, "%Y-%m-%d").strftime("%B")
    day_humidity = datetime.datetime.strptime(date_humidity, "%Y-%m-%d").strftime("%d")

    year = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y")

    print("For the Year", year)
    print("Highest:", str(temperature) + "C On", date_month_max, day_max)
    print("Lowest:", str(min_temperature) + "C On", date_month_min, day_min)
    print("Humidity:", str(humidity) + "% On", month_humidity, day_humidity)
