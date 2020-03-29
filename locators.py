from selenium.webdriver.common.by import By

# tutaj nie pisze na końcu .click() tylko w pliku w którym stworzę juz konkretne funkcje


class ProductAddingLocators:
# 1.kliknij w przycisk "sukienki"

    dresses_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=8&controller=category"][@title="Dresses"]')

# 2. kliknij w "EVENING DRESSES"


    evening_dress_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=10&controller=category"]')

    # 3.najedź myszką na zdjęcie sukienki
    dress_IMG = (By.XPATH, '//img[@src="http://automationpractice.com/img/p/1/0/10-home_default.jpg"]')

    #4. kliknij w przycisk "more"
    more_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_product=4&controller=product"]')
    #5. wybierz rozmiar M
    size_M_hoover_BTN = (By.XPATH, '//div[@id="uniform-group_1"]')
    size_M_BTN = (By.XPATH, '//option[@title="M"]')


    # 4.kliknij "dodaj do koszyka"

    add_BTN = (By.XPATH, '//button[@name="Submit"]')

    # 5.kliknij "wróć do zakupów"
    continue_shopping_BTN = (By.XPATH, '//span[@title="Continue shopping"]')


    # 6.kliknij w "t-shirt"

    tShirt_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=5&controller=category"]')

    short_sleeve_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_product=1&controller=product"]')
    #kliknij w znacznik '+' zwiekszający ilośc produktów
    plus_BTN = (By.CLASS_NAME, "icon-plus")

    women_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=3&controller=category"]')

    summer_DRESS_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_product=5&controller=product"][@title="Printed Summer Dress"]')

    orange_BTN = (By.ID, 'id="color_13"')

    size_S_hoover_BTN = (By.ID, 'id="uniform-group_1"')

    submit_BTN = (By.XPATH, '//button[@type="submit"]')

    checkout_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?controller=order"][@class="btn btn-default button button-medium"]')







    # 7.kliknij w "różowy sweter z ozdobną krawatką" #zmienić nazwe na rózowy sweter
    hoodie_BTN = (By.XPATH, '//a[@href="https://quiosque.pl/szara-wygodna-bluza-z-kapturem-na-zamek-6jf002240.html"][text()="Szara wygodna bluza z kapturem na zamek"]')
    #yellow_sweater_BTN = (By.XPATH, '//a[@href="https://quiosque.pl/zolty-sweter-z-ozdobna-krawatka-6ih004302.html"]')

    # 8.wybierz rozmiar 38

    size_38_BTN = (By.XPATH, '//div[@id="option-label-size-139-item-8"]')

    # 9.kliknij "dodaj do koszyka"   # tu śię wywala, niby nieklikalny element

    #add_to_cart_BTN = (By.XPATH, '/html/body/div[2]/main/div[2]/div/div[1]/div[5]/form/div[2]/div/div/div[2]/button')
    add_to_cart_BTN = (By.XPATH, '//button[@id="product-addtocart-button"]')
    #add_to_cart_BTN = (By.XPATH, '//*[@id="product-addtocart-button"]')
    #add_to_cart_BTN = (By.XPATH, '//button[@data-configurable="1"][@data-id="6JA001500"][@id="product-addtocart-button"]')

    #spróboj webDriwerWait!!!!!


    # 10.kliknij"wróć do zakupów"

    back_to_shopping_BTN2 = (By.XPATH, '//button[@class="action secondary"][@data-role="action"]')

    # 11.kliknij w "akcesoria"

    accesories_BTN = (By.XPATH, '//a[@href="https://quiosque.pl/dodatki-i-akcesoria.html"]')

    # 12.kliknij w "bransoletka typu pandora ze srebrną gwiazdką"

    bracelet_BTN = (By.XPATH, '//a[@href="https://quiosque.pl/bransoletka-5jd231304.html"]')

    # 13.wybierz "uni"

    uni_BTN = (By.XPATH, '//div[@id="option-label-size-139-item-1857"]')

    # 14.kliknij "dodaj do koszyka"

    add_to_cart_BTN2 = (By.XPATH, '//button[@id="product-addtocart-button"]')

    # 15.kliknij"do kasy"

    register_BTN = (By.XPATH, '//button[@class="action primary"][@data-role="action"]')

    #shipping_BTN = (By.XPATH, '//a[@id="tab-label-shipping-title"]')

    #full_screen_BTN = (By.XPATH, '//a[@id="gallery-fullscreen-btn"]')

class HomePageLocators:
    NEWSLETTER_X = (By.ID, "sc_close")
    #ACCEPTANCE_BTN = (By.XPATH, '//a[@id="hide-button"]')
    ACCEPTANCE_BTN = (By.XPATH, '/html/body/div[1]/div/a')
