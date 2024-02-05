from selene import browser, be, have, by
import os

def test_fill_form_user_flow():
    browser.open('/')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.execute_script('document.querySelector("footer").remove()')
    browser.element('#firstName').should(be.blank).type('Anna')
    browser.element('#lastName').should(be.blank).type('Danch')
    browser.element('#userEmail').should(be.blank).type('anda@gmail.com')
    browser.element("label[for='gender-radio-2']").click()
    browser.element('#userNumber').type('9321506262')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').s(by.text('October')).click()
    browser.element('.react-datepicker__year-select').s(by.text('1985')).click()
    browser.element("div[aria-label*='21st']").click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element("label[for='hobbies-checkbox-1']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('file/отпуск!.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Somewhere in India')
    browser.element('#state').click()
    browser.all('#state div').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('#city div').element_by(have.exact_text('Delhi')).click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(
        have.texts(
    'Anna Danch',
        'anda@gmail.com',
        'Female',
        '9321506262',
        '21 October,1985',
        'Computer Science',
        'Sports',
        'отпуск!.jpg',
        'Somewhere in India',
        'NCR Delhi'
        )
    )