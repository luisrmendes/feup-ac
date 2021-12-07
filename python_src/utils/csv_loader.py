import csv
from data.bank_data import Bank_Data
from data.district import District
from data.enum_types import Order
from data.client import Client
from data.loan import Loan
from data.transaction import Transaction
from data.account import Account
from data.disposition import Disposition
from data.card import Card
from data.enum_types import CardType




def populate_csv(data):
    f = open('dataMining.csv', 'a')

    # create the csv writer
    writer = csv.writer(f)

    # LOANS
    loans = data.loans
    loan_ids = data.get_all(loans, Loan.get_id)
    # loan_dates = data.get_all(loans, Loan.get_date)
    # loan_ammounts = data.get_all(loans, Loan.get_ammount)
    # loan_durations = data.get_all(loans, Loan.get_duration)
    # loan_payments= data.get_all(loans, Loan.get_payments)
    # loan_status= data.get_all(loans, Loan.get_status)


    # ACCOUNTS
    accounts = data.get_accounts_with_loans()
    account_ids = data.get_all(accounts, Account.get_id)
    account_dates = data.get_all(accounts, Account.get_date)
    account_frequency = data.get_all(accounts, Account.get_frequency)


    # TRANSACTIONS loan.account_id=acount.account_id

    # no_trans
    # last_trans
    # balance
    # no_credit
    # avg_ammount_withdrawal
    # rng_ammount_withdrawal
    # avg_ammount_credit
    # rng_ammount_credit
    # no_k_na
    # no_k_hosehold
    # no_k_old_age_pension
    # no_k_insurrance_payment
    # no_k_payment_for_statment
    # no_k_sanction_interest_if_negative_balance

    transactions = data.get_transactions_from_accounts(accounts)
    transactions_ids = data.get_all(transactions, Transaction.get_id)
    transactions_dates = data.get_all(transactions, Transaction.get_date)
    transactions_balance = data.get_all(transactions, Transaction.get_balance)
    transactions_type = data.get_all(transactions, Transaction.get_type)
    transactions_amount = data.get_all(transactions, Transaction.get_amount)
    transactions_k_symbol = data.get_all(transactions, Transaction.get_k_symbol)


    # CLIENTS loan.account_id=disposition.account_id  disposition.client_id=client.client_id
    dispositions = data.get_dispositions_from_accounts(accounts)
    disposition_ids = data.get_all(dispositions, Disposition.get_id)
    disposition_ownerships = data.get_all(dispositions, Disposition.get_ownership)

    clients = data.get_clients_from_dispositions(dispositions)
    # no_clients
    # client_birth_number
    clients_gender = data.get_all(clients, Client.get_gender)
    clients_birth_date_year = data.get_all(clients, Client.get_birth_date_year)


    # CREDIT CARDS loan.account_id=disposition.account_id disposition.type=="Owner"
    credit_cards = data.get_credit_cards_from_dispositions(dispositions)
    credit_card_ids = data.get_all(credit_cards, Card.get_id)
    # no_credit_cards
    # credit_card_type 
    # credit_card_issued_date
    
    credit_card_types = data.get_all(credit_cards, Card.get_type)
    credit_card_issue_date = data.get_all(credit_cards, Card.get_issue_date)
    

    # DEMOGRAPHIC DATA loan.account_id=account.account_id account.district_id=demograph.district_id
    # loan.account_id -> account.account_id -> disposition.client_id -> client.district_id
    demographics = data.get_clients_from_dispositions(dispositions)

    # district_name
    # region
    # no_Inhabitants
    # no_of_municipalities_with_inhabitants_less_499
    # no_of_municipalities_with_inhabitants_between_500_1999
    # no_of_municipalities_with_inhabitants_between_2000_9999
    # no_of_municipalities_with_inhabitants_greater_10000
    # no_of_cities
    # ratio_of_urban_inhabitants
    # average_salary
    # unemploymant_rate_95
    # unemploymant_rate_96
    # no_of_enterpreneurs_per_1000_inhabitants
    # no_of_commited_crimes_95
    # no_of_commited_crimes_96


    # writer.writerow(list_of_account_ids)

    # write a row to the csv file
