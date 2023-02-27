from settings import valid_email, sql_injection, random_int
from pages.base_page import BasePage
from pages.locators import BaseLocators, AuthLocators, ChangePassLocators, RegLocators, \
    UserAgreementLocators, RejectedRequestLocators


class AuthPage(BasePage):
    # Позитивные тесты
    # PT013 метод проверки перехода на форму авторизации
    def the_authorization_form_is_open(self):
        assert self.is_element_present(AuthLocators.AUTH_HEADING)
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # PT014 метод проверки расположения логотипа и слогана
    def location_of_the_logo_and_slogan(self):
        assert self.is_element_present(AuthLocators.AUTH_LOGO), "element not found"
        assert self.is_element_present(AuthLocators.AUTH_SLOGAN), "element not found"

    # PT015 метод проверки расположения меню выбора типа аутентификации
    def location_of_the_tab_menu(self):
        assert self.is_element_present(AuthLocators.AUTH_TAB_MENU), "element not found"

    # PT016 метод проверки типа аутентификации по умолчанию
    def default_authentication_type(self):
        assert self.is_element_present(AuthLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "element not found"

    # PT017 метод проверки автоматического изменения типа аутентификации
    def automatic_change_of_authentication_type(self):
        self.find_element(AuthLocators.AUTH_USERNAME_INPUT).send_keys(valid_email())
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(AuthLocators.AUTH_USERNAME_INPUT_ACTIV_EMAIL), "element not found"

    # PT018 метод проверки ссылки на форму восстановления пароля
    def link_to_the_password_recovery_form(self):
        self.find_element(AuthLocators.AUTH_FORGOT_PASSWORD_LINK).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassLocators.CHANGE_PASS_HEADING), "element not found"

    # PT019 метод проверки ссылки на форму регистрации
    def link_to_the_registration_form(self):
        self.find_element(AuthLocators.AUTH_REGISTER_LINK).click()
        assert self.is_element_present(RegLocators.REG_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" \
               in self.browser.current_url, "url do not match"

    # PT020 метод проверки ссылки под кнопкой "Войти" на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(AuthLocators.AUTH_USER_AGREEMENT_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # PT021 метод проверки ссылки в футере на страницу с пользовательским соглашением
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(AuthLocators.AUTH_PRIVACY_POLICY_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # PT022 метод проверки ссылки на страницу авторизации с помощью соцсети "ВКонтакте"
    def link_to_social_vk(self):
        self.find_element(AuthLocators.AUTH_SOCIAL_VK_LINK).click()
        assert "https://oauth.vk.com/authorize" in self.browser.current_url, "url do not match"

    # Негативные тесты
    # NT023 метод проверки авторизации с незаполненными полями
    def authorization_with_blank_fields(self):
        self.find_element(AuthLocators.AUTH_TAB_PHONE).click()
        self.find_element(AuthLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(AuthLocators.AUTH_ERROR_ENTER_PHONE_NUMBER), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # NT024 метод проверки текстового поля на SQL
    def sql_injection_in_a_text_field(self):
        self.find_element(AuthLocators.AUTH_USERNAME_INPUT).send_keys(sql_injection())
        self.find_element(AuthLocators.AUTH_PASSWORD_INPUT).send_keys(random_int())
        self.find_element(AuthLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(RejectedRequestLocators.REJECTED_REQUEST_HEADING), "element not found"
        assert self.is_element_present(RejectedRequestLocators.REJECTED_REQUEST_INFO), "element not found"
