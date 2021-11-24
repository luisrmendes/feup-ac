from data.bank_data import Bank_Data
from data.district import District
from data.enum_types import Order
from data.utils import *
import matplotlib.pyplot as plt

data = Bank_Data()

data.add_districts("data/ficheiros_competicao/district.csv")
data.add_clients("data/ficheiros_competicao/client.csv")
data.add_accounts("data/ficheiros_competicao/account.csv")
data.add_dispositions("data/ficheiros_competicao/disp.csv")
data.add_loans("data/ficheiros_competicao/loan_train.csv")
data.add_cards("data/ficheiros_competicao/card_train.csv")
data.add_transanctions("data/ficheiros_competicao/trans_train.csv")

#list = data.districts
#list = data.quicksort(list, District.get_n_inhab, Order.Decreasing)
#list = data.filter(list, District.get_average_salary, "<", 8200)
#for member in list:
#    member.print()

# data.print()


list2 = data.districts
all_avg_salary = data.get_all(list2, District.get_average_salary)

print(getAverage(all_avg_salary))


# left_coordinates = [1, 2, 3, 4, 5]
# heights = [10, 20, 30, 15, 40]
# bar_labels = ['One', 'Two', 'Three', 'Four', 'Five']
# plt.bar(left_coordinates, heights, tick_label=bar_labels,
#         width=0.6, color=['red', 'black'])
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title("A simple bar graph")
# plt.show()
