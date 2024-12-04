import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import DRIVER_NAME

class MainPage(BasePage):
    @allure.step('Нажимаем кнопку "Заказать" в хедере')
    def click_button_lichnyi_kabinet_in_header(self):
        return self.click_to_element(MainPageLocators.KNOPKA_LICHNYI_KABINET)
    @allure.step('клик кнопки конструктор')
    def button_konstruktor_click(self):
        return self.click_to_element(MainPageLocators.KNOPKA_KONSTRUKTOR)
    @allure.step('клик кнопки лента заказов')
    def button_lenta_zakazov_click(self):
        return self.click_to_element(MainPageLocators.KNOPKA_LENTA_ZAKAZOV)
    @allure.step('проверка успешного нажатия кнопки конструктор')
    def check_button_konstruktor_click_successful(self):
        return self.find_element_with_wait(MainPageLocators.KONSTRUKTOR_PROVERKA)

    @allure.step('нажать кнопку булки')
    def click_button_bun(self):
        return self.click_to_element(MainPageLocators.PROVERKA_VKLADKA_BULKI)
    @allure.step('проверка нажатия кнопки булки')
    def check_bun_click(self):
        return self.find_element_with_wait(MainPageLocators.CHECK_BUN_CLICK)
    @allure.step('закрыть информацию об ингридиенте')
    def close_ingredient_info(self):
        return self.click_to_element(MainPageLocators.EXIT_DETAILS_CROSS)

    @allure.step('добавить ингр в заказ')
    def add_ingredient_in_order(self):
        return self.drag_and_drop_element(MainPageLocators.PROVERKA_VKLADKA_BULKI,MainPageLocators.ING_LIST)
    @allure.step('проверка изменения каунтера ингр')
    def check_change_counter(self):
        return self.get_text_from_element(MainPageLocators.ING_COUNTER)
    @allure.step('проверка главной после входа')
    def check_main_window_after_add(self):
        return self.find_element_with_wait(MainPageLocators.PROVERKA_USPESHNOGO_VHODA)
    @allure.step('нажать кнопку конструктор')
    def click_button_konstruktor(self):
        self.click_to_element(MainPageLocators.KNOPKA_KONSTRUKTOR)
    @allure.step('проверка успешного нажатия кнопки конструктор')
    def check_successful_click_konstruktor(self):
        return self.find_element_with_wait(MainPageLocators.KONSTRUKTOR_PROVERKA)
    @allure.step('сделать заказ')
    def make_order(self):
        self.drag_and_drop_element(MainPageLocators.PROVERKA_VKLADKA_BULKI,MainPageLocators.ING_LIST)
        self.click_to_element(MainPageLocators.ARRANGE_ORDER_BUTTON)

    @allure.step('закрыть окно с номером заказа')
    def close_number_order_window(self):
        if DRIVER_NAME == 'chrome':
            self.clickable_element(MainPageLocators.CLOSE_ORD_WINDOW)
        else:
            self.move_to_element_and_click(MainPageLocators.CLOSE_ORD_WINDOW)
    @allure.step('дождаться изчезновения оверлея')
    def wait_overlay(self):
        self.invis_element(MainPageLocators.WAIT)
    @allure.step('сохранить номер заказа')
    def give_ord_number(self):
        n = self.get_text_from_element(MainPageLocators.DEF_ORDER_NUMBER)
        return f'0{n}'


















