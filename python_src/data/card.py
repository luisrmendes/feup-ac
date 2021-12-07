import types
from data.enum_types import CardType
from data.date import Date
from data.disposition import Disposition

class Card:
    def __init__(self, id = 0, type = "classic", issued = Date()):
        self.id = int(id)
        if type == "classic":
            self.type = CardType.Classic
        elif type == "junior":
            self.type = CardType.Junior
        elif type == "gold":
            self.type = CardType.Gold
        else:
            print(str(type) + " error")
        self.issued = Date()
        self.issued.set_from_YYMMDD(int(issued))
        self.disposition = Disposition()

    def add_disposition(self, dispoisition):
        self.disposition = dispoisition

    def get_issue_date(self):
        return self.issued

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def print(self):
        print(str(self.id) + " | " + str(self.disposition.id) + " | " + self.type.to_str() + " | " + self.issued.to_str())