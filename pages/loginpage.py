from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR,"#email-2")
    PASSWORD = (By.CSS_SELECTOR,"#field")
    CONTINUE = (By.CSS_SELECTOR, "[wized='loginButton']")


    def open_reelly_url(self):
        self.open_url("https://soft.reelly.io/sign-in")

    def input_email(self):
        self.input_text("***",*self.EMAIL)

    def input_password(self):
        self.input_text("****",*self.PASSWORD)

    def click_continue(self):
        self.click(*self.CONTINUE)
        sleep(5)






