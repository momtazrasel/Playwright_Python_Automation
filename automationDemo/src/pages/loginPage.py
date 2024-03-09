import time


class LoginPageClass:
    def __init__(self, page):
        self.page = page
        self._dropdownButton = page.locator("(//select[@class='tls-input-select'])[1]")
        self._dropdownOption = page.locator("(//option[@value='gb'])[1]")
        # self._dropdownButton = page.locator("(//h5[normalize-space()='Elements'])[1]")
        self._username = page.locator("")
        self._password = page.locator("")

    def click_dropdown_button(self):
        self._dropdownButton.click()
        time.sleep(2)
        self._dropdownOption.click()
        time.sleep(2)
        # dropdown = self._dropdownButton
        # time.sleep(2)
        # dropdown.select_option("gb")

    def click_dropdown_buttons(self, option_value):
        self._dropdownButton.click()
        time.sleep(2)  # You may want to replace this sleep with proper waiting logic
        dropdown = self._dropdownButton
        dropdown.select_option({'label': option_value})
