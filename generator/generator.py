import random
import os
from data.data import Person
from faker import Faker
#faker_en = Faker("En")
fake = Faker("ru_Ru")
subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
     "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]

def generated_person():
    return Person(
        first_name=fake.first_name_male(),
        last_name=fake.last_name_male(),
        middle_name=fake.middle_name_male(),
        email=fake.email(),
        mobile=''.join(str(random.randint(0, 9)) for _ in range(10)),
        subject=random.sample(subjects, random.randint(0, 3)),
        current_address=fake.address(),
        permanent_address=fake.address(),
        age=random.randint(18, 80),
        salary=random.randint(15000, 250000),
        department=fake.company(),
        date_of_birth="11 Oct 1991"
    )


def generated_file():
    #path = rf'C:\Users\home\PycharmProjects\4-Page-Object-Model-Pattern\test{random.randint(10,100)}.txt'
    server_folder_path = os.getcwd()
    path = os.path.join(server_folder_path, f'test{random.randint(10,100)}.txt')
    file = open(path, 'w')
    file.write(f'Helloworld{random.randint(10,50)}')
    file.close()
    return file.name, path