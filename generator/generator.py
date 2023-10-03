import random

from data.data import Person
from faker import Faker
#faker_en = Faker("En")
fake = Faker("ru_Ru")


def generated_person():
    return Person(
        first_name=fake.first_name_male(),
        last_name=fake.last_name_male(),
        middle_name=fake.middle_name_male(),
        email=fake.email(),
        # mobile=fake.phone_number(),
        mobile='89102345678',
        subject='English',
        current_address=fake.address(),
        permanent_address=fake.address(),
        age=random.randint(18, 80),
        salary=random.randint(15000, 250000),
        department=fake.company()
    )


def generated_file():
    path = rf'C:\Users\home\PycharmProjects\4-Page-Object-Model-Pattern\test{random.randint(10,100)}.txt'
    file = open(path, 'w')
    file.write(f'Helloworld{random.randint(10,50)}')
    file.close()
    return file.name, path