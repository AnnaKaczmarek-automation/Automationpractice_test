from tests.base_test import BaseTest
from pages.product_adding_page import AddingProducts
import logging
import unittest


class ShoppingTest(BaseTest):
    def testCorrectProductAdding(self):

        print("rozpoczynam uruchamianie poszczególnych kroków testu, metodą należącą do klasy AddingProducts")
        ad = AddingProducts(self.driver)

        print("wchodzę w zakładke SUKIENKI)")
        ad.click_dresses()
        print('właczam podstronę z "evening dresses"')
        ad.click_evening_dresses()
        print('najeżdzam na zdjecie sukienki')
        ad.hoover_on_img()
        print('klikam "more"')
        ad.click_on_moore()
        print('wybieram rozmiar')
        ad.choose_size()
        print("asercja dla ceny i ilości sukienen wieczorowych")
        ad.assertion_evening_dress_price_and_amount()


        print("klikam w przycisk 't-shirt'")
        ad.click_tshirt()
        print("klikam w t-shirt")
        ad.choose_short_sleeve()
        print('zwiększam liczbę produktów')
        ad.click_plus()
        print("asercja dla ceny i ilości t-shirtów")
        ad.tShirt_price()


        print('klikam w zakłądkę "women"')
        ad.click_women_btn()
        print('wybieram letnią sukienkę')
        ad.click_summer_dress()
        print('wybieram kolor pomarańczowy')
        ad.choose_orange()
        print('wuybieram rozmiar S')
        ad.choose_size_s()
        print("asercja dla ceny,ilości i koloru sukienki letniej")
        ad.summerDressPrice()


    logging.basicConfig(filename="//home/tester/Dokumenty/Ania/projekt na zaliczenie//test.log",
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%Y/%m/%d %I:%M:%S %p')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    logger.debug("This is debug message")
    logger.info("This is info message")
    logger.warning("This is warning message")
    logger.error("This is error message")
    logger.critical("This is critical message")




    def tearDown(self):
        self.driver.quit()
if "__name__" == "__main__":
    unittest.main()
