import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage



class TestPassword:


    @allure.title('Тест на переход на страницу восстановления пароля')
    @allure.description('Проверяем переход на страницу восстановления пароля по клику на восстановить')
    def test_move_to_restore_password_window_after_click(self,user_2,driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_button_lichnyi_kabinet_in_header()
        login_page.click_button_vosstanovit()
        assert login_page.check_recovery_password_window()

    @allure.title('Тест на переход к финальной странице восстановления')
    @allure.description('Проверяем что после заполнения пароля и клика по кнопке восстановить мы переходим к посл шагу восстановления')
    def test_add_email_and_click_button_vosstanovit(self,user_2,driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_button_lichnyi_kabinet_in_header()
        login_page.click_button_vosstanovit()
        login_page.add_email_field_in_restore()
        login_page.click_to_button_vosstanovit_under_email_field()
        assert login_page.check_restore_password_window()

    @allure.title('Тест сделать пароль видимым при клике на символ глаза')
    @allure.description('В окне пароля кликаем на символ глаза и проверяем чо пароль виден')
    def test_make_password_visible(self,user_2,driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_button_lichnyi_kabinet_in_header()
        login_page.fill_password_field_in_add()
        login_page.click_to_make_password_visible()
        assert login_page.check_password_field()
