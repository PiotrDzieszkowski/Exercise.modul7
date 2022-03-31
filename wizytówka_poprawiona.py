
from string import capwords
from faker import Faker
import random
from datetime import date
today = date.today()


class BaseContact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f'{self.name} {self.email}'

    def __repr__(self):
        return f"BaseContact(make={self.name} phone_number={self.phone_number} mail={self.email})"

    @property
    def contact(self):
        return print(f"I dial the number: {self.phone_number} and contacted: {self.name}")

    @property
    def lenght_count(self):
        return print(len(self.name)+1)

class BusinessContact(BaseContact):
    def __init__(self, company, job, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.company_phone = company_phone

    def __repr__(self):
        return f"BusinessContact(make={self.name}, company={self.company}, company_phone={self.company_phone}, job={self.job}, phone_number={self.phone_number}, mail={self.email})"

    def __str__(self):
        return f"{self.name} {self.email} {self.company} {self.job}"

def create_contacts(card_type, quantity):

    quantity = int(quantity)
    
    contacts =[]
    print('Today Date: {}\n'.format(today.strftime("%d/%m/%Y")))
    if card_type == "P":
        for n in range(quantity):
            fake = Faker()
            contact = BaseContact(name = fake.name(), phone_number=fake.phone_number(), email=fake.email())
            contacts.append(contact)
    if card_type == "B":
        for n in range(quantity):
            fake = Faker()
            contact = BusinessContact(name=fake.name(), company=fake.company(), company_phone=fake.phone_number(), job=fake.job(), phone_number=fake.phone_number(), email=fake.email())
            contacts.append(contact)
    for n in contacts:
        print(n)
    contacts = False

    
   

card_type = input("Which card would you like to choose: Business [B] or Personal [P]? ")    
quantity = input("How many cards you want? " )
create_contacts(card_type, quantity)

if __name__ == "__main__":
    create_contacts()
    print("Chcesz wykonać kolejne działanie? Wpisz literę T lub N")
    contacts = False
    while not contacts:

        contacts = input()
        if contacts == "N":
            contacts = True
        elif contacts != "T":
            print("Niepoprawny wybór")
            break

