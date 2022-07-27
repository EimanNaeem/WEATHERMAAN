import datetime


def given_month(complete_data, year, month):

    avg_temperature = 0
    avg_min_temperature = 0
    avg_humidity = 0
    date = ''

    list_of_dict = []

    for dictionaries in complete_data:
        if 'PKT' in dictionaries:

            if dictionaries['PKT'][0:4] == year:
                if month in dictionaries['PKT'][5:7]:
                    list_of_dict.append(dictionaries)

    for row in range(len(list_of_dict)):
        if "Max TemperatureC" in list_of_dict[row]:
            if (list_of_dict[row]['Max TemperatureC']) != '':

                avg_temperature = int(avg_temperature) + int(list_of_dict[row]['Max TemperatureC'])
                date = list_of_dict[row]['PKT']
            if (list_of_dict[row]['Min TemperatureC']) != '':
                avg_min_temperature = int(avg_min_temperature) + int(list_of_dict[row]['Min TemperatureC'])

            if (list_of_dict[row]['Max Humidity']) != '':
                avg_humidity = int(avg_humidity) + int(list_of_dict[row]['Max Humidity'])
    if len(list_of_dict) > 0:
        avg = avg_temperature//len(list_of_dict)
        avg_min = avg_min_temperature//len(list_of_dict)
        avg_max_humidity = avg_humidity//len(list_of_dict)

        date_month_min = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%B")

        print("For the Year", year, date_month_min)
        print("Highest Average:", str(avg) + "C")
        print("Lowest Average:", str(avg_min) + "C")
        print("Highest Average:", str(avg_max_humidity) + "%")
    else:
        print("Not in given month")
