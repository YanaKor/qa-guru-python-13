class RegistrationPageLocators:
    ADS_ON_PAGE = '[id^=google_ads][id$=container__]'
    FIRST_NAME = '//input[@id="firstName"]'
    LAST_NAME = '//input[@id="lastName"]'

    EMAIL = '//input[@id="userEmail"]'

    GENDER_LOCATOR = '//label[@for="gender-radio-2"]'

    MOBILE_NUMBER = '//input[@id="userNumber"]'

    DATE_OF_BIRTH_CALENDAR = '//input[@id="dateOfBirthInput"]'
    MONTH_OF_BIRTH = '//select[@class="react-datepicker__month-select"]'
    YEAR_OF_BIRTH = '//select[@class="react-datepicker__year-select"]'
    DAY_OF_BIRTH = '//div[@class="react-datepicker__day react-datepicker__day--0*"]'

    SUBJECT = '//input[@id="subjectsInput"]'

    HOBBIES_MUSIC = '//label[@for="hobbies-checkbox-3"]'

    ADDRESS = '//textarea[@id="currentAddress"]'

    STATE = '//input[@id="react-select-3-input"]'
    CITY = '//input[@id="react-select-4-input"]'

    SUBMIT_BUTTON = '//button[@id="submit"]'

    SUBMITTING_FORM_TEXT = '//div[@id="example-modal-sizes-title-lg"]'
    SUBMITTING_USER_INFO = '.table-responsive .table td:nth-child(2)'
