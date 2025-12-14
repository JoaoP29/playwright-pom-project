def test_005_verify_pix_above_limits(page, login_page, home_page, pix_page, common_page) -> None:
    login_page.navigate()
    login_page.login("user1", "pass1")
    home_page.access_menu("Fazer Pix")
    pix_page.perform_pix_payment("999.999.999-99", "3001")
    common_page.assert_text("O valor do Pix não pode ultrapassar R$ 3.000,00. Tente novamente.")