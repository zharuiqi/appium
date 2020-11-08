from selenium.webdriver.common.by import By

from base.base_action import BaseAvtion


class MyPage(BaseAvtion):

    # 点击密码登录按钮
    click_password_login_button = By.XPATH, '//*[@text="密码登录"]'

    # 输入用户名
    input_username = By.ID, 'com.suning.mobile.ebuy:id/account'

    # 输入密码
    input_password = By.ID, 'com.suning.mobile.ebuy:id/password'

    # 点击登录按钮
    click_login_button = By.ID, 'com.suning.mobile.ebuy:id/btn_logon_first'

    def page_click_password_login_button(self):
        self.base_click(self.click_password_login_button)

    def page_input_username(self, username):
        self.base_input(self.input_username, username)

    def page_input_password(self, password):
        self.base_input(self.input_password, password)

    def page_click_login_button(self):
        self.base_click(self.click_login_button)