import csv
from data.bank_data import Bank_Data
from data.district import District
from data.enum_types import Order
from data.client import Client
from data.loan import Loan
from data.transaction import Transaction
from data.account import Account


def populate_csv(data):
    f = open('dataMining.csv', 'a')

    # create the csv writer
    writer = csv.writer(f)

    # LOANS
    loans = data.loans
    loan_ids = data.get_all(loans, Loan.get_id)
    loan_dates = data.get_all(loans, Loan.get_date)
    loan_ammounts = data.get_all(loans, Loan.get_ammount)
    loan_durations = data.get_all(loans, Loan.get_duration)
    loan_payments= data.get_all(loans, Loan.get_payments)
    loan_status= data.get_all(loans, Loan.get_status)


    # ACCOUNTS
    accounts = data.get_accounts_with_loans()
    account_ids = data.get_all(accounts, Account.get_id)
    account_dates = data.get_all(accounts, Account.get_date)
    account_ammounts = data.get_all(accounts, Account.get_frequency)
    account_dates = data.get_all(accounts, Account.get_date)
    account_dates = data.get_all(accounts, Account.get_date)
    account_dates = data.get_all(accounts, Account.get_date)

    print(account_ids)

    # TRANSACTIONS loan.account_id=acount.account_id
    transactions = data.get_transactions_with_accounts(accounts)

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

    # # CLIENTS loan.account_id=disposition.account_id  disposition.client_id=client.client_id
    # no_clients

    # # disposition.type == "Owner"
    # owner_birth_number

    # # CREDIT CARDS loan.account_id=disposition.account_id disposition.type=="Owner"
    # no_credit_cards
    # credit_card_type 
    # credit_card_issued_date

    # # DEMOGRAPHIC DATA loan.account_id=account.account_id account.district_id=demograph.district_id
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
