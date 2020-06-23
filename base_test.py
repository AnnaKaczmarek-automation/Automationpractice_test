from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()


if "__name__" == "__main__":
    unittest.main()
