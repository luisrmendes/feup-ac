# load csv module
import csv
import pandas as pd

def getAverage(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

file_name = 'ficheiros_competicao/loan_test.csv'

# open file for reading
# with open(file_name) as csvDataFile:

#     # read file as csv file, demilitador = ;
#     csvReader = csv.reader(csvDataFile, delimiter=';')

#     # for every row, print the row
#     for row in csvReader:
#         print(row)

df = pd.read_csv(file_name, delimiter=';')
# print(df.loc[:,"duration"].to_list())
print(getAverage(df.loc[:,"duration"].to_list()))
# print(df.loc[0])
