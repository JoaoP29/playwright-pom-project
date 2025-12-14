from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.welcome_heading = page.get_by_role("heading", name="Bem-vindo ao SimulaBank!")
        self.verify_bank_statement_button = page.get_by_role("button", name="Ver Extrato")
        self.pix_payment_button = page.get_by_role("button", name="Fazer Pix")

    def navigate(self) -> None:
        self.page.goto("https://leogcarvalho.github.io/simulabank/home.html")

    def access_menu(self, menu: str) -> None:
        self.verify_bank_statement_button = self.page.get_by_role("button", name=menu).click()

    def assert_actual_amount(self, expected_actual_amount) -> None:
        self.page.get_by_text(expected_actual_amount)