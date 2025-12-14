from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Usuário:")
        self.password_input = page.get_by_role("textbox", name="Senha:")
        self.login_button = page.get_by_role("button", name="Entrar")

    def navigate(self) -> None:
        self.page.goto("https://leogcarvalho.github.io/simulabank/login.html")

    def login(self, username: str, password: str) -> None:
        self.username_input.press_sequentially(username)
        self.password_input.press_sequentially(password)
        self.login_button.click()
        self.page.get_by_text("Bem-vindo ao SimulaBank!").wait_for()

