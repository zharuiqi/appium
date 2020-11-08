from appium import webdriver


def init_driver():
    desired_caps = {
        'automationName': 'UiAutomator1',
        'platformName': 'Android',
        'platformVersion': '7.1',
        'deviceName': 'xiaoyao',
        'appPackage': 'com.suning.mobile.ebuy',
        'appActivity': 'com.suning.mobile.ebuy.member.newlogin.common.ui.LoginActivity',
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
    }
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
