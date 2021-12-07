from data.enum_types import Ownership
from data.client import Client
from data.account import Account

class Disposition:
    def __init__(self, id = 0, ownership = "OWNER"):
        self.id = int(id)
        if ownership == "OWNER":
            self.ownership = Ownership.Owner
        elif ownership == "DISPONENT":
            self.ownership = Ownership.Disponent
        else:
            print(str(ownership) + " error")
        self.client = Client()
        self.account = Account()
    
    def get_ownership(self):
        return self.ownership

    def add_client(self, client):
        self.client = client

    def add_account(self, account):
        self.account = account

    def get_id(self):
        return self.id

    def print(self):
        print(str(self.id), " | " + str(self.client.id) + " | " + str(self.account.id) + " | " + self.ownership.to_str())