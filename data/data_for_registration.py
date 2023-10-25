from dataclasses import dataclass


class Url:
    URL = '/automation-practice-form'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subject: str
    address: str
    state: str
    city: str


@dataclass
class UserWithHobbyAndGender(User):
    gender: str
    hobby: str


user_information = UserWithHobbyAndGender(
    first_name='Yana',
    last_name='Kormshch',
    email='email@test.com',
    mobile_number='89744584422',
    year_of_birth='1997',
    month_of_birth='January',
    day_of_birth='06',
    subject='English',
    address='Moscow, Smolnaya street, 5',
    state='Uttar Pradesh',
    city='Agra',
    gender='Female',
    hobby='Music'
)
