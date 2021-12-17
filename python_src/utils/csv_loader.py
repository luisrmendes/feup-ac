import csv
import numpy as np

from os import name
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


def populate_csv(data, filename):

    print("Generating data . . .\n")

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


    # TRANSACTIONS: transactions per account -> loan.account_id=acount.account_id
    transactions_number_per_account = []
    last_transaction_date_per_account = []
    transactions_last_balance_per_account = []
    no_transactions_type_credit_per_account = []
    no_transactions_type_withdrawal_per_account = []

    avg_amount_of_transaction_credit_per_account = []
    median_amount_of_transaction_credit_per_account = []
    max_amount_of_transaction_credit_per_account = []
    min_amount_of_transaction_credit_per_account = []
    variance_amount_of_transaction_credit_per_account = []

    avg_amount_of_transaction_withdrawal_per_account = []
    median_amount_of_transaction_withdrawal_per_account = []
    max_amount_of_transaction_withdrawal_per_account = []
    min_amount_of_transaction_withdrawal_per_account = []
    variance_amount_of_transaction_withdrawal_per_account = []

    covariance_amount_of_transaction_credit_and_withdrawal_per_account = []

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
        
        last_transaction = account_transactions[0]
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
        no_transactions_type_withdrawal_per_account.append(len(ammounts_withdrawal))
        
        if (len(ammounts_credit) != 0):
            avg_amount_of_transaction_credit_per_account.append(round(statistics.mean(ammounts_credit), 1))
            median_amount_of_transaction_credit_per_account.append(statistics.median(ammounts_credit))
            max_amount_of_transaction_credit_per_account.append(max(ammounts_credit))
            min_amount_of_transaction_credit_per_account.append(min(ammounts_credit))
            variance_amount_of_transaction_credit_per_account.append(round(statistics.pvariance(ammounts_credit), 1))
        else:
            avg_amount_of_transaction_credit_per_account.append(0)
            median_amount_of_transaction_credit_per_account.append(0)
            max_amount_of_transaction_credit_per_account.append(0)
            min_amount_of_transaction_credit_per_account.append(0)
            variance_amount_of_transaction_credit_per_account.append(0)
        
        if (len(ammounts_withdrawal) != 0):
            avg_amount_of_transaction_withdrawal_per_account.append(round(statistics.mean(ammounts_withdrawal), 1))
            median_amount_of_transaction_withdrawal_per_account.append(statistics.median(ammounts_withdrawal))
            max_amount_of_transaction_withdrawal_per_account.append(max(ammounts_withdrawal))
            min_amount_of_transaction_withdrawal_per_account.append(min(ammounts_withdrawal))
            variance_amount_of_transaction_withdrawal_per_account.append(round(statistics.pvariance(ammounts_withdrawal), 1))
        else:
            avg_amount_of_transaction_withdrawal_per_account.append(0)
            median_amount_of_transaction_withdrawal_per_account.append(0)
            max_amount_of_transaction_withdrawal_per_account.append(0)
            min_amount_of_transaction_withdrawal_per_account.append(0)
            variance_amount_of_transaction_withdrawal_per_account.append(0)

        # if (len(ammounts_credit) and len(ammounts_withdrawal)) != 0:
        #     covariance_amount_of_transaction_credit_and_withdrawal_per_account.append(
        #         np.cov(
        #             np.array(ammounts_credit), 
        #             np.array(ammounts_withdrawal)
        #             )
        #         )[0][1]

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


    # CLIENTS loan.account_id=disposition.account_id  disposition.client_id=client.client_id
    owner_gender_per_account = []
    owner_birth_year_per_account = []
    # client_no_credit_cards_per_account = []
    client_credit_card_type_per_account = []
    client_credit_card_issue_date_per_account = []

    owner_district_name_per_account = []
    owner_region_per_account = []
    owner_district_n_inhab_per_account = []
    owner_district_n_mun_inhab_0_499_per_account = []
    owner_district_n_mun_inhab_500_1999_per_account = []
    owner_district_n_mun_inhab_2000_9999_per_account = []
    owner_district_n_mun_inhab_10000_inf_per_account = []
    owner_district_n_cities_per_account = []
    owner_district_ratio_urban_inhab_per_account = []
    owner_district_average_salary_per_account = []
    owner_district_unemploymant_95_per_account = []
    owner_district_unemploymant_96_per_account = []
    owner_district_n_enterp_per_1000_per_account = []
    owner_district_n_crimes_95_per_account = []
    owner_district_n_crimes_96_per_account = []

    for i in range(len(accounts)):
        disposition = data.get_owner_disposition_from_account(accounts[i])
        
        owner_of_disposition = data.get_clients_of_disposition(disposition[0])
        if owner_of_disposition[0].get_gender() == "Men":
            owner_gender_per_account.append(0)
        else:
            owner_gender_per_account.append(1)
        owner_birth_year_per_account.append(owner_of_disposition[0].get_birth_date_year())
        
        credit_cards_of_disposition = data.get_credit_cards_of_disposition(disposition[0])
        
        if (len(credit_cards_of_disposition) != 0):
            client_credit_card_type_per_account.append(credit_cards_of_disposition[0].get_type())
            client_credit_card_issue_date_per_account.append(credit_cards_of_disposition[0].get_issue_date().get_yymmdd())
        else:
            client_credit_card_type_per_account.append(0)
            client_credit_card_issue_date_per_account.append(0)


        demographics = data.get_demograph_from_client(owner_of_disposition[0])

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

        # all_districts = data.get_districts()
        owner_district_name_per_account.append(demographics[0].get_name())
        owner_region_per_account.append(demographics[0].get_region())
        owner_district_n_inhab_per_account.append(demographics[0].get_n_inhab())
        owner_district_n_mun_inhab_0_499_per_account.append(demographics[0].get_n_mun_inhab_0_499())
        owner_district_n_mun_inhab_500_1999_per_account.append(demographics[0].get_n_mun_inhab_500_1999())
        owner_district_n_mun_inhab_2000_9999_per_account.append(demographics[0].get_n_mun_inhab_2000_9999())
        owner_district_n_mun_inhab_10000_inf_per_account.append(demographics[0].get_n_mun_inhab_10000_inf())
        owner_district_n_cities_per_account.append(demographics[0].get_n_cities())
        owner_district_ratio_urban_inhab_per_account.append(demographics[0].get_ratio_urban_inhab())
        owner_district_average_salary_per_account.append(demographics[0].get_average_salary())
        owner_district_unemploymant_95_per_account.append(demographics[0].get_unemploymant_95())
        owner_district_unemploymant_96_per_account.append(demographics[0].get_unemploymant_96())
        owner_district_n_enterp_per_1000_per_account.append(demographics[0].get_n_enterp_per_1000())
        owner_district_n_crimes_95_per_account.append(demographics[0].get_n_crimes_95())
        owner_district_n_crimes_96_per_account.append(demographics[0].get_n_crimes_96())
  
    print("Creating CSV . . .\n")

    f = open(filename, 'a')
    writer = csv.writer(f)

    labels = []
    labels.append('loan_id')
    labels.append('loan_dates_year')
    labels.append('loan_ammounts')
    labels.append('loan_durations')
    labels.append('loan_payments')
    labels.append('loan_status')
    labels.append('account_dates_yymd')
    labels.append('transactions_number_per_account')
    labels.append('last_transaction_date_per_account')
    labels.append('transactions_last_balance_per_account')
    labels.append('no_transactions_type_credit_per_account')
    labels.append('no_transactions_type_withdrawal_per_account')
    labels.append('avg_amount_of_transaction_credit_per_account')
    labels.append('median_amount_of_transaction_credit_per_account')
    labels.append('max_amount_of_transaction_credit_per_account')
    labels.append('min_amount_of_transaction_credit_per_account')
    labels.append('variance_amount_of_transaction_credit_per_account')
    labels.append('avg_amount_of_transaction_withdrawal_per_account')
    labels.append('median_amount_of_transaction_withdrawal_per_account')
    labels.append('max_amount_of_transaction_withdrawal_per_account')
    labels.append('min_amount_of_transaction_withdrawal_per_account')
    labels.append('variance_amount_of_transaction_withdrawal_per_account')

    labels.append('no_k_na_of_transaction_per_account')
    labels.append('no_k_household_of_transaction_per_account')
    labels.append('no_k_interest_credited_of_transaction_per_account')
    labels.append('no_k_old_age_pension_of_transaction_per_account')
    labels.append('no_k_insurrance_payment_of_transaction_per_account')
    labels.append('no_k_payment_for_statement_of_transaction_per_account')
    labels.append('no_k_sanction_interest_if_negative_balance_of_transaction_per_account')

    labels.append('owner_gender_per_account')
    labels.append('owner_birth_year_per_account')
    labels.append('owner_district_n_inhab_per_account')
    labels.append('owner_district_n_mun_inhab_0_499_per_account')
    labels.append('owner_district_n_mun_inhab_500_1999_per_account')
    labels.append('owner_district_n_mun_inhab_2000_9999_per_account')
    labels.append('owner_district_n_mun_inhab_10000_inf_per_account')
    labels.append('owner_district_n_cities_per_account')
    labels.append('owner_district_ratio_urban_inhab_per_account')
    labels.append('owner_district_average_salary_per_account')
    labels.append('owner_district_unemploymant_95_per_account')
    labels.append('owner_district_unemploymant_96_per_account')
    labels.append('owner_district_n_enterp_per_1000_per_account')
    labels.append('owner_district_n_crimes_95_per_account')
    labels.append('owner_district_n_crimes_96_per_account')

    writer.writerow(labels)

    for i in range(len(loans)):
        row = []

        row.append(loan_ids[i])
        row.append(loan_dates[i].get_year())
        row.append(loan_ammounts[i])
        row.append(loan_durations[i])
        row.append(loan_payments[i])
        row.append(loan_status[i])

        # row.append(account_ids[i])  # ?
        row.append(account_dates[i].get_yymmdd())
        # row.append(account_frequency[i].value)
        
        row.append(transactions_number_per_account[i])
        row.append(last_transaction_date_per_account[i])
        row.append(transactions_last_balance_per_account[i])
        row.append(no_transactions_type_credit_per_account[i])
        row.append(no_transactions_type_withdrawal_per_account[i])

        row.append(avg_amount_of_transaction_credit_per_account[i])
        row.append(median_amount_of_transaction_credit_per_account[i])
        row.append(max_amount_of_transaction_credit_per_account[i])
        row.append(min_amount_of_transaction_credit_per_account[i])
        row.append(variance_amount_of_transaction_credit_per_account[i])

        row.append(avg_amount_of_transaction_withdrawal_per_account[i])
        row.append(median_amount_of_transaction_withdrawal_per_account[i])
        row.append(max_amount_of_transaction_withdrawal_per_account[i])
        row.append(min_amount_of_transaction_withdrawal_per_account[i])
        row.append(variance_amount_of_transaction_withdrawal_per_account[i])

        # row.append(covariance_amount_of_transaction_credit_and_withdrawal_per_account[i])

        row.append(no_k_na_of_transaction_per_account[i])
        row.append(no_k_household_of_transaction_per_account[i])
        row.append(no_k_interest_credited_of_transaction_per_account[i])
        row.append(no_k_old_age_pension_of_transaction_per_account[i])
        row.append(no_k_insurrance_payment_of_transaction_per_account[i])
        row.append(no_k_payment_for_statement_of_transaction_per_account[i])
        row.append(no_k_sanction_interest_if_negative_balance_of_transaction_per_account[i])
        
        row.append(owner_gender_per_account[i])
        row.append(owner_birth_year_per_account[i])
        # row.append(owner_district_name_per_account[i])
        # row.append(owner_region_per_account[i])
        row.append(owner_district_n_inhab_per_account[i])
        row.append(owner_district_n_mun_inhab_0_499_per_account[i])
        row.append(owner_district_n_mun_inhab_500_1999_per_account[i])
        row.append(owner_district_n_mun_inhab_2000_9999_per_account[i])
        row.append(owner_district_n_mun_inhab_10000_inf_per_account[i])
        row.append(owner_district_n_cities_per_account[i])
        row.append(owner_district_ratio_urban_inhab_per_account[i])
        row.append(owner_district_average_salary_per_account[i])
        row.append(owner_district_unemploymant_95_per_account[i])
        row.append(owner_district_unemploymant_96_per_account[i])
        row.append(owner_district_n_enterp_per_1000_per_account[i])
        row.append(owner_district_n_crimes_95_per_account[i])
        row.append(owner_district_n_crimes_96_per_account[i])
        
        writer.writerow(row)
