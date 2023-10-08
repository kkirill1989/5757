import time
import yaml
import logging

from testpage import OperationsHelper

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser_type = testdata['browser']


def test_login_invalid_user(browser):
    """Негативный тест попытки входа на сайт несуществующим пользователем"""
    logging.info('Test 1 is starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()

    test_page.enter_login('test')
    test_page.enter_pass('test')

    test_page.click_login_button()
    assert test_page.get_error_text() == '401', 'Test 1 failed'


def test_valid_login(browser):
    """Позитивный тест входа на сайт"""
    logging.info('Test 2 is starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()

    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])

    test_page.click_login_button()
    assert test_page.get_login_text() == f'Hello, {testdata["login"]}', 'Test 2 failed'


def test_add_post(browser):
    """Позитивный тест добавления поста"""
    logging.info('Test 3 is starting')
    test_page = OperationsHelper(browser)

    time.sleep(testdata['sleep_time'])
    test_page.click_create_post_button()
    time.sleep(testdata['sleep_time'])

    test_page.enter_post_title(testdata['post_title'])
    test_page.enter_post_description(testdata['post_description'])
    test_page.enter_post_content(testdata['post_content'])

    test_page.click_save_post_button()
    time.sleep(testdata['sleep_time'])

    assert test_page.get_post_title() == testdata['post_title'], 'Test 3 failed'


def test_contactus_form(browser):
    """Позитивный тест заполнения формы обратной связи"""
    logging.info('Test 4 is starting')
    test_page = OperationsHelper(browser)

    time.sleep(testdata['sleep_time'])
    test_page.click_contact_us_button()
    time.sleep(testdata['sleep_time'])

    test_page.enter_username_contact_us_form(testdata['username'])
    test_page.enter_email_contact_us_form(testdata['email'])
    test_page.enter_content_contact_us_form(testdata['contact_us_text'])

    test_page.click_send_contact_us_form()
    time.sleep(testdata['sleep_time'])

    assert test_page.get_alert() == 'Form successfully submitted', 'Test 4 failed'