from PageObjectLibrary import PageObject

class HomePage(PageObject):
    PAGE_URL = "/account"

    _locators = {
        "first_invoie_details_button": "xpath=/html/body/section/div/div[2]/div[5]/a"
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

    def click_first_invoice(self):
        with self._wait_for_page_refresh():
            link = self.selib.get_element_attribute(self.locator.first_invoie_details_button, "href")
            self.selib.go_to(link)
