from selenium.webdriver.common.by import By

class OrderFeedLocators:
    PROVERKA_CLICK_LENTA_ZAKAZOV = By.XPATH, './/*[text()="Готовы:"]'
    #вкладка лента заказов
    ORDERS_OF_ALL_TIME = By.XPATH, '//div[2]/p[2][@class="OrderFeed_number__2MbrQ text text_type_digits-large"]'
    #заказы за все время
    TODAYS_ORDERS = By.XPATH, '//div[3]/p[2][@class="OrderFeed_number__2MbrQ text text_type_digits-large"]'
    #заказы сегодня
    IN_WORK_FIELD = By.XPATH, './/li[@class="text text_type_digits-default mb-2"]'
    #поле "в работе"
    IN_WORK_DEF = By.XPATH, './/li[@class="text text_type_main-small"]'
    #поле в работе изначальное
    FOR_CYCLE_ORDERS = By.XPATH, './/p[@class="text text_type_digits-default"]'
    #локатор для скролла
    CHECK_HISTORY = By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]'
    #проверка что видна история заказов


