from faker import Faker
fake = Faker()
class BusinessCardHolder():   
    def __init__(self,name, surname,company_name,job_position,email_adress):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.job_position = job_position
        self.email_adress = email_adress
        
        self._label_lenght = ""

    def __str__(self):
        return f"{self.name} {self.surname} {self.email_adress}"
    
    @property
    def label_lenght(self):
        self._label_lenght = len(self.name + " " + self.surname)
        return f"Lista znaków: {self._label_lenght}"       

    def contact(self):
        return f"Kontaktuje się z {self.name} {self.surname} {self.job_position} {self.email_adress}"

class BaseContact(BusinessCardHolder):
    def __init__(self, name, surname, private_number, email_adress):
        self.name = name
        self.surname = surname
        self.private_number = private_number
        self.email_adress = email_adress
    
    def contact(self):
        return f"Wybieram numer {self.private_number} i dzwonię do {self.name} {self.surname}"
    @property
    def create_contacts(self):
        card = f"Base Card.{self.label_lenght}"
        return card

class BusinessContact(BaseContact):
    def __init__(self,job_position, company_name, work_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.job_position = job_position
        self.company_name = company_name
        self.work_number = work_number
        
    def contact(self):
        return f"Wybieram numer {self.work_number} i dzwonię do {self.name} {self.surname}"

    @property
    def create_contacts(self):
        card = f"Business Card.{self.label_lenght}"
        return card

contact_card = BusinessContact(name = fake.first_name(), surname = fake.last_name(), private_number = fake.country_calling_code() + " " + fake.phone_number(),email_adress = fake.company_email(), job_position = fake.job(),company_name = fake.company(),work_number = fake.country_calling_code() + " " + fake.phone_number())
print(contact_card.contact())
print(contact_card.create_contacts)
print(contact_card.__str__())

contact_card = BaseContact(name = fake.first_name(), surname = fake.last_name(), private_number = fake.country_calling_code() + " " + fake.phone_number(),email_adress = fake.company_email())
print(contact_card.contact())
print(contact_card.create_contacts)