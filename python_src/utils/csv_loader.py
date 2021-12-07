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
from data.enum_types import *
import statistics



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
    loan_payments = data.get_all(loans, Loan.get_payments)
    loan_status = data.get_all(loans, Loan.get_status)


    # ACCOUNTS
    accounts = data.get_accounts_with_loans()
    account_ids = data.get_all(accounts, Account.get_id)
    account_dates = data.get_all(accounts, Account.get_date)
    account_frequency = data.get_all(accounts, Account.get_frequency)


    # TRANSACTIONS loan.account_id=acount.account_id

    # Get transactions per account
    transactions_number_per_account = []
    last_transaction_date_per_account = []
    transactions_last_balance_per_account = []
    no_transactions_type_credit_per_account = []
    avg_amount_of_transaction_credit_per_account = []
    max_amount_of_transaction_credit_per_account = []
    min_amount_of_transaction_credit_per_account = []
    avg_amount_of_transaction_withdrawal_per_account = []
    max_amount_of_transaction_withdrawal_per_account = []
    min_amount_of_transaction_withdrawal_per_account = []
    no_k_na_of_transaction_per_account = []
    no_k_household_of_transaction_per_account = []
    no_k_interest_credited_of_transaction_per_account = []
    no_k_old_age_pension_of_transaction_per_account = []
    no_k_insurrance_payment_of_transaction_per_account = []
    no_k_payment_for_statement_of_transaction_per_account = []
    no_k_sanction_interest_if_negative_balance_of_transaction_per_account = []

    for i in range(len(accounts)):
        account_transactions = data.get_transactions_from_account(accounts[i])
        
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

        transactions_number_per_account.append(len(account_transactions))
        
        last_transaction = account_transactions[0];
        for transaction in account_transactions:
            if transaction.get_date().get_yymmdd() > last_transaction.get_date().get_yymmdd():
                last_transaction = transaction
                

        last_transaction_date_per_account.append(last_transaction.get_date().get_yymmdd())
        transactions_last_balance_per_account.append(last_transaction.get_balance())

        ammounts_credit = []
        ammounts_withdrawal = []
        for transaction in account_transactions:
            if transaction.get_type() == TransactionType.Credit:
                ammounts_credit.append(transaction.get_amount())
            else:
                ammounts_withdrawal.append(transaction.get_amount())

        no_transactions_type_credit_per_account.append(len(ammounts_credit))
        
        if (len(ammounts_credit) != 0):
            avg_amount_of_transaction_credit_per_account.append(statistics.mean(ammounts_credit))
            max_amount_of_transaction_credit_per_account.append(max(ammounts_credit))
            min_amount_of_transaction_credit_per_account.append(min(ammounts_credit))
        else:
            avg_amount_of_transaction_credit_per_account.append(0)
            max_amount_of_transaction_credit_per_account.append(0)
            min_amount_of_transaction_credit_per_account.append(0)
        
        if (len(ammounts_withdrawal) != 0):
            avg_amount_of_transaction_withdrawal_per_account.append(statistics.mean(ammounts_withdrawal))
            max_amount_of_transaction_withdrawal_per_account.append(max(ammounts_withdrawal))
            min_amount_of_transaction_withdrawal_per_account.append(min(ammounts_withdrawal))
        else:
            avg_amount_of_transaction_withdrawal_per_account.append(0)
            max_amount_of_transaction_withdrawal_per_account.append(0)
            min_amount_of_transaction_withdrawal_per_account.append(0)

        no_k_na = 0
        no_k_household = 0
        no_k_interest_credited = 0
        no_k_old_age_pension = 0
        no_k_insurrance_payment = 0
        no_k_payment_for_statement = 0
        no_k_sanction_interest_if_negative_balance = 0

        for transaction in account_transactions:
            if transaction.get_k_symbol() == KSymbol.NA:
                no_k_na += 1
            elif transaction.get_k_symbol() == KSymbol.Household:
                no_k_household += 1
            elif transaction.get_k_symbol() == KSymbol.InterestCredited:
                no_k_interest_credited += 1
            elif transaction.get_k_symbol() == KSymbol.OldAgePension:
                no_k_old_age_pension += 1
            elif transaction.get_k_symbol() == KSymbol.InsurrancePayment:
                no_k_insurrance_payment += 1
            elif transaction.get_k_symbol() == KSymbol.PaymentForStatement:
                no_k_payment_for_statement += 1
            elif transaction.get_k_symbol() == KSymbol.SanctionInterestIfNegativeBalance:
                no_k_sanction_interest_if_negative_balance += 1            
            else:
                print("k_symbol not recognized")

        no_k_na_of_transaction_per_account.append(no_k_na)
        no_k_household_of_transaction_per_account.append(no_k_household)
        no_k_interest_credited_of_transaction_per_account.append(no_k_interest_credited)
        no_k_old_age_pension_of_transaction_per_account.append(no_k_old_age_pension)
        no_k_insurrance_payment_of_transaction_per_account.append(no_k_insurrance_payment)
        no_k_payment_for_statement_of_transaction_per_account.append(no_k_payment_for_statement)
        no_k_sanction_interest_if_negative_balance_of_transaction_per_account.append(no_k_sanction_interest_if_negative_balance)


    # transactions = data.get_transactions_from_accounts(accounts)
    # transactions_ids = data.get_all(transactions, Transaction.get_id)
    # transactions_dates = data.get_all(transactions, Transaction.get_date)
    # transactions_balance = data.get_all(transactions, Transaction.get_balance)
    # transactions_type = data.get_all(transactions, Transaction.get_type)
    # transactions_amount = data.get_all(transactions, Transaction.get_amount)
    # transactions_k_symbol = data.get_all(transactions, Transaction.get_k_symbol)


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

    print(len(loan_ids))
    print(len(account_ids))

    for i in range(len(loans)):
        row = []

        row.append(loan_ids[i])
        row.append(loan_dates[i].get_year())
        row.append(loan_ammounts[i])
        row.append(loan_durations[i])
        row.append(loan_payments[i])
        row.append(loan_status[i])

        row.append(account_ids[i])
        row.append(account_dates[i].get_year())
        row.append(account_frequency[i])
        
        row.append(transactions_number_per_account[i])
        row.append(last_transaction_date_per_account[i])
        row.append(transactions_last_balance_per_account[i])
        row.append(no_transactions_type_credit_per_account[i])
        row.append(avg_amount_of_transaction_credit_per_account[i])
        row.append(max_amount_of_transaction_credit_per_account[i])
        row.append(min_amount_of_transaction_credit_per_account[i])
        row.append(avg_amount_of_transaction_withdrawal_per_account[i])
        row.append(max_amount_of_transaction_withdrawal_per_account[i])
        row.append(min_amount_of_transaction_withdrawal_per_account[i])
        row.append(no_k_na_of_transaction_per_account[i])
        row.append(no_k_household_of_transaction_per_account[i])
        row.append(no_k_interest_credited_of_transaction_per_account[i])
        row.append(no_k_old_age_pension_of_transaction_per_account[i])
        row.append(no_k_insurrance_payment_of_transaction_per_account[i])
        row.append(no_k_payment_for_statement_of_transaction_per_account[i])
        row.append(no_k_sanction_interest_if_negative_balance_of_transaction_per_account[i])

        writer.writerow(row)



    # write a row to the csv file
