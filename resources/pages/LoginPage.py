from PageObjectLibrary import PageObject

from robot.libraries.BuiltIn import BuiltIn

class LoginPage(PageObject):
    PAGE_URL = ""

    _locators = {
        "username": "css=div.mt-3:nth-child(1) > div:nth-child(2) > input:nth-child(1)",
        "password": "css=div.row:nth-child(2) > div:nth-child(2) > input:nth-child(1)",
        "submit_button":  "id=btnLogin",
        "alert_wrong_user_or_pass": "css=.alert"
    }

    def _is_current_page(self):
        # this site uses the same title for many pages,
        # so we can't rely on the default implementation
        # of this function. Instead, we'll check the page
        # location, and raise an appropriate error if
        # we are not on the correct page
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def do_login(self, user):
        MASS = BuiltIn().get_variable_value("${MASS}")
        self.enter_username(MASS['USERS'][user]['user'])
        self.enter_password(MASS['USERS'][user]['password'])
        with self._wait_for_page_refresh():
            self.click_the_login_button()

    def enter_username(self, username):
        """Type the given text into the username field """
        self.selib.input_text(self.locator.username, username)

    def enter_password(self, password):
        """Type the given text into the password field"""
        self.selib.input_text(self.locator.password, password)

    def click_the_login_button(self):
        """Clicks the submit button on the form"""
        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.submit_button)

    def check_login_error_message(self):
        """Checks that the user was not able to log in using invalid credentials"""
        alert = self.selib.get_text(self.locator.alert_wrong_user_or_pass)
        BuiltIn().should_be_equal(alert, "Wrong username or password")