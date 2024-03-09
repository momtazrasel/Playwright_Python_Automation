import time


class LoginPageClass:
    def __init__(self, page):
        self.page = page
        self._dropdownButton = page.locator("(//select[@class='tls-input-select'])[1]")
        # self._dropdownButton = page.locator("(//h5[normalize-space()='Elements'])[1]")
        self._username = page.locator("")
        self._password = page.locator("")

    def click_dropdown_button(self):
        self._dropdownButton.click()
        time.sleep(2)
