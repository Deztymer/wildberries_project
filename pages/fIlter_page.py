from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base




class Filter_page(Base):

    def __init__(self, driver, product):
        super().__init__(driver)
        self.driver = driver
        self.product = product

    #locators
    filter_button = "//div[@data-testid = 'filters-all']"
    input_start_price = "//input[@name = 'startN']"
    input_end_price = "//input[@name = 'endN']"
    input_name_product = "(//input[@placeholder='Найти в списке'])[3]"
    show_all_button = "(//button[@class='filter__show-all j-show-whole-filters'])[2]"
    find_checkbox = "(//span[@class='checkbox-with-text__decor'])[3]"
    original_switch = "(//button[@class='btn-switch__btn j-filter-switch'])[2]"
    color_checkbox = "(//span[@title='черный undefined'])[1]"
    approve_filter = "(//button[@class='filters-desktop__btn-main btn-main'])[1]"


    #getters
    def get_filter_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_input_start_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.input_start_price)))

    def get_input_end_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.input_end_price)))

    def get_input_name_product(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.input_name_product)))

    def get_show_all_button(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.show_all_button)))

    def get_find_checkbox(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.find_checkbox)))

    def get_original_switch(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.original_switch)))

    def get_color_checkbox(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.color_checkbox)))

    def get_approve_filter(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.approve_filter)))

    #methods

    def click_filter_button(self):
        self.get_filter_button().click()
        print("Клик по кнопке фильтра")

    def click_input_start_price(self):
        self.get_input_start_price().click()
        self.get_input_start_price().clear()
        self.get_input_start_price().send_keys("2500")
        print("Введена стартовая цена")

    def click_input_end_price(self):
        self.get_input_end_price().click()
        self.get_input_end_price().clear()
        self.get_input_end_price().send_keys("50000")
        print("Введена максимальная цена")

    def click_get_show_all_button(self):
        button = self.get_show_all_button()
        self.scroll_to_element(button)
        button.click()
        print("Раскрыт список производителей")

    def click_find_button(self):
        self.get_find_checkbox().click()
        print("Выбран найденный товар")

    def click_input_name_product(self):
        self.get_input_name_product().send_keys(self.product)
        print("Введено название продукта")



    def click_and_check_original_switch(self):
        self.get_original_switch().click()
        print("Выбран оригинальный товар")

    def click_get_color_checkbox(self):
        self.scroll_to_element(self.get_color_checkbox())
        self.get_color_checkbox().click()
        print("Выбран цвет")

    def click_get_approve_filter(self):
        self.get_approve_filter().click()
        print("Фильтры успешно выбраны")



    def change_filters(self):
        self.click_filter_button()
        self.click_input_start_price()
        self.click_input_end_price()
        self.click_get_show_all_button()
        self.click_input_name_product()
        self.click_find_button()
        self.click_and_check_original_switch()
        self.click_get_color_checkbox()
        self.click_get_approve_filter()
        self.get_screenshot()
