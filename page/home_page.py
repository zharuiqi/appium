from selenium.webdriver.common.by import By
from base.base_action import BaseAvtion


class HomePage(BaseAvtion):

    # 点击我的按钮
    click_my_button = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout[1]/android.widget.TabWidget/android.widget.ImageView[2]'

    def home_page_click_my_button(self):
        self.base_click(self.click_my_button)
