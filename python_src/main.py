from data.bank_data import Bank_Data
from data.district import District
from data.enum_types import Order

import utils.metrics as Metrics

data = Bank_Data()

data.add_districts("data/ficheiros_competicao/district.csv")
data.add_clients("data/ficheiros_competicao/client.csv")
data.add_accounts("data/ficheiros_competicao/account.csv")
data.add_dispositions("data/ficheiros_competicao/disp.csv")
data.add_loans("data/ficheiros_competicao/loan_train.csv")
data.add_cards("data/ficheiros_competicao/card_train.csv")
data.add_transactions("data/ficheiros_competicao/trans_train.csv")

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
Metrics.display_loan_metrics(data)
