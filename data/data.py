from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    email: str = None
    subject: list = None
    mobile: str = None
    current_address: str = None
    permanent_address: str = None
    age: int = None
    salary: int = None
    department: str = None
    date_of_birth: str = None
