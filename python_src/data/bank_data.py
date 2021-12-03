from data.district import District
from data.client import Client
from data.account import Account
from data.disposition import Disposition
from data.loan import Loan
from data.card import Card
from data.transaction import Transaction
from data.enum_types import Order
import operator
import csv

class Bank_Data:
    def __init__(self):
        self.districts = []
        self.clients = []
        self.accounts = []
        self.dispositions = []
        self.loans = []
        self.cards = []
        self.transactions = []

    def get_transactions_with_loans(self):
        returnList = []
        for loan in self.loans:
            for transactions in self.transactions:
                if loan.account == transactions.account:
                    returnList.append(transactions)
                                
        return returnList

    def get_client_with_loans(self):
        returnList = []
        for loan in self.loans:
            for disposition in self.dispositions:
                if loan.account == disposition.account:
                    returnList.append(disposition.client)
                                
        return returnList

    def get_client_from_disposition(self, disposition):
        returnList = []
        for client in self.clients:
            if (disposition.client == client):
                returnList.insert(client)
        
        return returnList


    def add_districts(self, file):
        with open(file, newline='') as csvfile:
            districts = list(csv.reader(csvfile, delimiter=';'))
            
        districts.pop(0)

        for district in districts:
            self.districts.append(District(district[0], district[1], district[2], district[3], district[4], district[5], district[6], district[7], district[8], district[9], district[10], district[11], district[12], district[13], district[14], district[15]))

    def add_clients(self, file):
        with open(file, newline='') as csvfile:
            clients = list(csv.reader(csvfile, delimiter=';'))
            
        clients.pop(0)

        for client in clients:
            cli = Client(client[0], client[1])
            cli.add_district(self.get_by_id(self.districts,int(client[2])))
            self.clients.append(cli)

    def add_accounts(self, file):
        with open(file, newline='') as csvfile:
            accounts = list(csv.reader(csvfile, delimiter=';'))
            
        accounts.pop(0)

        for account in accounts:
            acc = Account(account[0], account[2], account[3])
            acc.add_district(self.get_by_id(self.districts, int(account[1])))
            self.accounts.append(acc)

        self.accounts = self.quicksort(self.accounts, Account.get_id, Order.Decreasing)
    
    def add_dispositions(self, file):
        with open(file, newline='') as csvfile:
            dispositions = list(csv.reader(csvfile, delimiter=';'))
            
        dispositions.pop(0)

        for disposition in dispositions:
            dis = Disposition(disposition[0], disposition[3])
            dis.add_client(self.get_by_id(self.clients, int(disposition[1])))
            dis.add_account(self.get_by_id(self.accounts, int(disposition[2])))
            self.dispositions.append(dis)

    def add_loans(self, file):
        with open(file, newline='') as csvfile:
            loans = list(csv.reader(csvfile, delimiter=';'))
            
        loans.pop(0)

        for loan in loans:
            lo = Loan(loan[0], loan[2], loan[3], loan[4], loan[5], loan[6])
            lo.add_account(self.get_by_id(self.accounts, int(loan[1])))
            self.loans.append(lo)
    
    def add_cards(self, file):
        with open(file, newline='') as csvfile:
            cards = list(csv.reader(csvfile, delimiter=';'))
            
        cards.pop(0)

        for card in cards:
            ca = Card(card[0], card[2], card[3])
            ca.add_disposition(self.get_by_id(self.dispositions, int(card[1])))
            self.cards.append(ca)

    def add_transactions(self, file):
        with open(file, newline='') as csvfile:
            transactions = list(csv.reader(csvfile, delimiter=';'))

        transactions.pop(0)
        
        i = 0
        for transaction in transactions:
            trans = Transaction(transaction[0], transaction[2], transaction[3], transaction[4], transaction[5], transaction[6], transaction[7], transaction[8], transaction[9])
            trans.add_account(self.get_by_id(self.accounts, int(transaction[1])))
            self.transactions.append(trans)
            i = i+1
            if (i%10000 == 0):print(i)

    def get_by_id(self,list,id):
        if id < len(list):
            start_id = id - 1
            finish_id = -1
            for x in range(start_id, finish_id, -1):
                if list[x].get_id() == id:
                    return list[x]
            start_id = len(list) - 1
            finish_id = id - 1
            for x in range(start_id, finish_id, -1):
                if list[x].get_id() == id:
                    return list[x]
            print (id)
            list[id-1].print()
        else:
            for x in range(0, len(list)):
                if list[x].get_id() == id:
                    return list[x]

    def quicksort(self, list, get, order):
        if len(list) == 0 or len(list) == 1:
            return list
        else:
            smaller = []
            bigger = []
            pivot = list.pop(0)
            for x in range(0,len(list)):
                if (get(list[x]) > get(pivot)):
                    bigger.append(list[x])
                else:
                    smaller.append(list[x])
            if order == Order.Growing:
                return self.quicksort(smaller, get, order) + [pivot] + self.quicksort(bigger, get, order)
            else:
                return self.quicksort(bigger, get, order) + [pivot] + self.quicksort(smaller, get, order)

    def filter(self, list, get, op, comp):
        if op == "==": operation = operator.eq
        elif op == "!=": operation = operator.ne
        elif op == "<": operation = operator.lt
        elif op == "<=": operation = operator.le
        elif op == ">": operation = operator.gt
        elif op == ">=": operation = operator.ge
        ret = []
        for member in list:
            if operation(get(member), comp):
                ret.append(member)
        return ret        

    def get_all(self, list, get):
        result = []
        for element in list:
            result.append(get(element))
        return result

    def print(self):
        #for district in self.districts:
        #    district.print()
        #for client in self.clients:
        #    client.print()
        #for account in self.accounts:
        #    account.print()
        #for disposition in self.dispositions:
        #    disposition.print()
        #for loan in self.loans:
        #    loan.print()
        #for card in self.cards:
        #    card.print()
        for transaction in self.transactions:
            transaction.print()
        pass