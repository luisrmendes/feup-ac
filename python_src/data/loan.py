from data.date import Date
from data.account import Account

class Loan:
    def __init__(self, id = 0, date = Date(), ammount = 0, duration = 0, payments = 0, status = 0):
        self.id = int(id)
        self.date = Date()
        self.date.set_from_YYMMDD(int(date))
        self.ammount = int(ammount)
        self.duration = int(duration)
        self.payments = int(payments)
        if not isinstance (status,int):
            self.status = 0
        else:
            self.status = int(status)
        self.account = Account()

    def add_account(self, account):
        self.account = account

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

    def get_ammount(self):
        return self.ammount
    
    def get_duration(self):
        return self.duration

    def get_payments(self):
        return self.payments
        
    def get_status(self):
        return self.status

    def print(self):
        print(str(self.id) + " | " + str(self.account.id) + " | " + self.date.to_str() + " | " + str(self.ammount) + " | " + str(self.duration) + " | " + str(self.payments) + " | " + str(self.status))