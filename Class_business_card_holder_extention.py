class Business_card_holder():
   
    
    def __init__(self,name, surname,company_name,job_position,email_adress):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.job_position = job_position
        self.email_adress = email_adress

    def __str__(self):
        return f"{self.name} {self.surname} {self.email_adress}"
   
contact_1 = Business_card_holder(name = "John",surname = "Paul", company_name = "Nordea",job_position = "IT developer",email_adress= "john.paul@nordea.com")
contact_2 = Business_card_holder(name="Dante",surname="Swenson",company_name="EY",job_position="Senior Business Analyst",email_adress="dante.swenson@e&y.com")
contact_3 = Business_card_holder(name="Paul",surname="Miller",company_name="Infosys",job_position="Senior Manager",email_adress="paul.miller@infosys.com")
contact_4 = Business_card_holder(name="Robert",surname="Baratheon",company_name="Seven Kingdoms",job_position="King",email_adress="rob.baratheon@7kingdoms.com")
contact_5 = Business_card_holder(name="Eddard",surname="Stark",company_name="North",job_position= "Knight",email_adress="ed.stark@7north.com")

contact_list = [contact_1, contact_2, contact_3, contact_4, contact_5]
by_name = sorted(contact_list, key=lambda contact: contact.name)
by_surname = sorted(contact_list, key=lambda contact: contact.surname)
by_email = sorted(contact_list, key=lambda contact: contact.email_adress)
print(by_name[0], by_name[1],by_name[2],by_name[3],by_name[4])
print(by_surname[0], by_surname[1],by_surname[2],by_surname[3],by_surname[4])
print(by_email[0], by_email[1],by_email[2],by_email[3],by_email[4])