from tests.base_test import BaseTest
from pages.product_adding_page import AddingProducts
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
        print("klikam 'add to card'")
        ad.add_to_basket()
        print("klikam przycisk 'continue shopping'")
        ad.click_back_btn()



        print("klikam w przycisk 't-shirt'")
        ad.click_tShirt()
        print("klikam w t-shirt")
        ad.choose_short_sleeve()
        print('zwiększam liczbę produktów')
        ad.click_plus()
        print("klikam 'add to card'")
        ad.add_to_basket2()
        print("klikam przycisk 'continue shopping'")
        ad.click_back_btn2()



        print('klikam w zakłądkę "women"')
        ad.click_women_btn()
        print('wybieram letnią sukienkę')
        ad.click_summer_dress()
        print('wybieram kolor pomarańczowy')
        ad.choose_orange()
        print('wuybieram rozmiar S')
        ad.choose_size_S()
        print('klikam "add to basket"')
        ad.add_to_basket3()
        print('klikam "checkout"')
        ad.click_checkout()




    def tearDown(self):
        self.driver.quit()
if "__name__" == "__main__":
    unittest.main()
