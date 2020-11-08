from page.login_page import MyPage
from page.home_page import HomePage


class Page:

    def __init__(self, driver):
        self.drver = driver

    @property
    def home(self):
        return HomePage(self.drver)

    @property
    def my(self):
        return MyPage(self.drver)
