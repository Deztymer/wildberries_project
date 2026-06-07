from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
import time
from selenium.webdriver.common.action_chains import ActionChains

class Sorted_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    maker_text = "//span[@class = 'product-card__brand']"
    model_text = "//span[@class = 'product-card__name']"
    heading_model = "(//td)[2]"


    #getters
    def get_maker_text(self):
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.maker_text))
        )
        return self.driver.find_elements(By.XPATH, self.maker_text)

    def get_model_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.model_text))
        )
        return self.driver.find_elements(By.XPATH, self.model_text)

    def get_heading_model(self):
        #time.sleep(5)
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.heading_model)))



    #methods

    def assert_maker_count(self, prod):
        assert sum(prod.lower() in el.text.lower() for el in self.get_maker_text()) > 10, f"Производитель '{prod}' встречается меньше 10 раз, фильтр не применен"
        print("Фильтр с производителем успешно применен")

    def change_model_count(self, mod):

        for element in self.get_model_text():
            if mod.lower() in element.text.lower():
                self.scroll_to_element(element)
                try:
                    actions = ActionChains(self.driver)
                    actions.move_to_element(element).click().perform()
                    return True
                except Exception as e:
                    print(f"Не удалось кликнуть по выбранной модели {mod} из-за ошибки {e}")
                print(f"Кликнули по модели: {mod}")
                return True
        print(f"Модель '{mod}' не найдена на странице")
        return False

    def check_heading_model(self, mod):
        assert mod.lower() == self.get_heading_model().text.lower(), f"Модель {mod} выбрана неверно"
        print(f"Модель {mod} выбрана верно")

    def search_headphones(self, prod, mod):
        self.get_screenshot()
        self.assert_maker_count(prod)
        self.change_model_count(mod)
        self.check_heading_model(mod)