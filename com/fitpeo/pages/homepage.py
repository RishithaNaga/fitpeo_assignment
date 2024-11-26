from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.fitpeo.com/"


    def navigate_to_revenue_calculator(self):
        self.driver.find_element(By.XPATH, '//button[@aria-label="open drawer"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Revenue Calculator"]').click()

    def navig(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
