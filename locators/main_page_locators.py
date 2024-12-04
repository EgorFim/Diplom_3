from selenium.webdriver.common.by import By

class MainPageLocators:

    VOITY_BUTTON = By.XPATH,'.//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    #кнопка "Войти в аккаунт" на главной странице
    PROVERKA_USPESHNOGO_VHODA = By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    #поиск кнопки "Оформить заказ" на главной
    KNOPKA_LICHNYI_KABINET = By.XPATH, './/*[text()="Личный Кабинет"]'
    #кнопка "Личный кабинет" на главной
    VOITY_IZ_OKNA_REGISTRACII = By.XPATH, './/*[text()="Войти"]'
    #кнопка "Войти" в окне ренистрации
    ZAGRUZKA_GLAVNOI = By.XPATH, './/*[@class="AppHeader_header__logo__2D0X2"]'
    #поиск хедера на главной
    KNOPKA_KONSTRUKTOR = By.XPATH, './/*[text()="Конструктор"]'
    #поиск кнопки "Конструктор"
    KONSTRUKTOR_PROVERKA = By.XPATH, './/*[text()="Соберите бургер"]'
    #поиск текста "Соберите бургер"
    KNOPKA_STELLAR = By.XPATH, './/*[@class="AppHeader_header__logo__2D0X2"]'
    #кнопка Stellar Burger
    KNOPKA_VYHOD = By.XPATH, './/button[text()="Выход"]'
    #кнопка "Выход"
    KNOPKA_SOUSY = By.XPATH, './/*[text()="Соусы"]'
    #кнопка "Соусы"
    KNOPKA_BULKI = By.XPATH, './/*[text()="Булки"]'
    #кнопка "Булки"
    KNOPKA_NACHINKI = By.XPATH, './/*[text()="Начинки"]'
    #кнопка "Начинки"
    PROVERKA_VKLADKA_SOUSY = By.XPATH, './/*[text()="Соус Spicy-X"]'
    #поиск названия соуса
    PROVERKA_VKLADKA_BULKI = By.XPATH, './/*[text()="Флюоресцентная булка R2-D3"]'
    #поиск названия булки
    PROVERKA_VKLADKA_NACHINKI = By.XPATH, './/*[text()="Мясо бессмертных моллюсков Protostomia"]'
    #поиск названия начинки
    PROVERKA_VYHODA = By.XPATH, './/*[text()="Вход"]'
    #поиск кнопки "Вход" для проверки выхода из аккаунта
    KNOPKA_LENTA_ZAKAZOV = By.XPATH, './/*[text()="Лента Заказов"]'
    #кнопка лента заказов в хедере
    CHECK_BUN_CLICK = By.XPATH, './/*[text()="Детали ингредиента"]'
    #окно информации об ингредиенте
    EXIT_DETAILS_CROSS = By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    #крест закрытия окна деталей
    ING_LIST = By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]'
    #список ингредиентов в заказе
    ING_COUNTER = By.XPATH, './/p[@class="counter_counter__num__3nue1"]'
    #счетчик кол-ва ингредиентов
    DEF_ORDER_NUMBER = By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'
    #номер созданного заказа
    ARRANGE_ORDER_BUTTON = By.XPATH, './/*[text()="Оформить заказ"]'
    #кнопка "оформить заказа
    CLOSE_ORD_WINDOW = By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    #крестик закрытия окна созданного заказа
    OVERLAY =  By.XPATH, './/*[@class="Modal_modal_overlay__x2ZCr"]'
    #локатор оверлэя перекрывающего страницу
    WAIT = By.XPATH, './/*[text()="9999"]'
    #локатор ожидания изменения номера заказа