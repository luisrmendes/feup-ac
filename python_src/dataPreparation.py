from data.bank_data import Bank_Data
from data.district import District
from data.enum_types import Order
from os.path import exists

import utils.metrics as Metrics
import utils.csv_loader as CsvLoader

if not exists("dataPrepTest.csv"):
    print("dataPrep.csv not found, generating . . .\n")
    
    data = Bank_Data()

    print("Loading districts . . .\n")
    data.add_districts("data/ficheiros_competicao/district.csv")
    print("Loading clients . . .\n")
    data.add_clients("data/ficheiros_competicao/client.csv")
    print("Loading accounts . . .\n")
    data.add_accounts("data/ficheiros_competicao/account.csv")
    print("Loading dispositions . . .\n")
    data.add_dispositions("data/ficheiros_competicao/disp.csv")
    print("Loading loans . . .\n")
    data.add_loans("data/ficheiros_competicao/loan_test.csv")
    print("Loading cards . . .\n")
    data.add_cards("data/ficheiros_competicao/card_test.csv")
    print("Loading transactions . . .\n")
    data.add_transactions("data/ficheiros_competicao/trans_test.csv")
    # print("Loading loans . . .\n")
    # data.add_loans("data/ficheiros_competicao/loan_train.csv")
    # print("Loading cards . . .\n")
    # data.add_cards("data/ficheiros_competicao/card_train.csv")
    # print("Loading transactions . . .\n")
    # data.add_transactions("data/ficheiros_competicao/trans_train.csv")

    # Load csv
    CsvLoader.populate_csv(data)

    print("Done\n")
else:
    print("dataPrep.csv exists, not generating\n")



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


