from playwright.sync_api import Page, expect

class CommonPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def assert_text(self, text: str) -> None:
        expect(self.page.get_by_text(text)).to_be_visible()