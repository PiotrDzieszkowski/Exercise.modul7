class Business_card_holder():
   
    
    def __init__(self,name, surname,company_name,job_position,email_adress):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.job_position = job_position
        self.email_adress = email_adress
        
        self.name_and_surname = ""

    def __str__(self):
        return f"{self.name} {self.surname} {self.email_adress}"
    
    @property
    def lenght_name_and_surname(self):
        self.name_and_surname = len(self.name + " " + self.surname)
        return f"Lista znaków: {self.name_and_surname}"
        


    def contact(self):
        return f"{self.name} {self.surname} {self.job_position} {self.email_adress}"
   
contact_1 = Business_card_holder(name = "John",surname = "Paul", company_name = "Nordea",job_position = "IT developer",email_adress= "john.paul@nordea.com")
contact_2 = Business_card_holder(name="Dante",surname="Swenson",company_name="EY",job_position="Senior Business Analyst",email_adress="dante.swenson@e&y.com")
contact_3 = Business_card_holder(name="Paul",surname="Miller",company_name="Infosys",job_position="Senior Manager",email_adress="paul.miller@infosys.com")
contact_4 = Business_card_holder(name="Robert",surname="Baratheon",company_name="Seven Kingdoms",job_position="King",email_adress="rob.baratheon@7kingdoms.com")
contact_5 = Business_card_holder(name="Eddard",surname="Stark",company_name="North",job_position= "Knight",email_adress="ed.stark@7north.com")

contact_list = [contact_1, contact_2, contact_3, contact_4, contact_5]

print(contact_1.contact())
print(contact_1.lenght_name_and_surname)