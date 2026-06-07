import time
import undetected_chromedriver as uc

from pages.buy_page import Buy_page
from pages.fIlter_page import Filter_page
from pages.main_page import Main_page
from pages.sorted_page import Sorted_page


def test_change_headphones():
    driver = uc.Chrome()

    print("Start test 1")
    mp = Main_page(driver)
    mp.change_headphones()
    hp = Filter_page(driver, "SONY")
    hp.change_filters()
    sp = Sorted_page(driver)
    sp.search_headphones("SONY", "WH-1000XM6")
    bp = Buy_page(driver)
    bp.result_buy_product()
    time.sleep(10)