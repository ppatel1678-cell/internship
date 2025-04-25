from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SecondaryListingPage(BasePage):

    FILTERS = (By.CSS_SELECTOR, "div.filter-button")
    SIDE_POP = (By.CSS_SELECTOR, "[wized='filtersWindow']")
    SELL = (By.CSS_SELECTOR, "[wized='ListingTypeSell']")
    APPLY_FILTER = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    WHOLE_LISTING = (By.CSS_SELECTOR, "[wized='listingCardMLS']")
    SALE_TAG = (By.CSS_SELECTOR, "[wized='saleTagMLS']")

    def verify_secondary_url(self):
        self.verify_url("https://soft.reelly.io/secondary-listings")


    def click_filters_button(self):
        self.wait_and_click(self.FILTERS)


    def wait_for_side_nav(self):
        self.wait.until(EC.visibility_of_element_located(self.SIDE_POP))


    def want_to_sell_button(self):
        self.wait_and_click(self.SELL)


    def apply_filter_button(self):
        self.wait_and_click(self.APPLY_FILTER)


    def verify_for_sale_tag(self):
        self.element_in_listing(self.WHOLE_LISTING,self.SALE_TAG)









