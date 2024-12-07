import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestPersonalAccount:

    @allure.title("Тест на вход в личный кабинет после клика по одноименной кнопке" )
    @allure.description('Проверяем что после клика мы находимся в личном кабинете')
    def test_move_in_pers_acc_after_click_button_licn_kab(self,user,driver_get):
        main_page = MainPage(driver_get)
        login_page = LoginPage(driver_get)
        login_page.enter_account()
        assert main_page.check_main_window_after_add()

    @allure.title('Тест на взод во вкладку история заказов после клика')
    @allure.description('Проверяем что находимся во вкладке история заказов после клика на нее')
    def test_move_istoriya_zakazov_folder(self,user,driver_get):
        main_page = MainPage(driver_get)
        login_page = LoginPage(driver_get)
        login_page.enter_account()
        main_page.click_button_lichnyi_kabinet_in_header()
        login_page.click_button_istoriya_zakazov()
        assert login_page.check_istoriya_zakazov_folder()

    @allure.title('Тест на выход из аккаунта по кнопке "выход"')
    @allure.description('Нажимаем на кнопку выход и проверяем что оказались на главной странице и вышли из акк')
    def test_exit_account(self,user,driver_get):
        main_page = MainPage(driver_get)
        login_page = LoginPage(driver_get)
        login_page.enter_account()
        main_page.click_button_lichnyi_kabinet_in_header()
        login_page.exit_from_account()
        assert login_page.check_exit_account()

