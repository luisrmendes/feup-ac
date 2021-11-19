from data.date import Date
from data.enum_types import Frequency
from data.district import District

class Account:
    def __init__(self, id = 0, frequency = "weekly issuance", date = 950101):
        self.id = int(id)
        if frequency == "issuance after transaction":
            self.frequency = Frequency.After_Transaction
        elif frequency == "weekly issuance":
            self.frequency = Frequency.Weekly
        elif frequency == "monthly issuance":
            self.frequency = Frequency.Monthly
        else:
            print(str(frequency) + " error")
        self.date = Date()
        self.date.set_from_YYMMDD(int(date))
        self.district = District()

    def add_district(self, district):
        self.district = district

    def get_id(self):
        return self.id

    def print(self):
        print(str(self.id) + " | " + self.district.name + " | " + self.frequency.to_str() + " | " + self.date.to_str())