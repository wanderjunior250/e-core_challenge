from PageObjectLibrary import PageObject

class InvoiceDetailsPage(PageObject):
    PAGE_URL = "/invoice/0"

    _locators = {
        "hotel_name_label": "css=section > div > h4",
        "invoice_date_label": "css=div > ul > li:nth-child(1)",
        "due_date_label": "css=div > ul > li:nth-child(2)",
        "invoice_number_label": "css=div > h6",
        "booking_code_label": "css=table:nth-child(8) > tbody > tr:nth-child(1) > td:nth-child(2)",
        "customer_details_label": "css=section > div > div",
        "room_label": "css=table:nth-child(8) > tbody > tr:nth-child(2) > td:nth-child(2)",
        "checkin_label": "css=table:nth-child(8) > tbody > tr:nth-child(5) > td:nth-child(2)",
        "checkout_label": "css=table:nth-child(8) > tbody > tr:nth-child(6) > td:nth-child(2)",
        "total_stay_count_label": "css=table:nth-child(8) > tbody > tr:nth-child(3) > td:nth-child(2)",
        "total_stay_amount_label": "css=table:nth-child(8) > tbody > tr:nth-child(4) > td:nth-child(2)",
        "deposit_now_label": "css=table:nth-child(12) > tbody > tr > td:nth-child(1)",
        "tax_vat_label": "css=table:nth-child(12) > tbody > tr > td:nth-child(2)",
        "total_amount_label": "css=table:nth-child(12) > tbody > tr > td:nth-child(3)"
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

    def validate_invoice_details(self, invoice):
        """This method validates the invoice details according to the provided mass as a dictionary"""
        self.selib.element_text_should_be(self.locator.hotel_name_label ,invoice["hotel_name"])
        self.selib.element_should_contain(self.locator.invoice_date_label ,invoice["invoice_date"])
        self.selib.element_should_contain(self.locator.due_date_label ,invoice["due_date"])
        self.selib.element_should_contain(self.locator.invoice_number_label ,invoice["invoice_number"])
        self.selib.element_text_should_be(self.locator.booking_code_label ,invoice["booking_code"])
        self.selib.element_should_contain(self.locator.customer_details_label ,invoice["customer_details"]["name"])
        self.selib.element_should_contain(self.locator.customer_details_label ,invoice["customer_details"]["address"])
        self.selib.element_should_contain(self.locator.customer_details_label ,invoice["customer_details"]["code"])
        self.selib.element_text_should_be(self.locator.room_label ,invoice["room"])
        self.selib.element_text_should_be(self.locator.checkin_label ,invoice["checkin"])
        self.selib.element_text_should_be(self.locator.checkout_label ,invoice["checkout"])
        self.selib.element_text_should_be(self.locator.total_stay_count_label ,invoice["total_stay_count"])
        self.selib.element_text_should_be(self.locator.total_stay_amount_label ,invoice["total_stay_amount"])
        self.selib.element_text_should_be(self.locator.deposit_now_label ,invoice["deposit_now"])
        self.selib.element_text_should_be(self.locator.tax_vat_label ,invoice["tax_vat"])
        self.selib.element_text_should_be(self.locator.total_amount_label ,invoice["total_amount"])