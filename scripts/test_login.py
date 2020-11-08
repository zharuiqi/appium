import time
import allure
import pytest

from base.base_driver import init_driver
from page.page import Page

"""
adb connect 127.0.0.1:21503
adb shell dumpsys window | findstr mCurrentFocus
"""


@allure.feature("智能调度台操作")
class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize(("username", "pwd"), [("15838100454", "qq501924111"), ("123456789", "987654321")])
    def test_login(self, username, pwd):
        # 点击密码登录
        self.page.my.page_click_password_login_button()
        # 输入账号
        self.page.my.page_input_username(username)
        # 输入密码
        self.page.my.page_input_password(pwd)
        # 点击登录按钮
        self.page.my.page_click_login_button()
