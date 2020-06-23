from pages.base_page import BasePage
from locators import ProductAddingLocators
import time
from selenium.webdriver.common.action_chains import ActionChains


class AddingProducts(BasePage):

    def click_dresses(self):

        women_btn = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_category=3&controller=category"]')
        Hover = ActionChains(self.driver).move_to_element(women_btn)
        Hover.perform()
        time.sleep(8)

    def click_evening_dresses(self):

        evening_btn = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_category=10&controller=category"][@title="Evening Dresses"]')
        Hover = ActionChains(self.driver).move_to_element(evening_btn)
        Hover.perform()
        time.sleep(8)
        self.driver.find_element(*ProductAddingLocators.evening_dress_BTN).click()
        time.sleep(5)

    def hoover_on_img(self):

        scroll = self.driver.find_element(*ProductAddingLocators.scroll_to_img)
        scroll.location_once_scrolled_into_view
        image = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_product=4&controller=product"][@title="Printed Dress"]')
        Hover = ActionChains(self.driver).move_to_element(image)
        Hover.perform()
        time.sleep(8)


    def click_on_moore(self):

        more = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_product=4&controller=product"]')
        Hover = ActionChains(self.driver).move_to_element(more)
        Hover.perform()
        time.sleep(8)
        self.driver.find_element(*ProductAddingLocators.more_BTN).click()
        time.sleep(3)


    def choose_size(self):

        self.driver.find_element(*ProductAddingLocators.size_M_hoover_BTN).click()
        self.driver.find_element(*ProductAddingLocators.size_M_BTN).click()
        time.sleep(3)


    def assertion_evening_dress_price_and_amount(self):

        dress_price = self.driver.find_element_by_xpath('//span[@id="our_price_display"][@itemprop="price"][text() ="$50.99"]')
        evening_dress_price = dress_price.get_attribute("innerText")
        evening_dress_price2 = evening_dress_price.replace('$', '')
        dress_price2 = float(evening_dress_price2)

        dress_amount = self.driver.find_element_by_xpath('//input[@id="quantity_wanted"]')
        evening_dress_amount = dress_amount.get_attribute("innerText")

        print('klikam w "add to bascet"')
        self.driver.find_element(*ProductAddingLocators.add_BTN).click()
        time.sleep(3)

        print('klikam w "Proceed to checkout"')
        self.driver.find_element_by_xpath('//a[@title="Proceed to checkout"]').click()

        dress_price_in_result = self.driver.find_element_by_xpath('//span[@id="total_product_price_4_17_0"]')
        evening_Dress_in_result = dress_price_in_result.get_attribute("innerText")
        print(evening_Dress_in_result)
        evening_Dress_in_result2 = evening_Dress_in_result.replace('$', '')
        Dress_in_result = float(evening_Dress_in_result2)
        print(Dress_in_result)


        dress_amount_in_result = self.driver.find_element_by_xpath('//input[@class="cart_quantity_input form-control grey"][@name="quantity_4_17_0_0"]')
        evening_Dress_amount_in_result = dress_amount_in_result.get_attribute("innerText")

        assert dress_price2 == Dress_in_result
        assert evening_dress_amount == evening_Dress_amount_in_result

        print("wracam do kontynuacji zakupów")
        self.driver.find_element_by_xpath('//a[@title="Continue shopping"]').click()


    def click_tshirt(self):

        print("najedż na przycisk WOMEN")
        women_btn = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_category=3&controller=category"]')
        Hover = ActionChains(self.driver).move_to_element(women_btn)
        Hover.perform()
        time.sleep(10)

        self.driver.find_element(*ProductAddingLocators.tShirt_BTN).click()
        time.sleep(3)

    def choose_short_sleeve(self):

        print('najedż na napis pod produktem')
        title = self.driver.find_element_by_xpath('//a[@title="Faded Short Sleeve T-shirts"]')
        Hover = ActionChains(self.driver).move_to_element(title)
        Hover.perform()
        time.sleep(8)
        print('najedź na przycisk MORE')
        more = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_product=1&controller=product"][@class="button lnk_view btn btn-default"]')
        Hover = ActionChains(self.driver).move_to_element(more)
        Hover.perform()
        time.sleep(8)
        print('kliknij w przycisk MORE')
        self.driver.find_element(*ProductAddingLocators.more_BTN_2).click()
        time.sleep(3)

    def click_plus(self):

        print('kliknij na przycisk "+"')
        self.driver.find_element(*ProductAddingLocators.plus_BTN).click()

    def tShirt_price(self):
        print("pobieram tekst ceny dla t-shirtu")
        tPrice = self.driver.find_element_by_xpath('//span[@id="our_price_display"][text()="$16.51"]')
        tShirt_price = tPrice.get_attribute('innerText')
        tShirt_price2 = tShirt_price.replace('$', '')
        t_price = float(tShirt_price2)*2


        print("pobieram tekst dla ilości produktów dla t-shirtu")
        tAmount = self.driver.find_element_by_xpath('//input[@id="quantity_wanted"]')
        tShirt_amount = tAmount.get_attribute("innerText")

        print("klikad w add to bascet")
        self.driver.find_element(*ProductAddingLocators.add_BTN).click()
        time.sleep(3)

        print('klikam w "Proceed to checkout"')
        self.driver.find_element_by_xpath('//a[@title="Proceed to checkout"]').click()

        print("pobieram tekst ceny dla t-shirtaw koszyku")
        tPrice_in_result = self.driver.find_element_by_xpath('//span[@id="total_product_price_1_1_0"]')
        tShirt_price_in_result = tPrice_in_result.get_attribute("innerText")
        tShirt_price_in_result2 = tShirt_price_in_result.replace('$', '')
        t_price_in_result = float(tShirt_price_in_result2)

        print("pobieram tekst dla ilości produktów w koszyku")
        tAmount_in_result = self.driver.find_element_by_xpath('//input[@class="cart_quantity_input form-control grey"][@name="quantity_1_1_0_0"]')
        tShirt_amount_in_result = tAmount_in_result.get_attribute("innerText")


        assert t_price == t_price_in_result
        assert tShirt_amount == tShirt_amount_in_result

        print("wracam do kontynuacji zakupów")
        self.driver.find_element_by_xpath('//a[@title="Continue shopping"]').click()

    def click_women_btn(self):
        print('kliknij w przycisk WOMEN')
        self.driver.find_element(*ProductAddingLocators.women_BTN).click()

    def click_summer_dress(self):

        print('najedż na napis pod produktem')
        title = self.driver.find_element_by_xpath('//a[@title="Printed Summer Dress"]')
        time.sleep(5)
        Hover = ActionChains(self.driver).move_to_element(title)
        Hover.perform()
        time.sleep(10)
        print('najedź na przycisk MORE')
        more = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_product=5&controller=product"][@class="button lnk_view btn btn-default"]')
        Hover = ActionChains(self.driver).move_to_element(more)
        Hover.perform()
        time.sleep(8)
        self.driver.find_element(*ProductAddingLocators.more_BTN_3).click()
        time.sleep(3)

    def choose_orange(self):

        self.driver.find_element(*ProductAddingLocators.orange_BTN).click()

    def choose_size_s(self):

        print('najeżdzam na wybór rozmiarów')
        self.driver.find_element(*ProductAddingLocators.size_S_hoover_BTN).click()
        time.sleep(3)
        print('najeżdzam na rozmiar L')
        self.driver.find_element(*ProductAddingLocators.size_L_BTN).click()
        time.sleep(5)


    def summerDressPrice(self):
        print("pobieram tekst ceny dla sukienki letniej")
        s_dress_price = self.driver.find_element_by_xpath('//span[@id="our_price_display"]')
        summer_dress_price = s_dress_price.get_attribute("innerText")
        summer_dress_price2 = summer_dress_price.replace('$', '')
        summer_price = float(summer_dress_price2)

        print("pobieram tekst dla liczby produktów")
        s_dress_amount = self.driver.find_element_by_xpath('//input[@id="quantity_wanted"]')
        summer_dress_amount = s_dress_amount.get_attribute("innerText")

        print("pobieram tekst dla koloru sukienki")
        colour = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_product=5&controller=product"][@id="color_13"]')
        colour_box = colour.get_attribute("title")
        print(colour_box)

        print("klikam w add to bascet")
        self.driver.find_element(*ProductAddingLocators.add_BTN).click()
        time.sleep(3)

        print('klikam w "Proceed to checkout"')
        self.driver.find_element_by_xpath('//a[@title="Proceed to checkout"]').click()

        print("pobieram tekst dla liczby produktów w koszyku")
        s_dress_amount_in_result = self.driver.find_element_by_xpath('//input[@name="quantity_5_29_0_0"]')
        summer_dress_amount_in_result = s_dress_amount_in_result.get_attribute("innerText")

        print("pobieram tekst dla ceny sukienki w koszyku")
        s_dress_price_in_result = self.driver.find_element_by_xpath('//span[@id="total_product_price_5_29_0"]')
        summer_dress_price_in_result = s_dress_price_in_result.get_attribute("innerText")
        summer_dress_price_in_result2 = summer_dress_price_in_result.replace('$','')
        summer_price_in_result = float(summer_dress_price_in_result2)

        print("pobieram tekst dla koloru sukienki w koszyku")
        colour_in_result = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_product=5&controller=product#/size-l/color-orange"][text()="Color : Orange, Size : L"]')
        colour_box_in_result = colour_in_result.get_attribute("innerText")
        print(colour_box_in_result)
        colour_box_in_result2 = colour_box_in_result.replace('Color : ', '')
        colour_box_in_result3 = colour_box_in_result2.replace(', Size : L','')
        print(colour_box_in_result3)

        assert summer_price == summer_price_in_result
        assert summer_dress_amount == summer_dress_amount_in_result
        assert colour_box == colour_box_in_result3

