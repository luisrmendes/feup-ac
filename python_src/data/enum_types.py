import enum

class Gender(enum.Enum):
    Men = 1
    Women = 2

    def to_str(self):
        if self == Gender.Men:
            return "Men"
        else:
            return "Women" 

class Frequency(enum.Enum):
    After_Transaction = 1
    Weekly = 2
    Monthly = 3

    def to_str(self):
        if self == Frequency.After_Transaction:
            return "Issuance After Transaction"
        elif self == Frequency.Weekly:
            return "Weekly Issuance"
        else:
            return "Monthly Issuance"

class Ownership(enum.Enum):
    Owner = 1
    Disponent = 2

    def to_str(self):
        if self == Ownership.Owner:
            return "Owner"
        else:
            return "Disponent"


class Order(enum.Enum):
    Growing = 1
    Decreasing = 2

