from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.pix_key_field = page.get_by_role("textbox", name="Chave Pix:")
        self.amount_field = page.get_by_role("textbox", name="Valor:")
        self.send_pix_button = page.get_by_role("button", name="Enviar Pix")
        self.verify_bank_statement_button = page.get_by_role("button", name="Ver Extrato")

    def perform_pix_payment(self, pix_key: str, amount: str) -> None:
        self.pix_key_field.press_sequentially(pix_key)
        self.amount_field.press_sequentially(amount)
        self.send_pix_button.click()

    def assert_pix_success(self) -> None:
        expect(self.page.get_by_text("Transação Realizada com Sucesso!")).to_be_visible()
        expect(self.page.get_by_text("A transação foi concluída com sucesso. Você pode voltar para a página principal e continuar suas operações")).to_be_visible()