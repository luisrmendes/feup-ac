import csv

with open('ficheiros_competicao/district.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=';'))

print(data)