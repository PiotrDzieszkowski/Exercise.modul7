from faker import Faker
fake  = Faker()
from datetime import time, datetime
current_time = time
date_time = datetime.now()
start_time = ""


def _end_time(func):
    def curr_time():
        result = func()
        end_time = date_time
        return (result + " " + str(end_time))
    return curr_time
        

@_end_time
def contact_card():
    card = f"{fake.first_name()} {fake.last_name()} {fake.company()}"
    return card

for num in range(1001):
    print(contact_card())