from data.enum_types import Gender

class Date:

    def __init__(self, day = 1, month =1 , year= 95):
        self.day = day
        self.month = month
        self.year = year
        self.yymmdd = self.year * 10000 + self.month * 100 + self.day

    def set_from_YYMMDD(self, yymmdd):
        self.year = yymmdd//10000
        self.month = (yymmdd%10000)//100
        self.day = yymmdd%100
        self.yymmdd = yymmdd

    def set_from_YYMM50DD(self, yymm50dd):
        self.year = yymm50dd//10000
        self.month = (yymm50dd%10000)//100
        gender = Gender.Men
        if self.month > 30:
            self.month -= 50
            gender = Gender.Women
        self.day = yymm50dd%100
        self.yymmdd = self.year * 10000 + self.month * 100 + self.day
        return gender

    def to_str(self):
        return str(self.day) + '/' + str(self.month) + '/' + str(self.year)