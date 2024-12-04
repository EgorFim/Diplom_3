import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

class TestMainFunctional:
    @allure.title('Тест переходf на вкладку "конструктор" после клика по ней' )
    @allure.description('Заходим во вкладку личный кабинет и оттуда кликаем по кнопке"нконструктор"')
    def test_move_to_konstruktor_folder_after_click(self,user_2,driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_button_lichnyi_kabinet_in_header()
        main_page.click_button_konstruktor()
        assert main_page.check_successful_click_konstruktor()
    @allure.title('Тест перехода в ленту заказов при клике на одноименную кнопку')
    def test_click_lenta_zakazov_button(self,user_2,driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.button_lenta_zakazov_click()
        assert order_feed_page.check_lenta_zakazov_click_successful()
    @allure.title('Тест на появление окна информации по клику на ингредиент')
    @allure.description('Кликаем на ингредиент и ожидаем появления окна')
    def test_appearance_details_window_after_click(self,user_2,driver):
        main_page = MainPage(driver)
        main_page.click_button_bun()
        assert main_page.check_bun_click()
    @allure.title('Тест закрытия окна с информацией об ингредиенте')
    @allure.description('Нажимаем на крестик и ожидаем закрытие окна')
    def test_close_ingredient_window(self,user_2,driver):
        main_page = MainPage(driver)
        main_page.click_button_bun()
        main_page.close_ingredient_info()
        assert main_page.check_main_window_after_add()
    @allure.title('Тест на изменения каунтера при доюавлении ингредиента в заказ')
    @allure.description('Добавляем ингр в заказ и ожидаем что цифра в каунтере изменится')
    def test_change_ing_counter(self,user_2,driver):
        main_page = MainPage(driver)
        n = main_page.check_change_counter()
        main_page.add_ingredient_in_order()
        m = main_page.check_change_counter()
        assert n != m
    @allure.title('Тест создания заказа')
    @allure.description('Создаем заказ и проверяем его появления в истории заказов')
    def test_make_order(self,user_2,driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        login_page.enter_account()
        main_page.make_order()
        main_page.wait_overlay()
        main_page.close_number_order_window()
        main_page.click_button_lichnyi_kabinet_in_header()
        login_page.click_button_istoriya_zakazov()
        assert login_page.check_istoriya_zakazov_folder()





