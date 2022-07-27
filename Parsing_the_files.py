import argparse
from For_Year import given_year
from For_months import given_month
from Bar_Chart import bar_chart
from weatherdata import get_files_data

parser = argparse.ArgumentParser()
parser.add_argument('-e', help=" According to Years", nargs='?')
parser.add_argument('-a', help="According to Months", nargs='?', type=str)
parser.add_argument('-c', help="Bar charts", nargs='?', type=str)

complete_data = get_files_data()

parameters = parser.parse_args()
if parameters.e:
    given_year(complete_data, parameters.e)
    print("\n")
if parameters.a:
    monthly = parameters.a
    given_month(complete_data, monthly.split('/')[0], monthly.split('/')[1])
    print("\n")
if parameters.c:
    graph = parameters.c
    bar_chart(complete_data, graph.split('/')[0], graph.split('/')[1])
    print("\n")
