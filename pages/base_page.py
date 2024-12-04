from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
            locator))
        return self.driver.find_element(*locator)

    def finds_elements(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)


    def find_element_with_wait_in_ord(self, locator):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(
            locator))

    def invis_element(self,locator):
        return WebDriverWait(self.driver, 20).until_not(expected_conditions.visibility_of_element_located(locator))


    def clickable_element(self, locator):
        element = self.find_element_with_wait_in_ord(locator)
        self.driver.execute_script('arguments[0].click();', element)


    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(element))

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()


    def drag_and_drop_element(self, locator_from, locator_to):
        self.find_element_with_wait(locator_from)
        self.find_element_with_wait(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                           var source = arguments[0];
                           var target = arguments[1];
                           var evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           source.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           source.dispatchEvent(evt);
                       """, element_from, element_to)




