import matplotlib.pyplot as plt
from data.date import Date
from data.client import Client
from data.loan import Loan
from data.transaction import Transaction
from data.enum_types import TransactionType
import statistics
from data.bank_data import Bank_Data
import numpy as np 


def getAverage(list):
    sum_num = 0
    for t in list:
        sum_num += t

    avg = sum_num / len(list)
    return avg

def valuelabel(subPlot, weight, height):
    for i in range(len(weight)):
        subPlot.text(i+1, height[i], height[i], ha='center',
                 bbox=dict(facecolor='cyan', alpha=0.8))

def display_client_metrics(data):
    print("Generating Client Metrics . . .\n")

    list_clients = data.clients

    fig, axs = plt.subplots(2,3)

    fig.suptitle("Client Metrics")

    # Metricas de idades
    list_of_ages = data.get_all(list_clients, Client.get_birth_date_year)

    age_avg = round(getAverage(list_of_ages), 2)
    age_moda = statistics.mode(list_of_ages)
    age_min = min(list_of_ages)
    age_max = max(list_of_ages)

    left_coordinates1 = [1, 2, 3, 4]
    heights1 = [age_avg, age_moda, age_max, age_min]
    bar_labels1 = ['Media', 'Moda', 'Max', 'Min']

    axs[0, 0].set_title("Client Age")
    axs[0, 0].bar(left_coordinates1, heights1, tick_label=bar_labels1,
        width=0.6, color=['green', 'purple'])
    valuelabel(axs[0, 0], left_coordinates1, heights1)

    # Metricas de Gender
    list_of_genders = data.get_all(list_clients, Client.get_gender)
    count_men = 0
    count_women = 0
    for n in list_of_genders:
        if n == "Men":
            count_men += 1
        elif n == "Women":
            count_women += 1

    left_coordinates2 = [1, 2]
    heights2 = [count_men, count_women]
    bar_labels2 = ['Men', 'Women']
    
    axs[0, 1].set_title("Client Gender")
    axs[0, 1].bar(left_coordinates2, heights2, tick_label=bar_labels2,
        width=0.6, color=['green', 'purple'])

    valuelabel(axs[0, 1], left_coordinates2, heights2)
    
    axs[1, 0].set_title('basic plot')
    axs[1, 0].boxplot(list_of_ages)

    axs[1, 0].set_title('basic plot')
    axs[1, 0].boxplot(list_of_ages, 1)

    plt.show()
    plt.close()

