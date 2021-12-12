from data.bank_data import Bank_Data
from data.district import District
from data.enum_types import Order
from os.path import exists
import os

import utils.csv_loader as CsvLoader
import sys

def load_test_data():
    filename = "csv_files/dataTest.csv"

    if not exists(filename):
        print(filename, " not found, generating . . .\n")
    else:
        print(filename, " exists, regen?\n")
        ans = input("y/n: ")
        if ans != 'y':
            exit(0)

        os.remove(filename) 

        print("\n")

        data = Bank_Data()

        print("Loading districts . . .\n")
        data.add_districts("data/ficheiros_competicao/district.csv")
        print("Loading clients . . .\n")
        data.add_clients("data/ficheiros_competicao/client.csv")
        print("Loading accounts . . .\n")
        data.add_accounts("data/ficheiros_competicao/account.csv")
        print("Loading dispositions . . .\n")
        data.add_dispositions("data/ficheiros_competicao/disp.csv")

        print("Loading test loans . . .\n")
        data.add_loans("data/ficheiros_competicao/loan_test.csv")
        print("Loading test cards . . .\n")
        data.add_cards("data/ficheiros_competicao/card_test.csv")
        print("Loading test transactions . . .\n")
        data.add_transactions("data/ficheiros_competicao/trans_test.csv")
    
        # Load csv
        CsvLoader.populate_csv(data, filename)

        print("Done\n")
 
def load_train_data():
    filename = "csv_files/dataTrain.csv"

    if not exists(filename):
        print(filename, " not found, generating . . .\n")
    else:
        print(filename, " exists, regen?\n")
        ans = input("y/n: ")
        if ans != 'y':
            exit(0)

        os.remove(filename) 

        print("\n")
            
    data = Bank_Data()

    print("Loading districts . . .\n")
    data.add_districts("data/ficheiros_competicao/district.csv")
    print(data.get_districts()[68].get_unemploymant_95())
    print(data.get_districts()[68].get_n_crimes_95())
    print("Loading clients . . .\n")
    data.add_clients("data/ficheiros_competicao/client.csv")
    print("Loading accounts . . .\n")
    data.add_accounts("data/ficheiros_competicao/account.csv")
    print("Loading dispositions . . .\n")
    data.add_dispositions("data/ficheiros_competicao/disp.csv")

    print("Loading train loans . . .\n")
    data.add_loans("data/ficheiros_competicao/loan_train.csv")
    print("Loading train cards . . .\n")
    data.add_cards("data/ficheiros_competicao/card_train.csv")
    print("Loading train transactions . . .\n")
    data.add_transactions("data/ficheiros_competicao/trans_train.csv")
        
    # Load csv
    CsvLoader.populate_csv(data, filename)

    print("Done\n")

if len(sys.argv) != 2:
    print("Usage: python dataPreparation.py <train | test>")
    exit(1)
else:
    if sys.argv[1] == "test":
        load_test_data()
    elif sys.argv[1] == "train":
        load_train_data()
    else:
        print("Incorrect argument ", sys.argv[1], ", use test or train")

#list = data.districts
#list = data.quicksort(list, District.get_n_inhab, Order.Decreasing)
#list = data.filter(list, District.get_average_salary, "<", 8200)
#for member in list:
#    member.print()

# data.print()

# list2 = data.districts
# all_avg_salary = data.get_all(list2, District.get_average_salary)
# print(getAverage(all_avg_salary))

# Metrics.display_client_metrics(data)
# Metrics.display_loan_metrics(data)


