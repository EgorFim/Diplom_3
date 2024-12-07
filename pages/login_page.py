import allure
from data import EMAIL_TEXT, PASSWORD_TEXT
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Заполняем поля email')
    def fill_email_field_in_add(self):
        self.add_text_to_element(LoginPageLocators.EMAIL_ADD,EMAIL_TEXT)

    @allure.step('кликаем кнопку "восстановить"')
    def click_button_vosstanovit(self):
        self.click_to_element(LoginPageLocators.KNOPKA_VOSSTANOVIT_PAROL)

    @allure.step('делаем пароль видимым')
    def click_to_make_password_visible(self):
        self.click_to_element(LoginPageLocators.MAKE_PASSWORD_VISIBLE)

    @allure.step('заполняем поле пароль')
    def fill_password_field_in_add(self):
        self.add_text_to_element(LoginPageLocators.PASSWORD_ADD,PASSWORD_TEXT)

    @allure.step('проверяем что пароль виден')
    def check_password_field(self):
        return self.find_element_with_wait(LoginPageLocators.CHECK_PASSWORD_FIELD)

    @allure.step('проверяем что находимся в окне восстановления пароля')
    def check_recovery_password_window(self):
        return self.find_element_with_wait(LoginPageLocators.RECOVERY_PASSWORD_WINDOW)

    @allure.step('кнопка восстановить под полем email')
    def click_to_button_vosstanovit_under_email_field(self):
        return self.click_to_element(LoginPageLocators.BUTTON_VOSSTANOVIT_FINAL)

    @allure.step('клик кнопки история заказов')
    def click_button_istoriya_zakazov(self):
        return self.click_to_element(LoginPageLocators.BUTTON_ISTORIYA_ZAKAZOV)

    @allure.step('клик кнопки выход из аккаунта')
    def exit_from_account(self):
        return self.click_to_element(LoginPageLocators.BUTTON_EXIT_ACCOUNT)

    @allure.step('проверка выхода из аккаунта')
    def enter_account_in_added_window(self):
        return self.click_to_element(LoginPageLocators.VOITY_BUTTON_AFTER_ADD)

    @allure.step('проверка нахождения во вкладке история заказов')
    def check_is_istoriya_zakazov_folder(self):
        return self.find_element_with_wait(LoginPageLocators.ISTORIYA_ZAKAZOV_PAGE_CHECK)

    @allure.step('проверка выхода из аккаунта')
    def check_exit_account(self):
        return self.find_element_with_wait(LoginPageLocators.REGISTER_BUTTON_1)


    @allure.step('клик на вкладку история заказов')
    def click_on_order_history(self):
        return self.click_to_element(LoginPageLocators.BUTTON_ISTORIYA_ZAKAZOV)

    @allure.step('проверка видимости окна с инфо о заказе')
    def check_info_about_order(self):
        return self.find_element_with_wait(LoginPageLocators.ORDER_INFO_WINDOW)

    @allure.step('проверка нахождения в последнем окне восст пароля')
    def check_restore_password_window(self):
        return self.find_element_with_wait(LoginPageLocators.CHECK_RESTORE_PASSWORD_FINAL)

    @allure.step('заполнить email при восстановлении пароля')
    def add_email_field_in_restore(self):
        return self.add_text_to_element(LoginPageLocators.EMAIL_FIELD_IN_RESTORE,EMAIL_TEXT)

    @allure.step('войти в аккаунт')
    def enter_account(self):
        self.click_to_element(LoginPageLocators.KNOPKA_LICHNYI_KABINET_ENTER)
        self.fill_email_field_in_add()
        self.fill_password_field_in_add()
        self.enter_account_in_added_window()

    @allure.step('проверка нахождения во вкладке история заказов')
    def check_istoriya_zakazov_folder(self):
        return self.find_element_with_wait(LoginPageLocators.CHECK_ISTORIYA_ZAKAZOV_FOLDER)

    @allure.step('клик по заказу в аккаунте')
    def click_on_order_in_acc(self):
        return self.click_to_element(LoginPageLocators.ORDER_IN_ACCOUNT)

    @allure.step('проверить отображение деталей заказа')
    def check_view_order_details(self):
        return self.find_element_with_wait(LoginPageLocators.ORD_WINDOW_IN_ACCOUNT)

    @allure.step('получить номер заказа в списке в аккаунте')
    def get_order_number(self):
        return self.get_text_from_element(LoginPageLocators.ORDER_NUMBER_IN_ACCOUNT)












