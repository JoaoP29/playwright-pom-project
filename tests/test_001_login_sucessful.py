from playwright.sync_api import Page, expect

def test_001_login_sucessful(page, login_page) -> None:
    login_page.navigate()
    login_page.login("user1", "pass1")
    expect(page).to_have_url('https://leogcarvalho.github.io/simulabank/home.html')
    expect(page.get_by_role("heading")).to_be_visible()
    expect(page.get_by_role("heading")).to_have_text('Bem-vindo ao SimulaBank!')