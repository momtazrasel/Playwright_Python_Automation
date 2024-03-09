import time

from automationDemo.src.pages.loginPage import LoginPageClass


def test_login_page(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_method = LoginPageClass(page)
    # time.sleep(6)
    login_method.click_dropdown_button()
