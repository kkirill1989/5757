import logging

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """Класс, содержащий необходимые методы для работы с webdriver"""

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'

    def find_element(self, locator, time=10):
        """Метод, осуществляющий поиск одного элемента и возвращающий его"""
        try:
            element = WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except TimeoutException:
            logging.exception('Find element exception:')
            element = None
        return element

    def get_element_property(self, locator, el_property):
        """Метод, возвращающий свойство одного элемента"""
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(el_property)
        logging.exception(f'Property {el_property} not found in element with locator {locator}')
        return None

    def go_to_site(self):
        """Переход на указанную страницу"""
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open the site')
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception with alert')
            return None