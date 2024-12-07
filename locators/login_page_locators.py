from selenium.webdriver.common.by import By

class LoginPageLocators:
    NAME_INPUT_FIELD = By.XPATH, '//label[ text()="Имя" ]/parent::div/input'
    # поле ввода имени при регистрации
    EMAIL_INPUT_FIELD = By.XPATH, '//label[ text()="Email" ]/parent::div/input'
    # поле ввода почты при регистрации
    PASSWORD_INPUT_FIELD = By.XPATH, '//label[ text()="Пароль" ]/parent::div/input'
    # поле ввода пароля при регистрации
    REGISTER_BUTTON_1 = By.XPATH, './/a[@class = "Auth_link__1fOlj"]'
    # кнопка "Зарегистрироваться" на окне авторизации
    REGISTER_BUTTON_FINAL = By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
    # кнопка "Зарегистрироваться" на окне регистрации
    EMAIL_ADD = By.XPATH, './/input[@class="text input__textfield text_type_main-default"]'
    # поле email в окне авторизации
    PASSWORD_ADD = By.XPATH, './/input[@type="password"]'
    # поле password в окне авторизации
    VOITY_BUTTON_AFTER_ADD = By.XPATH, './/button[text()="Войти"]'
    # кнопка "Войти" в окне авторизации
    OZHIDANIE_POSLE_ZAPOLNENIYA_REGISTRACII = By.XPATH, './/h2[text()="Вход"]'
    # ожидание загрузки после регистрации
    NEVERNIY_PAROL = By.XPATH, './/p[@class="input__error text_type_main-default"]'
    # проверка что пароль введен не верно
    V_LICHNOM_KABINETE = By.XPATH, './/*[text()="В этом разделе вы можете изменить свои персональные данные"]'
    # поиск элемента с текстом "В этом разделе вы можете изменить свои персональные данные"
    KNOPKA_VOSSTANOVIT_PAROL = By.XPATH, './/*[text()="Восстановить пароль"]'
    # кнопка "Восстановить" в окне авторизации
    MAKE_PASSWORD_VISIBLE = By.XPATH, './/div[@class="input__icon input__icon-action"]'
    # нажать символ видимости пароля
    CHECK_PASSWORD_FIELD = By.XPATH, './/div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]'
    # проверка что поле видимо
    RECOVERY_PASSWORD_WINDOW = By.XPATH, './/*[text()="Восстановление пароля"]'
    # окно "восстановленме пароля"
    BUTTON_VOSSTANOVIT_FINAL = By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
    # кнопка восстановить после ввода мэйла
    BUTTON_ISTORIYA_ZAKAZOV = By.XPATH, './/*[text()="История заказов"]'
    # вкладка история заказов в лич кабинете
    CHECK_ISTORIYA_ZAKAZOV_FOLDER = By.XPATH, './/a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]'
    # проверка нажатия клика истории заказов
    BUTTON_EXIT_ACCOUNT = By.XPATH, './/*[text()="Выход"]'
    # кнопка "выход" в личном кабинете
    ISTORIYA_ZAKAZOV_PAGE_CHECK = By.XPATH, './/a[@class="Account_contentBox__2CPm3"]'
    # проверка нахождения во вкладке история заказов
    ORDER_INFO_WINDOW = By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]'
    # локаор окна заказа
    CHECK_RESTORE_PASSWORD_FINAL = By.XPATH, './/*[text()="Введите код из письма"]'
    # проверка удачного восстановления пароля
    EMAIL_FIELD_IN_RESTORE = By.XPATH, './/input[@class="text input__textfield text_type_main-default"]'
    # поле мэйл на странице восстановления пароля
    ORDER_IN_ACCOUNT = By.XPATH, './/a[@class="OrderHistory_link__1iNby"]'
    # заказ в личном кабинете
    ORD_WINDOW_IN_ACCOUNT = By.XPATH, './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]'
    # окно информации о заказе в личном кабинете
    ORDER_NUMBER_IN_ACCOUNT = By.XPATH, '//p[@class="text text_type_digits-default"]'
    # номер заказа в лич кабинете
    KNOPKA_LICHNYI_KABINET_ENTER = By.XPATH, './/*[text()="Личный Кабинет"]'
    # кнопка "Личный кабинет" на главной
