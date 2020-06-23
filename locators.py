from selenium.webdriver.common.by import By




class ProductAddingLocators:

    scroll_to_img = (By.XPATH, '//form[@action="http://automationpractice.com/index.php?controller=products-comparison"]')

    evening_dress_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=10&controller=category"][@title="Evening Dresses"]')

    more_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_product=4&controller=product"][@title="View"]')

    size_M_hoover_BTN = (By.XPATH, '//div[@id="uniform-group_1"]')

    size_M_BTN = (By.XPATH, '//option[@title="M"]')

    add_BTN = (By.XPATH, '//button[@name="Submit"]')

    continue_shopping_BTN = (By.XPATH, '//span[@title="Continue shopping"]')

    tShirt_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=5&controller=category"]')

    short_sleeve_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_product=1&controller=product"]')

    more_BTN_2 = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_product=1&controller=product"][@class="button lnk_view btn btn-default"]')

    plus_BTN = (By.XPATH, '//a[@href="#"][@class="btn btn-default button-plus product_quantity_up"][@data-field-qty="qty"]')

    women_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=3&controller=category"]')

    more_BTN_3 = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_product=5&controller=product"][@itemprop="url"][@title="View"]')

    orange_BTN = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_product=5&controller=product"][@title="Orange"]')

    size_S_hoover_BTN = (By.XPATH, '//div[@id="uniform-group_1"]')

    size_L_BTN = (By.XPATH, '//option[@title="L"]')

    submit_BTN = (By.XPATH, '//button[@class="exclusive"][@type="submit"]')

    checkout_BTN = (By.XPATH, '//a[@title="Proceed to checkout"][@href="http://automationpractice.com/index.php?controller=order"]')


