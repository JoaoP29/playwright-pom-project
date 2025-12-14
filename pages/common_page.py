from playwright.sync_api import Page, expect

class CommonPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.return_to_home_button = page.get_by_role("button", name="Voltar para a Home")

    def assert_text(self, text: str) -> None:
        expect(self.page.get_by_text(text)).to_be_visible()

    def return_to_home(self) -> None:
        self.return_to_home_button.wait_for()
        self.return_to_home_button.click()