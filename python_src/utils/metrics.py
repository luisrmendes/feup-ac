import matplotlib.pyplot as plt
from data.date import Date
from data.client import Client
from data.loan import Loan
from data.transaction import Transaction
from data.enum_types import TransactionType
import statistics


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
    list_clients = data.clients

    fig, axs = plt.subplots(2)

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

    axs[0].set_title("Client Age")
    axs[0].bar(left_coordinates1, heights1, tick_label=bar_labels1,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[0], left_coordinates1, heights1)

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
    
    axs[1].set_title("Client Gender")
    axs[1].bar(left_coordinates2, heights2, tick_label=bar_labels2,
        width=0.6, color=['red', 'black'])

    valuelabel(axs[1], left_coordinates2, heights2)
    
    plt.show()
    plt.close()

def display_loan_metrics(data):
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
        print(n)
        if n == TransactionType.Credit:
            count_credit += 1
        elif n == TransactionType.Withdrawal:
            count_withdrawal += 1
        elif n == TransactionType.WithdrawalInCash:
            count_withdrawal_in_cash += 1

    print(count_credit)
    print(count_withdrawal)
    print(count_withdrawal_in_cash)

    left_coordinates7 = [1, 2, 3]
    heights7 = [count_credit, count_withdrawal, count_withdrawal_in_cash]
    bar_labels7 = ['Credit', 'Withdrawal', 'Withdrawal_in_cash']
    
    axs[2, 0].set_title("Transaction Type")
    axs[2, 0].bar(left_coordinates7, heights7, tick_label=bar_labels7,
        width=0.6, color=['red', 'black'])
    valuelabel(axs[2, 0], left_coordinates7, heights7)

    # print(list_of_transactions)

    plt.show()
    plt.close()