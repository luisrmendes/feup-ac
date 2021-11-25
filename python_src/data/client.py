from data.district import District
from data.date import Date
from data.enum_types import Gender 

class Client:
    def __init__(self, id = 0, birth_number = 950101):
        self.id = int(id)
        self.birth_date = Date()
        self.gender = Gender.Women
        self.gender = self.birth_date.set_from_YYMM50DD(int(birth_number))
        self.ditrict = District()

    def add_district(self, district):
        self.ditrict = district

    def get_id(self):
        return self.id

    def get_birth_date_yymmdd(self):
        return self.birth_date.get_yymmdd()
    
    def get_birth_date_year(self):
        return self.birth_date.get_year()

    def print(self):
        print(str(self.id) + " | " + self.gender.to_str() + " | " + self.birth_date.to_str() + " | " + self.ditrict.name)