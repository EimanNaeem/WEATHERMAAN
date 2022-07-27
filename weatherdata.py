import zipfile
import os

# Class weatherdata:


def get_files_data():

    path_data = "C:\\Users\\kcs\\Desktop\\Assignment 1\\weatherdata\\ *.txt"
    os.chdir('weatherdata')
    new_directory = os.getcwd()

    data = []
    for root, folder, files in os.walk(new_directory):
        for file in files:
            path = os.path.join(root, file)
            with open(path, 'r') as read_file:
                data.append(read_file.readlines())

    complete_data = []
    keys = []

    for data_no in range(len(data)):
        for i in range(len(data[data_no])):
            lis = data[data_no]
            if i == 0:
                keys = lis[i].split(',')
            elif i > 0:
                dictionary = dict(zip(keys, data[data_no][i].split(',')))
                complete_data.append(dictionary)
    return complete_data
