from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self,*locator):
        self.driver.find_element(*locator).click()

    def wait_and_click(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator),message=f'Element by {locator} not clickable').click()


    def element_in_listing(self,all_products,product_element):
        self.driver.execute_script("window.scrollBy(0, 2000)")
        products = self.driver.find_elements(*all_products)
        for product in products:
            sales_tag = product.find_element(*product_element).text
            assert sales_tag in product, f'{sales_tag} not in {product}'
            print(product_element)


    def verify_partial_text(self,expected_text,*locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} but got {actual_text}'

    def verify_url(self,expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'{expected_url} != {actual_url}'