def display_loan_metrics(data):
    print("Generating Loan Metrics . . .\n")

    list_loans = data.loans
    fig, axs = plt.subplots(3, 3)
    fig.suptitle("Loan Metrics")

    # Metricas de ammount
    list_of_ammounts = data.get_all(list_loans, Loan.get_ammount)

    left_coordinates1 = [1, 2, 3, 4]
    heights1 = [
        round(getAverage(list_of_ammounts), 2), 
        statistics.mode(list_of_ammounts), 
        max(list_of_ammounts), 
        min(list_of_ammounts)
    ]
    bar_labels1 = ['Media', 'Moda', 'Max', 'Min']

    axs[0, 0].set_title("Loan Ammount")
    axs[0, 0].bar(left_coordinates1, heights1, tick_label=bar_labels1,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[0, 0], left_coordinates1, heights1)

    # Metricas de duration
    list_of_durations = data.get_all(list_loans, Loan.get_duration)

    left_coordinates2 = [1, 2, 3, 4]
    heights2 = [
        round(getAverage(list_of_durations), 2), 
        statistics.mode(list_of_durations), 
        max(list_of_durations), 
        min(list_of_durations)
    ]
    bar_labels2 = ['Media', 'Moda', 'Max', 'Min']

    axs[0, 1].set_title("Loan Duration")
    axs[0, 1].bar(left_coordinates2, heights2, tick_label=bar_labels2,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[0, 1], left_coordinates2, heights2)

    # Metricas de payments
    list_of_payments = data.get_all(list_loans, Loan.get_payments)

    left_coordinates3 = [1, 2, 3, 4]
    heights3 = [
        round(getAverage(list_of_payments), 2), 
        statistics.mode(list_of_payments), 
        max(list_of_payments), 
        min(list_of_payments)
    ]
    bar_labels3 = ['Media', 'Moda', 'Max', 'Min']

    axs[0, 2].set_title("Loan Payments")
    axs[0, 2].bar(left_coordinates3, heights3, tick_label=bar_labels3,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[0, 2], left_coordinates3, heights3)

    # Metricas de status
    list_of_status = data.get_all(list_loans, Loan.get_status)

    count_paid = 0
    count_not_paid = 0
    for n in list_of_status:
        if n == 1:
            count_paid += 1
        elif n == -1:
            count_not_paid += 1

    left_coordinates4 = [1, 2]
    
    heights4 = [
        count_paid, 
        count_not_paid
    ]
    bar_labels4 = ['Paid', 'Not Paid']

    axs[1, 0].set_title("Loan Status")
    axs[1, 0].bar(left_coordinates4, heights4, tick_label=bar_labels4,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[1, 0], left_coordinates4, heights4)

    # Metricas de Clientes
    list_clients_with_loans = data.get_client_with_loans()

    # ----- Metricas de Idades
    list_of_ages = data.get_all(list_clients_with_loans, Client.get_birth_date_year)

    left_coordinates5 = [1, 2, 3, 4]
    heights5 = [
        round(getAverage(list_of_ages), 2), 
        statistics.mode(list_of_ages), 
        max(list_of_ages), 
        min(list_of_ages)
    ]
    bar_labels5 = ['Media', 'Moda', 'Max', 'Min']

    axs[1, 1].set_title("Client Age")
    axs[1, 1].bar(left_coordinates5, heights5, tick_label=bar_labels5,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[1, 1], left_coordinates5, heights5)

    # ------ Metricas de Gender
    list_of_genders = data.get_all(list_clients_with_loans, Client.get_gender)
    count_men = 0
    count_women = 0
    for n in list_of_genders:
        if n == "Men":
            count_men += 1
        elif n == "Women":
            count_women += 1

    left_coordinates6 = [1, 2]
    heights6 = [count_men, count_women]
    bar_labels6 = ['Men', 'Women']
    
    axs[1, 2].set_title("Client Gender")
    axs[1, 2].bar(left_coordinates6, heights6, tick_label=bar_labels6,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[1, 2], left_coordinates6, heights6)

    # Metricas de transactions
    list_clients_with_transactions = data.get_transactions_with_loans()

    # ----- Metricas de Transaction Types
    list_of_transactions = data.get_all(list_clients_with_transactions, Transaction.get_type)
    count_credit = 0
    count_withdrawal = 0
    count_withdrawal_in_cash = 0
    for n in list_of_transactions:
        if n == TransactionType.Credit:
            count_credit += 1
        elif n == TransactionType.Withdrawal:
            count_withdrawal += 1
        elif n == TransactionType.WithdrawalInCash:
            count_withdrawal_in_cash += 1

    left_coordinates7 = [1, 2, 3]
    heights7 = [count_credit, count_withdrawal, count_withdrawal_in_cash]
    bar_labels7 = ['Credit', 'Withdrawal', 'Withdrawal_in_cash']
    
    axs[2, 0].set_title("Transaction Type")
    axs[2, 0].bar(left_coordinates7, heights7, tick_label=bar_labels7,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[2, 0], left_coordinates7, heights7)

    plt.show()
    plt.close()

