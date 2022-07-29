import argparse

from data import weatherdata
from main import main

#Argument Parsing
main = main()
data = weatherdata()
weatherdata.get_files_data()
main.for_monthly()
main.for_yearly()
main.bar_chart()

parser = argparse.ArgumentParser()
parser.add_argument('-e', help=" According to Years", nargs='?')
parser.add_argument('-a', help="According to Months", nargs='?', type=str)
parser.add_argument('-c', help="Bar charts", nargs='?', type=str)
parser.add_argument("get_files_path", help="Files Path", type=str)


parameters = parser.parse_args()

if parameters.e:
    main.for_yearly(weatherdata, parameters.e)
    print("\n")
if parameters.a:
    monthly   = parameters.a
    main.for_monthly(weatherdata, monthly.split('/')[0], monthly.split('/')[1])
    print("\n")
 if parameters.c:
     chart = parameters.c
     main.bar_chart(weatherdata, chart.split('/')[0], chart.split('/')[1])
        print("\n")

