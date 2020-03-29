from pages.base_page import BasePage
from locators import ProductAddingLocators
import time
from selenium.webdriver.common.action_chains import ActionChains





class AddingProducts(BasePage):

    def click_dresses(self):
        # dresses = self.driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_category=8&controller=category"][@title="Dresses"]')
        # Hover = ActionChains(self.driver).move_to_element(dresses)
        # Hover.perform()
        # time.sleep(10)
        #
        # self.driver.find_element(*ProductAddingLocators.evening_dress_BTN).click()  #tutaj odwołuje sie do nazwy klasy  zktó©ej jest mój lokator i po kropce podaję nazwę lokatora
        self.driver.find_element(*ProductAddingLocators.dresses_BTN).click()

    def click_evening_dresses(self):
        self.driver.find_element(*ProductAddingLocators.evening_dress_BTN).click()

    def hoover_on_img(self):
        Hover = ActionChains(self.driver).move_to_element(*ProductAddingLocators.dress_IMG)
        Hover.perform().click()
        time.sleep(5)

    def click_on_moore(self):
        self.driver.find_element(*ProductAddingLocators.more_BTN).click()

    def choose_size(self):
        self.driver.find_element(*ProductAddingLocators.size_M_hoover_BTN).click()
        self.driver.find_element(*ProductAddingLocators.size_M_BTN).click()

    def add_to_basket(self):
        self.driver.find_element(*ProductAddingLocators.add_BTN).click()

    def click_back_btn(self):

        self.driver.find_element(*ProductAddingLocators.continue_shopping_BTN).click()

    def click_tShirt(self):

        self.driver.find_element(*ProductAddingLocators.tShirt_BTN).click()

    def choose_short_sleeve(self):
        self.driver.find_element(*ProductAddingLocators.short_sleeve_BTN).click()

    def click_plus(self):
        self.driver.find_element(*ProductAddingLocators.plus_BTN).click()

    def add_to_basket2(self):

        self.driver.find_element(*ProductAddingLocators.add_BTN).click()

    def click_back_btn2(self):

        self.driver.find_element(*ProductAddingLocators.continue_shopping_BTN).click()

    def click_women_btn(self):
        self.driver.find_element(*ProductAddingLocators.women_BTN).click()

    def click_summer_dress(self):
        self.driver.find_element(*ProductAddingLocators.summer_DRESS_BTN).click()

    def choose_orange(self):
        self.driver.find_element(*ProductAddingLocators.orange_BTN).click()

    def choose_size_S(self):
        self.driver.find_element(*ProductAddingLocators.size_S_hoover_BTN).click()

    def add_to_basket3(self):
        self.driver.find_element(*ProductAddingLocators.submit_BTN).click()

    def click_checkout(self):
        self.driver.find_element(*ProductAddingLocators.checkout_BTN).click()












    #
    # def choose_size_38(self):
    #     # print("zamykam pojawiajązy się chat")  # założenie jest takie, żeby przed każðą akcją test sprawdzał czy czat działa i jeśli tak,to by go zamknął
    #     # hp = HomePage(self.driver)
    #     # hp.close_chat()
    #     #self.driver.find_element(*ProductAddingLocators.chat_BTN)
    #     self.driver.find_element(*ProductAddingLocators.size_38_BTN).click()
    #
    # def add_to_basket2(self):
    #     # print("zamykam pojawiajązy się chat")  # założenie jest takie, żeby przed każðą akcją test sprawdzał czy czat działa i jeśli tak,to by go zamknął
    #     # hp = HomePage(self.driver)
    #     # hp.close_chat()
    #     # print("srolluje do dołu strony")
    #     # ELEMENT = self.driver.find_element_by_xpath('//a[@id="gallery-fullscreen-btn"]')
    #     # ELEMENT.location_once_scrolled_into_view()  # srolluje do dołu strony takżeby przycisk dodania do koszyka był widoczn
    #     #
    #     # time.sleep(10)
    #
    #     #WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((ProductAddingLocators.add_to_cart_BTN)))
    #     print("Klikam dodaj do koszyka")
    #     self.driver.find_element(*ProductAddingLocators.add_to_cart_BTN).click()
    #
    # def click_back_btn2(self):
    #     # print("zamykam pojawiajązy się chat")  # założenie jest takie, żeby przed każðą akcją test sprawdzał czy czat działa i jeśli tak,to by go zamknął
    #     # hp = HomePage(self.driver)
    #     # hp.close_chat()
    #     # element2 = self.driver.find_element_by_xpath('//button[@class="action secondary"][@data-role="action"]')
    #     # element2.location_once_scrolled_into_view()
    #     # time.sleep(5)
    #     self.driver.find_element(*ProductAddingLocators.back_to_shopping_BTN2).click()
    #
    # def click_in_accesories(self):
    #     # print("zamykam pojawiajązy się chat")  # założenie jest takie, żeby przed każðą akcją test sprawdzał czy czat działa i jeśli tak,to by go zamknął
    #     # hp = HomePage(self.driver)
    #     # hp.close_chat()
    #     self.driver.find_element(*ProductAddingLocators.accesories_BTN).click()
    #
    # def choose_bracelet(self):
    #     # print("zamykam pojawiajązy się chat")  # założenie jest takie, żeby przed każðą akcją test sprawdzał czy czat działa i jeśli tak,to by go zamknął
    #     # hp = HomePage(self.driver)
    #     # hp.close_chat()
    #     #spróbuj zamienić lokatory dla bransoletki i zrobić tak jak ze swetrem
    #     bracelet = self.driver.find_element_by_xpath('//a[@href="https://quiosque.pl/bransoletka-5jd231304.html"][text()="BRANSOLETKA"]')  # dodaj do lokatorów jesli zadziała
    #     Hover3 = ActionChains(self.driver).move_to_element(bracelet)
    #     Hover3.perform()
    #     time.sleep(10)
    #     self.driver.find_element(*ProductAddingLocators.bracelet_BTN).click()  #na tym się wywala,najeżdza na napis sukienka a potem mówi że "ZOBACZ" jest nieklikalne
    #
    # def click_uni(self):
    #     # print("zamykam pojawiajązy się chat")  # założenie jest takie, żeby przed każðą akcją test sprawdzał czy czat działa i jeśli tak,to by go zamknął
    #     # hp = HomePage(self.driver)
    #     # hp.close_chat()
    #     self.driver.find_element(*ProductAddingLocators.uni_BTN).click()
    #
    # def add_to_basket3(self):
    #     # print("zamykam pojawiajązy się chat")  # założenie jest takie, żeby przed każðą akcją test sprawdzał czy czat działa i jeśli tak,to by go zamknął
    #     # hp = HomePage(self.driver)
    #     # hp.close_chat()
    #     # element3 = self.driver.find_element_by_xpath('//div[@id="option-label-size-139-item-1857"]') # scrolluje,żevt chat nie zasłaniała przycisku "dodaj do koszyka"
    #     # element3.location_once_scrolled_into_view
    #     # time.sleep(5)
    #     self.driver.find_element(*ProductAddingLocators.add_to_cart_BTN2).click()
    #
    # def click_register(self):
    #     # print("zamykam pojawiajązy się chat")  # założenie jest takie, żeby przed każðą akcją test sprawdzał czy czat działa i jeśli tak,to by go zamknął
    #     # hp = HomePage(self.driver)
    #     # hp.close_chat()
    #     self.driver.find_element(*ProductAddingLocators.register_BTN).click()
