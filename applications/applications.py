from pages.basepage import BasePage
from pages.loginpage import LoginPage
from pages.sidenavigationpage import SideNavigationPage
from pages.secondarylistingspage import SecondaryListingPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.basepage = BasePage(driver)
        self.loginpage = LoginPage(driver)
        self.sidenavigationpage = SideNavigationPage(driver)
        self.secondarylistingspage = SecondaryListingPage(driver)





