from faker import Faker
fake = Faker()



class Business_card_holder():
   
    
    def __init__(self,name, address,postcode, phone_number, job):
        self.name = name
        self.address = address
        self.postcode = postcode
        self.phone_number = phone_number
        self.job = job
        
        print(name,address,postcode, phone_number, job)
   

for _ in range(10):
    new_contact = Business_card_holder(fake.name(),fake.address(),fake.postcode(),fake.phone_number(), fake.job())


print(fake.first_name())
print(fake.last_name())