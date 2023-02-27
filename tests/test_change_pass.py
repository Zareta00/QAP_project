import pytest
from pages.change_pass import ChangePass
from settings import url_change_pass


'''Восстановление пароля'''


class TestChangePass:

    # Позитивные тесты
    def test_PT025_default_password_recovery_type(self, browser):
        change_pass_page = ChangePass(browser, url_change_pass)
        change_pass_page.open()
        change_pass_page.default_password_recovery_type()

    @pytest.mark.xfail
    def test_PT026_phone_field_validation_valid_data(self, browser):
        change_pass_page = ChangePass(browser, url_change_pass)
        change_pass_page.open()
        change_pass_page.phone_field_validation_valid_data()

    def test_PT027_email_field_validation_valid_data(self, browser):
        change_pass_page = ChangePass(browser, url_change_pass)
        change_pass_page.open()
        change_pass_page.email_field_validation_valid_data()

    def test_PT028_go_back_button(self, browser):
        change_pass_page = ChangePass(browser, url_change_pass)
        change_pass_page.open()
        change_pass_page.go_back_button()

    def test_PT029_link_fut_to_the_user_agreement_page(self, browser):
        change_pass_page = ChangePass(browser, url_change_pass)
        change_pass_page.open()
        change_pass_page.link_to_the_user_agreement_page()

    # Негативные тесты
    def test_NT030_password_recovery_with_blank_fields(self, browser):
        change_pass_page = ChangePass(browser, url_change_pass)
        change_pass_page.open()
        change_pass_page.password_recovery_with_blank_fields()

    def test_NT031_password_recovery_with_blank_captcha(self, browser):
        change_pass_page = ChangePass(browser, url_change_pass)
        change_pass_page.open()
        change_pass_page.password_recovery_with_blank_fields()

    def test_NT032_sql_injection_in_a_text_field(self, browser):
        change_pass_page = ChangePass(browser, url_change_pass)
        change_pass_page.open()
        change_pass_page.sql_injection_in_a_text_field()
