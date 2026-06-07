from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.common.exceptions import WebDriverException


class Main_page(Base):

    base_url = "https://www.wildberries.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    menu_button = "//button[@data-testid = 'nav-burger-menu']" #Селектор кнопки меню
    electronic_button = "//li[@data-menu-id = '4830']" #Селектор кнопки раздела электронники
    headphones_button = "//li[@data-menu-id = '9468']"#Селектор кнопки выбора наушников


    #getters
    def get_menu_button(self):
        return WebDriverWait(self.driver, 65).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_electronic_bitton(self):
        return WebDriverWait(self.driver, 65).until(EC.element_to_be_clickable((By.XPATH, self.electronic_button)))

    def get_headphones_bitton(self):
        return WebDriverWait(self.driver, 65).until(EC.element_to_be_clickable((By.XPATH, self.headphones_button)))

    #methods

    def click_menu_button(self):
        try:
            self.get_menu_button().click()
            print("Клик по кнопке меню")
        except WebDriverException as e:
            print(f"Произошла ощибка: {e.msg}, \nDыполняю повторную попытку клика")
            self.driver.refresh()
            self.get_menu_button().click()
            print("Клик по кнопке меню")

    def click_and_check_electronic_button(self):
        assert self.get_electronic_bitton().text == "Электроника"
        print("Текст заголовка пункта меню соответствует заданному")
        self.get_electronic_bitton().click()
        print("Выбран пункт меню")

    def click_and_check_headphones_button(self):
        assert self.get_headphones_bitton().text == "Гарнитуры и наушники"
        print("Текст заголовка пункта меню соответствует заданному")
        self.get_headphones_bitton().click()
        print("Выбран пункт меню")
        assert self.driver.current_url == "https://www.wildberries.ru/catalog/elektronika/igry-i-razvlecheniya/aksessuary/garnitury"
        print("Нужная страница открылась")

    def change_headphones(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.click_menu_button()
        self.click_and_check_electronic_button()
        self.click_and_check_headphones_button()