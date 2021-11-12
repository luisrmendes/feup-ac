import csv
import pandas as pd
import matplotlib.pyplot as plt

# with open('ficheiros_competicao/loan_train.csv') as csv_file:
#     csv_read=csv.reader(csv_file, delimiter=',')

csv_file="ficheiros_competicao/loan_train.csv"
data = pd.read_csv(csv_file)

print(Votes = data["TotalVotes"])
