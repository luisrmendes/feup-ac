from data.bank_data import Bank_Data
from data.district import District
from data.enum_types import Order

data = Bank_Data()

data.add_districts("data/ficheiros_competicao/district.csv")
data.add_clients("data/ficheiros_competicao/client.csv")
data.add_accounts("data/ficheiros_competicao/account.csv")
data.add_dispositions("data/ficheiros_competicao/disp.csv")

list = data.districts
list = data.quicksort(list, District.get_n_inhab, Order.Decreasing)
list = data.filter(list, District.get_average_salary, "<", 8200)
for member in list:
    member.print()

data.print()