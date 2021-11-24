class District:
    def __init__(self, code = 0, name = "", region = "", n_inhab = 0, n_mun_inhab_0_499 = 0, n_mun_inhab_500_1999 = 0, n_mun_inhab_2000_9999 = 0, n_mun_inhab_10000_inf = 0, n_cities = 0, ratio_urban_inhab = 0, average_salary = 0, unemploymant_95 = 0, unemploymant_96 = 0, n_enterp_per_1000 = 0, n_crimes_95 = 0, n_crimes_96 = 0):
        self.code = int(code)
        self.name = name
        self.region = region

        if n_inhab != "?":
            self.n_inhab = int(n_inhab)
        else: 
            self.n_inhab = -1
        
        if n_mun_inhab_0_499 != "?":
            self.n_mun_inhab_0_499 = int(n_mun_inhab_0_499)
        else:
            self.n_mun_inhab_0_499 = -1

        if n_mun_inhab_500_1999 != "?":
            self.n_mun_inhab_500_1999 = int(n_mun_inhab_500_1999)
        else:
            self.n_mun_inhab_500_1999 = -1
        
        if n_mun_inhab_2000_9999 != "?":
            self.n_mun_inhab_2000_9999 = int(n_mun_inhab_2000_9999)
        else:
            self.n_mun_inhab_2000_9999 = -1

        if n_mun_inhab_10000_inf != "?":
            self.n_mun_inhab_10000_inf = int(n_mun_inhab_10000_inf)
        else:
            self.n_mun_inhab_10000_inf = -1

        if n_cities != "?":
            self.n_cities = int(n_cities)
        else:
            self.n_cities = -1

        if ratio_urban_inhab != "?":
            self.ratio_urban_inhab = float(ratio_urban_inhab)
        else:
            self.ratio_urban_inhab = -1

        if average_salary != "?":
            self.average_salary = int(average_salary)
        else:
            self.average_salary = -1

        if unemploymant_95 != "?":
            self.unemploymant_95 = float(unemploymant_95)
        else:
            self.unemploymant_95 = -1

        if unemploymant_96 != "?":
            self.unemploymant_96 = float(unemploymant_96)
        else:
            self.unemploymant_96 = -1

        if n_enterp_per_1000 != "?":
            self.n_enterp_per_1000 = int(n_enterp_per_1000)
        else:
            self.n_enterp_per_1000 = -1

        if n_crimes_95 != "?":
            self.n_crimes_95 = int(n_crimes_95)
        else:
            self.n_crimes_95 = -1

        if n_crimes_96 != "?":
            self.n_crimes_96 = int(n_crimes_96)
        else:
            self.n_crimes_96 = -1

    def get_id(self):
        return self.code

    def get_n_inhab(self):
        return self.n_inhab
    
    def get_average_salary(self):
        return self.average_salary

    def print(self):
        print(str(self.code) + " | " + self.name + " | " + self.region + " | " + str(self.n_inhab) + " | " + str(self.n_mun_inhab_0_499) + " | "  + str(self.n_mun_inhab_500_1999) + " | "  + str(self.n_mun_inhab_2000_9999) + " | "  + str(self.n_mun_inhab_10000_inf)  + " | " + str(self.n_cities)  + " | "  + str(self.ratio_urban_inhab)  + " | " + str(self.average_salary)  + " | " + str(self.unemploymant_95) + " | " + str(self.unemploymant_96) + " | "  + str(self.n_enterp_per_1000) + " | " + str(self.n_crimes_95) + " | " + str(self.n_crimes_96))
