from data.date import Date
from data.enum_types import TransactionType, Operation, KSymbol
from data.account import Account

class Transaction:
    def __init__(self, id = 0, date = Date(), type = "credit", operation = "credit in cash", amount = 0, balance = 0, k_symbol = "household", bank = "", account = 0):
        self.id = int(id)
        self.date = Date()
        self.date.set_from_YYMMDD(int(date))
        if type == "credit":
            self.type = TransactionType.Credit
        elif type == "withdrawal":
            self.type = TransactionType.Withdrawal
        elif type == "withdrawal in cash":
            self.type = TransactionType.WithdrawalInCash
        else:
            print(str(type) + " error")
        if operation == "":
            self.operation = Operation.NA
        elif operation == "credit in cash":
            self.operation = Operation.CreditInCash
        elif operation == "withdrawal in cash":
            self.operation = Operation.WithdrawalInCash
        elif operation == "credit card withdrawal":
            self.operation = Operation.CreditCardWithdrawal
        elif operation == "remittance to another bank":
            self.operation = Operation.RemittanceToAnotherBank
        elif operation == "collection from another bank":
            self.operation = Operation.CollectionFromAnotherBank
        else:
            print(str(operation) + " error")
        self.amount = float(amount)
        self.balance = float(balance)
        if k_symbol == "" or k_symbol == " ":
            self.k_symbol = KSymbol.NA
        elif k_symbol == "household":
            self.k_symbol = KSymbol.Household
        elif k_symbol == "interest credited":
            self.k_symbol = KSymbol.InterestCredited 
        elif k_symbol == "old-age pension":
            self.k_symbol = KSymbol.OldAgePension 
        elif k_symbol == "insurrance payment":
            self.k_symbol = KSymbol.InsurrancePayment 
        elif k_symbol == "payment for statement":
            self.k_symbol = KSymbol.PaymentForStatement
        elif k_symbol == "sanction interest if negative balance":
            self.k_symbol = KSymbol.SanctionInterestIfNegativeBalance
        else:
            print(str(k_symbol) + " error")
        self.bank = bank
        if account == "":
            self.partner_account = 0
        else:
            self.partner_account = account
        self.account = Account()

    def add_account(self, account):
        self.account = account

    def get_id(self):
        return self.id

    def print(self):
        print(str(self.id) + " | " + str(self.account.id) + " | " + self.date.to_str() + " | " + self.type.to_str() + " | " + self.operation.to_str() + " | " + str(self.amount) + " | " + str(self.balance) + " | " + self.k_symbol.to_str() +" | " + self.bank + " | " + str(self.partner_account))
