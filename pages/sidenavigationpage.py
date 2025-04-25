from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from time import sleep

class SideNavigationPage(BasePage):
    SECONDARY = (By.CSS_SELECTOR, "[href='/secondary-listings']")

    def click_secondary_button(self):
        self.wait_and_click(self.SECONDARY)









