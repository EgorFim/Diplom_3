import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('проверка успешного клика по ленте заказов в хедере')
    def check_lenta_zakazov_click_successful(self):
        return self.find_element_with_wait(OrderFeedLocators.PROVERKA_CLICK_LENTA_ZAKAZOV)
    @allure.step('взять текст из поля в работе')
    def give_in_work_field_text(self):
        return self.get_text_from_element(OrderFeedLocators.IN_WORK_FIELD)
    @allure.step('взять номер заказа из поля в работе')
    def check_in_work_field(self):
        self.invis_element(OrderFeedLocators.IN_WORK_DEF)
        return self.get_text_from_element(OrderFeedLocators.IN_WORK_FIELD)
    @allure.step('проверить отображение списка заказов в ленте')
    def cycle_of_orders(self):
        return self.finds_elements(OrderFeedLocators.FOR_CYCLE_ORDERS)
    @allure.step('каунтер заказов за все время')
    def count_of_all_time_ord(self):
        return self.get_text_from_element(OrderFeedLocators.ORDERS_OF_ALL_TIME)
    @allure.step('каунтер заказов за сегодня')
    def count_today_ord(self):
        return self.get_text_from_element(OrderFeedLocators.TODAYS_ORDERS)

    @allure.step('прокрутить историю заказов')
    def scroll_in_history(self):
        self.scroll_to_element(OrderFeedLocators.FOR_CYCLE_ORDERS)
        return self.get_text_from_element(OrderFeedLocators.FOR_CYCLE_ORDERS)
    @allure.step('проверить наличие списка истории заказов')
    def check_history(self):
        return self.find_element_with_wait(OrderFeedLocators.CHECK_HISTORY)


