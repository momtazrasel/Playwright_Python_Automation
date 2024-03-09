from automationDemo.src.pages.loginPage import LoginPageClass


def test_login_page(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_method = LoginPageClass(page)
    login_method.click_dropdown_button()
    login_method.submit_button()
    login_method.confirm_button()
