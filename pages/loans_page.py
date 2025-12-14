from playwright.sync_api import Page, expect

class LoansPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.take_out_loan_button = self.page.get_by_role("button", name="Contratar Empréstimo")

    def choose_loan_amount(self, amount: str) -> None:
        self.page.get_by_role("radio", name=amount).wait_for()
        self.page.get_by_role("radio", name=amount).click()

    def click_take_out_loan(self) -> None:
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.take_out_loan_button.click()
    