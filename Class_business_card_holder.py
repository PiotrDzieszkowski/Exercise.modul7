class Business_card_holder():
   
    
    def __init__(self,name, surname,company,job_position,email_adress):
        self.name = name
        self.surname = surname
        self.company = company
        self.job_position = job_position
        self.email_adress = email_adress

        print(name, surname, company, email_adress)
   
contact_list = [["John","Paul","Nordea","IT developer","john.paul@nordea.com"],
["Dante","Swenson","EY","Senior Business Analyst","dante.swenson@e&y.com"],
["Paul","Miller","Infosys","Senior Manager","paul.miller@infosys.com"],
["Robert","Baratheon","Seven Kingdom","King","rob.baratheon@7kingdom.com"],
["Eddard","Stark","North","Knight","ed.stark@7north.com"]
]

for contact in contact_list:
    new_contact = Business_card_holder(contact[0], contact[1], contact[2], contact[3], contact[4])