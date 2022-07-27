# Find Graph Function
from colorama import Fore
import datetime


def bar_chart(complete_data, year, month):
    high_temperature = 0
    min_tem_day_max = 0
    min_temperature = 0
    max_tem_day_min = 0
    date = ''
    date_min = ''

    list_of_dic = []

    for dictionaries in complete_data:
        if 'PKT' in dictionaries:

            if dictionaries['PKT'][0:4] == year:
                if month in dictionaries['PKT'][5:7]:
                    list_of_dic.append(dictionaries)

    for row in range(len(list_of_dic)):

        if list_of_dic[row]['Max TemperatureC'] != '':
            if int(list_of_dic[row]['Max TemperatureC']) > high_temperature:
                high_temperature = int(list_of_dic[row]['Max TemperatureC'])
                date = list_of_dic[row]['PKT']
                min_temperature = high_temperature
            elif int(list_of_dic[row]['Max TemperatureC']) < min_temperature:
                min_temperature = int(list_of_dic[row]['Max TemperatureC'])
                date_min = list_of_dic[row]['PKT']

        if list_of_dic[row]['PKT'] == date:
            min_tem_day_max = (int(list_of_dic[row]['Min TemperatureC']))

        if list_of_dic[row]['PKT'] == date_min:
            max_tem_day_min = (int(list_of_dic[row]['Max TemperatureC']))

    date_month_min = datetime.datetime.strptime(date_min, "%Y-%m-%d").strftime("%B")
    day_max = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d")
    day_min = datetime.datetime.strptime(date_min, "%Y-%m-%d").strftime("%d")

    print(date_month_min, year)
    print(Fore.RED, day_max, high_temperature * '+', str(high_temperature) + "C")
    print(Fore.BLUE, day_max, min_tem_day_max * '+', str(min_tem_day_max) + "C")
    print(Fore.RED, day_min, min_temperature * '+', str(min_temperature) + "C")
    print(Fore.BLUE, day_min, max_tem_day_min * '+', str(max_tem_day_min) + "C")
