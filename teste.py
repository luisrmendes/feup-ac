# load csv module
import csv

# open file for reading
file_name = 'ficheiros_competicao/loan_test.csv'
with open(file_name) as csvDataFile:

    # read file as csv file, demilitador = ;
    csvReader = csv.reader(csvDataFile, delimiter=';')

    # for every row, print the row
    for row in csvReader:
        print(row)