from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class Buy_page(Base):

    base_url = "https://www.wildberries.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    buy_product = "(//button[@class='mo-button mo-button_view_fillLight mo-button_colors_brand mo-button_width_fill mo-button_size_large buyNowButton--k2IKT'])[1]"
    price_text = "(//span[@class='priceBlockPrice--xf8pi'])[1]"
    result_price_text = "(//div[@class='list-item__price-new red-price'])[1]"
    buy_button = "(//div[@class='j-pos-btn-confirm-order'])[1]"


    #getters
    def get_buy_product(self):
        return WebDriverWait(self.driver, 65).until(EC.element_to_be_clickable((By.XPATH, self.buy_product)))

    def get_price_text(self):
        return WebDriverWait(self.driver, 65).until(EC.visibility_of_element_located((By.XPATH, self.price_text)))

    def get_result_price_text(self):
        return WebDriverWait(self.driver, 65).until(EC.visibility_of_element_located((By.XPATH, self.result_price_text)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 65).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))


    #methods
    def copy_get_price_text(self):
        self.product_price = self.get_price_text().text

    def click_get_buy_product(self):
        self.get_buy_product().click()
        print("Клик по кнопке покупки")


    def assert_price_product(self):
        assert self.get_result_price_text().text == self.product_price, "Стоимость с карточки товара и при заказе не совпадает"
        print("Стоимость с карточки товара и при заказе совпадает")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Заказ успешно оформлен")


    def result_buy_product(self):
        self.get_screenshot()
        self.copy_get_price_text()
        self.click_get_buy_product()
        self.assert_price_product()
        self.click_buy_button()
        self.get_screenshot()