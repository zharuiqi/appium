import time

from appium import webdriver
from selenium.webdriver.common.keys import Keys

desired_caps = {
        'automationName': 'UiAutomator1',
        'platformName': 'Android',
        'platformVersion': '7.1',
        'deviceName': 'xiaoyao',
        'appPackage': 'com.suning.mobile.ebuy',
        'appActivity': 'com.suning.mobile.ebuy.host.MainActivity',
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

els = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout[1]/android.widget.TabWidget/android.widget.ImageView[2]')
print(els)
print(driver.page_source)
els.click()
print(driver.page_source)
time.sleep(5)
driver.quit()


