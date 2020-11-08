from selenium.webdriver.support.wait import WebDriverWait


class BaseAvtion:

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_find_elements(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.send_keys(value)


