import time


class LoginPageClass:
    def __init__(self, page):
        self.page = page
        self._dropdownButton = page.locator("(//select[@class='tls-input-select'])[1]")
        self._dropdownOption = page.locator("(//option[@value='gb'])[1]")
        self._submitButton = page.locator("(//button[normalize-space()='Envoyer'])[1]")
        self._confirmButton = page.locator("//button[@class = 'tls-button-primary -uppercase']")
        # self._dropdownButton = page.locator("(//h5[normalize-space()='Elements'])[1]")
        self._username = page.locator("")
        self._password = page.locator("")

    def click_dropdown_button(self):
        # self._dropdownButton.click()
        time.sleep(2)
        dropdown = self._dropdownButton
        dropdown.select_option(label='Royaume-Uni')
        time.sleep(3)

    def submit_button(self):
        time.sleep(2)
        self._submitButton.click()
        time.sleep(4)

    def confirm_button(self):
        time.sleep(2)
        self._confirmButton.click()
        time.sleep(6)

