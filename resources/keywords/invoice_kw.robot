*** Keywords ***
| Then the application should open invoice details screen
| | The current page should be | InvoiceDetailsPage

| And the information presented should match ${invoice}
| | Validate Invoice Details | ${MASS['INVOICES']['${invoice}']}