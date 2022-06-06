import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SephoraCartTest(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.sephora.pl")
        self.wait = self.driver.implicitly_wait(10)

    def testPriceEqual(self):
        driver = self.driver
        wait = self.wait
        # zamykamy okno od ciasteczek
        driver.find_element(By.ID, "footer_tc_privacy_button_3").click()
        show_search_bar = driver.find_element(By.XPATH, "//div[@class='input-box js-open-search']")
        show_search_bar.click()
        wait
        search_bar = driver.find_element(By.ID, 'q')
        search_bar.clear()
        search_bar.send_keys('dolce Vita')
        search_bar.send_keys(Keys.RETURN)
        wait
        catalogue_price = driver.find_element(By.CLASS_NAME, 'product-price').text
        driver.find_element(By.ID, 'add-to-cart').click()
        wait
        driver.find_element(By.XPATH, "//a[@class='show-cart button']").click()
        wait
        price_in_cart = driver.find_element(By.XPATH, "//span[@class='product-sales-price price-sales-standard']").text
        summary_price = driver.find_element(By.XPATH, "//div[@class='cart-summary-row order-total']/div[2]").text
        self.assertEqual(catalogue_price, price_in_cart)
        self.assertEqual(catalogue_price, summary_price)

    def tearDown(self):
        self.driver.quit()
