import allure
from data.data_for_registration import user_information


@allure.description('Successful registration')
@allure.label('owner', 'Yana')
@allure.suite('Registration suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_registration_page(practice_form):
    user = user_information
    practice_form.open_form()

    practice_form.fill_first_name(user.first_name)
    practice_form.fill_last_name(user.last_name)

    practice_form.fill_email(user.email)

    practice_form.select_gender_button()

    practice_form.fill_mobile_number(user.mobile_number)

    practice_form.open_birthday_calendar()
    practice_form.fill_year_of_birth(user.year_of_birth)
    practice_form.fill_month_of_birth(user.month_of_birth)
    practice_form.fill_day_of_birth(user.day_of_birth)

    practice_form.fill_subject_field(user.subject)
    practice_form.select_hobbies()

    practice_form.fill_address(user.address)
    practice_form.select_state(user.state)
    practice_form.select_city(user.city)

    practice_form.submit_the_form()

    practice_form.check_registered_user_info()