def display_more_loan_metrics(data):
    print("Generating Loan Metrics . . .\n")

    list_loans = data.loans
    # fig, axs = plt.subplots(3, 3)
    # fig.suptitle("Loan Metrics")

    # Metricas de ammount
    list_of_ammounts = data.get_all(list_loans, Loan.get_ammount)
    accounts_with_loans = data.get_accounts_with_loans()
    # Metricas de duration
    list_of_durations = data.get_all(list_loans, Loan.get_duration)

    list_clients_with_loans = data.get_client_with_loans()
    
    # list_of_client_ammounts = data.get_all(list_clients_with_loans, Loan.get_ammount)
    list_of_ages = data.get_all(list_clients_with_loans, Client.get_birth_date_year)

    # disposition = data.get_owner_disposition_from_account(accounts_with_loans[i])
        
    # client_of_disposition = data.get_clients_of_disposition(disposition[0])
    # aux = list(zip(list_of_ammounts, list_of_ages))

    ammounts = []
    ages = []

    districts_success = [[0,0]] * len(data.districts)

    for i in range(len(data.loans)):
        owner = data.get_account_owner(data.loans[i].account.id)
        ages.append(owner.get_birth_date_year())
        ammounts.append(data.loans[i].ammount)
        
        id = owner.district.code - 1
        new_pos = 0
        if data.loans[i].status == 1:
            new_pos = districts_success[id][0] + 1
        else:
            new_pos = districts_success[id][0]
        new_total = districts_success[id][1] + 1
        districts_success[id] = [new_pos, new_total]

    print (districts_success)

    
    districts_names = []
    districts_succ = []
    districts_total = []

    for i in range(len(districts_success)):
        #if districts_success[i][1] == 0:
        #    districts_success[i] = 0
        #else:
        #    districts_success[i] = districts_success[i][0]/districts_success[i][1]
        districts_succ.append(districts_success[i][0])
        districts_total.append(districts_success[i][1])
        #districts_names.append(str(data.districts[i].code))
        districts_names.append(str(data.districts[i].code))


    avgs = []
    for i in range(min(ages), max(ages)+1):
        count_total = 0
        count_sum = 0
        for j in range(len(ages)):
            if ages[j] == i:
                count_total += 1
                count_sum += list_of_ammounts[j]
        if count_total == 0:
            avgs.append((i, 0))
        else:
            avgs.append((i ,count_sum/count_total))   


    plt.plot(avgs)
    plt.show()


    X_axis = np.arange(len(districts_names))
  
    plt.bar(X_axis - 0.2, districts_succ, 0.4, label = 'Success')
    plt.bar(X_axis + 0.2, districts_total, 0.4, label = 'Total')
    
    plt.xticks(X_axis, districts_names)
    plt.xlabel("Districts")
    plt.ylabel("Number of Loans")
    plt.title("Status per District")
    plt.legend()
    plt.show()
    return

    left_coordinates2 = [1, 2, 3, 4]
    heights2 = [
        round(getAverage(list_of_durations), 2), 
        statistics.mode(list_of_durations), 
        max(list_of_durations), 
        min(list_of_durations)
    ]
    bar_labels2 = ['Media', 'Moda', 'Max', 'Min']

    axs[0, 1].set_title("Loan Duration")
    axs[0, 1].bar(left_coordinates2, heights2, tick_label=bar_labels2,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[0, 1], left_coordinates2, heights2)

    # Metricas de payments
    list_of_payments = data.get_all(list_loans, Loan.get_payments)

    left_coordinates3 = [1, 2, 3, 4]
    heights3 = [
        round(getAverage(list_of_payments), 2), 
        statistics.mode(list_of_payments), 
        max(list_of_payments), 
        min(list_of_payments)
    ]
    bar_labels3 = ['Media', 'Moda', 'Max', 'Min']

    axs[0, 2].set_title("Loan Payments")
    axs[0, 2].bar(left_coordinates3, heights3, tick_label=bar_labels3,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[0, 2], left_coordinates3, heights3)

    # Metricas de status
    list_of_status = data.get_all(list_loans, Loan.get_status)

    count_paid = 0
    count_not_paid = 0
    for n in list_of_status:
        if n == 1:
            count_paid += 1
        elif n == -1:
            count_not_paid += 1

    left_coordinates4 = [1, 2]
    
    heights4 = [
        count_paid, 
        count_not_paid
    ]
    bar_labels4 = ['Paid', 'Not Paid']

    axs[1, 0].set_title("Loan Status")
    axs[1, 0].bar(left_coordinates4, heights4, tick_label=bar_labels4,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[1, 0], left_coordinates4, heights4)

    # Metricas de Clientes
    list_clients_with_loans = data.get_client_with_loans()

    # ----- Metricas de Idades
    list_of_ages = data.get_all(list_clients_with_loans, Client.get_birth_date_year)

    left_coordinates5 = [1, 2, 3, 4]
    heights5 = [
        round(getAverage(list_of_ages), 2), 
        statistics.mode(list_of_ages), 
        max(list_of_ages), 
        min(list_of_ages)
    ]
    bar_labels5 = ['Media', 'Moda', 'Max', 'Min']

    axs[1, 1].set_title("Client Age")
    axs[1, 1].bar(left_coordinates5, heights5, tick_label=bar_labels5,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[1, 1], left_coordinates5, heights5)

    # ------ Metricas de Gender
    list_of_genders = data.get_all(list_clients_with_loans, Client.get_gender)
    count_men = 0
    count_women = 0
    for n in list_of_genders:
        if n == "Men":
            count_men += 1
        elif n == "Women":
            count_women += 1

    left_coordinates6 = [1, 2]
    heights6 = [count_men, count_women]
    bar_labels6 = ['Men', 'Women']
    
    axs[1, 2].set_title("Client Gender")
    axs[1, 2].bar(left_coordinates6, heights6, tick_label=bar_labels6,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[1, 2], left_coordinates6, heights6)

    # Metricas de transactions
    list_clients_with_transactions = data.get_transactions_with_loans()

    # ----- Metricas de Transaction Types
    list_of_transactions = data.get_all(list_clients_with_transactions, Transaction.get_type)
    count_credit = 0
    count_withdrawal = 0
    count_withdrawal_in_cash = 0
    for n in list_of_transactions:
        if n == TransactionType.Credit:
            count_credit += 1
        elif n == TransactionType.Withdrawal:
            count_withdrawal += 1
        elif n == TransactionType.WithdrawalInCash:
            count_withdrawal_in_cash += 1

    left_coordinates7 = [1, 2, 3]
    heights7 = [count_credit, count_withdrawal, count_withdrawal_in_cash]
    bar_labels7 = ['Credit', 'Withdrawal', 'Withdrawal_in_cash']
    
    axs[2, 0].set_title("Transaction Type")
    axs[2, 0].bar(left_coordinates7, heights7, tick_label=bar_labels7,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[2, 0], left_coordinates7, heights7)

    plt.show()
    plt.close()

def load_data():
    data = Bank_Data()
    print("Loading districts . . .\n")
    data.add_districts("data/ficheiros_competicao/district.csv")
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
    # print("Loading train transactions . . .\n")
    # data.add_transactions("data/ficheiros_competicao/trans_train.csv")

    return data


data = load_data()

# display_client_metrics(data)
# display_loan_metrics(data)
display_more_loan_metrics(data)