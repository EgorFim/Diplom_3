import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title('Тест появления окна с инф о заказе при клике на него в истории заказов')
    @allure.description('Входим в аккаунт, и создаем заказ, после этого проверяем появление окна при нажатии на заказ')
    def test_order_info_after_click(self,user,driver_get):
        login_page = LoginPage(driver_get)
        main_page = MainPage(driver_get)
        login_page.enter_account()
        main_page.make_order()
        main_page.wait_overlay()
        main_page.close_number_order_window()
        main_page.check_main_window_after_add()
        main_page.click_button_lichnyi_kabinet_in_header()
        login_page.click_button_istoriya_zakazov()
        login_page.click_on_order_in_acc()
        assert login_page.check_view_order_details()

    @allure.title('Тест на появление заказа в ленте заказов')
    @allure.description('Проверяем что созданный пользователем заказ отображается в ленте заказов')
    def test_order_in_order_list(self,user,driver_get):
        login_page = LoginPage(driver_get)
        main_page = MainPage(driver_get)
        order_feed_page = OrderFeedPage(driver_get)
        login_page.enter_account()
        main_page.make_order()
        main_page.wait_overlay()
        main_page.close_number_order_window()
        main_page.click_button_lichnyi_kabinet_in_header()
        login_page.click_on_order_history()
        m = login_page.get_order_number()
        main_page.button_lenta_zakazov_click()
        order_feed_page.check_history()
        n= order_feed_page.scroll_in_history()
        assert m == n

    @allure.title('Тест на изменение количества заказов за все время после создания заказа')
    @allure.description('Создаем заказ и проверяем что количество заказов после стало больше')
    def test_counter_orders_of_all_time_change(self,user,driver_get):
        login_page = LoginPage(driver_get)
        main_page = MainPage(driver_get)
        order_feed_page = OrderFeedPage(driver_get)
        main_page.button_lenta_zakazov_click()
        n = order_feed_page.count_of_all_time_ord()
        login_page.enter_account()
        main_page.make_order()
        main_page.wait_overlay()
        main_page.close_number_order_window()
        main_page.button_lenta_zakazov_click()
        m = order_feed_page.count_of_all_time_ord()
        assert m > n

    @allure.title('Тест на изменение количества заказов за сегодня после создания заказа')
    @allure.description('Создаем заказ и проверяем что количество заказов после стало больше')
    def test_counter_today_orders_change(self,user,driver_get):
        login_page = LoginPage(driver_get)
        main_page = MainPage(driver_get)
        order_feed_page = OrderFeedPage(driver_get)
        main_page.button_lenta_zakazov_click()
        n = order_feed_page.count_today_ord()
        login_page.enter_account()
        main_page.make_order()
        main_page.wait_overlay()
        main_page.close_number_order_window()
        main_page.button_lenta_zakazov_click()
        m = order_feed_page.count_today_ord()
        assert m > n

    @allure.title('Тест на появление номера созданного заказа в в списке "в работе"')
    @allure.description('Проверяем что после создания заказа его номер появился в в поле "в работе"')
    def test_new_order_in_work(self,user,driver_get):
        login_page = LoginPage(driver_get)
        main_page = MainPage(driver_get)
        order_feed_page = OrderFeedPage(driver_get)
        login_page.enter_account()
        main_page.make_order()
        main_page.wait_overlay()
        m = main_page.give_ord_number()
        main_page.close_number_order_window()
        main_page.button_lenta_zakazov_click()
        n = order_feed_page.check_in_work_field()
        assert m == n



