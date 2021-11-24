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

class CardType(enum.Enum):
    Classic = 1
    Junior = 2
    Gold = 3

    def to_str(self):
        if self == CardType.Classic:
            return "Classic"
        elif self == CardType.Junior:
            return "Junior"
        else:
            return "Gold"

class TransactionType(enum.Enum):
    Credit = 1
    Withdrawal = 2
    WithdrawalInCash = 3

    def to_str(self):
        if self == TransactionType.Credit:
            return "Credit"
        elif self == TransactionType.Withdrawal:
            return "Withdrawal"
        else:
            return "Withdrawal in Cash"

class Operation(enum.Enum):
    NA = 1
    CreditInCash = 2
    WithdrawalInCash = 3
    CreditCardWithdrawal = 4
    RemittanceToAnotherBank = 5 
    CollectionFromAnotherBank = 6

    def to_str(self):
        if self == Operation.NA:
            return "NA"
        elif self == Operation.CreditInCash:
            return "Credit in Cash"
        elif self == Operation.WithdrawalInCash:
            return "Withdrawal in Cash"
        elif self == Operation.CreditCardWithdrawal:
            return "Credit Card Withdrawal"
        elif self == Operation.RemittanceToAnotherBank:
            return "Remittance to Another Bank"
        else:
            return "Collection from Another Bank"

class KSymbol(enum.Enum):
    NA = 1
    Household = 2
    InterestCredited = 3
    OldAgePension = 4
    InsurrancePayment = 5
    PaymentForStatement = 6
    SanctionInterestIfNegativeBalance = 7

    def to_str(self):
        if self == KSymbol.NA:
            return "NA"
        elif self == KSymbol.Household:
            return "Household"
        elif self == KSymbol.InterestCredited:
            return "Interest Credited"
        elif self == KSymbol.OldAgePension:
            return "Old-age Pension"
        elif self == KSymbol.InsurrancePayment:
            return "Insurrance Payment"
        elif self == KSymbol.PaymentForStatement:
            return "Payment for Statement"
        elif self == KSymbol.SanctionInterestIfNegativeBalance:
            return "Sanction Interest if Negative Balance"

class Order(enum.Enum):
    Growing = 1
    Decreasing = 2

