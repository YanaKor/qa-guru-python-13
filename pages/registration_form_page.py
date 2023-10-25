import allure
from selene import browser, be, have, command

from data.data_for_registration import Url
from pages.locators import RegistrationPageLocators as locators


class RegistrationFormPage:
    table_submitting_locator = '//div[@class="table-responsive"]//tbody'

    def __init__(self):
        self.browser = browser

    @allure.step('Open practice form page')
    def open_form(self):
        self.browser.open(Url.URL)
        browser.all(locators.ADS_ON_PAGE).with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all(locators.ADS_ON_PAGE).perform(command.js.remove)

    @allure.step('Fill first name field')
    def fill_first_name(self, name: str):
        self.browser.element(locators.FIRST_NAME).should(be.blank).type(name)

    @allure.step('Fill last name field')
    def fill_last_name(self, surname: str):
        self.browser.element(locators.LAST_NAME).should(be.blank).type(surname)

    @allure.step('Fill email field')
    def fill_email(self, email: str):
        self.browser.element(locators.EMAIL).should(be.blank).type(email)

    @allure.step('Select gender')
    def select_gender_button(self):
        self.browser.element(locators.GENDER_LOCATOR).click()

    @allure.step('Fill mobile number field')
    def fill_mobile_number(self, mobile_number: str):
        self.browser.element(locators.MOBILE_NUMBER).should(be.blank).type(mobile_number)

    @allure.step('Open calendar')
    def open_birthday_calendar(self):
        self.browser.element(locators.DATE_OF_BIRTH_CALENDAR).click()

    @allure.step('Choose year of birth')
    def fill_year_of_birth(self, year: str):
        self.browser.element(locators.YEAR_OF_BIRTH).type(year).click()

    @allure.step('Choose month of birth')
    def fill_month_of_birth(self, month: str):
        self.browser.element(locators.MONTH_OF_BIRTH).type(month).click()

    @allure.step('Choose day of birth')
    def fill_day_of_birth(self, day: str):
        self.browser.element(locators.DAY_OF_BIRTH.replace('*', day)).click()

    @allure.step('Fill subject field')
    def fill_subject_field(self, subject: str):
        self.browser.element(locators.SUBJECT).should(be.blank).type(subject).press_enter()

    @allure.step('Choose hobby')
    def select_hobbies(self):
        self.browser.element(locators.HOBBIES_MUSIC).click()

    @allure.step('Fill address field')
    def fill_address(self, address: str):
        self.browser.element(locators.ADDRESS).should(be.blank).type(address)

    @allure.step('Choose state')
    def select_state(self, state):
        self.browser.element(locators.STATE).type(state).press_enter()

    @allure.step('Choose city')
    def select_city(self, city):
        self.browser.element(locators.CITY).type(city).press_enter()

    @allure.step('Click on submitting button')
    def submit_the_form(self):
        self.browser.element(locators.SUBMIT_BUTTON).should(be.visible).click()

    @allure.step('Check registered information')
    def check_registered_user_info(self):
        self.browser.element(locators.SUBMITTING_FORM_TEXT).should(have.exact_text(
            'Thanks for submitting the form'))
