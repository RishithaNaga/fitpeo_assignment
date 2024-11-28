from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

class HomePage:
    button_menu_xpath='//button[@aria-label="open drawer"]'
    button_revenuecalculator_xpath='//span[text()="Revenue Calculator"]'


    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.fitpeo.com/"


    def navigate_to_revenue_calculator(self):
        self.driver.find_element(By.XPATH,HomePage.button_menu_xpath ).click()
        self.driver.find_element(By.XPATH,HomePage.button_revenuecalculator_xpath ).click()

    def navig(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
