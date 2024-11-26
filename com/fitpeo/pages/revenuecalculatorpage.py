from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from com.fitpeo.exceptions.valuemismatchexception import ValueMismatchException


class RevenueCalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def type_in_slider_text_field(self, number):
        slider_text_field_element = self.driver.find_element(By.XPATH, '//input[@aria-invalid="false"]')
        slider_text_field_element.click()
        for _ in range(4):
            slider_text_field_element.send_keys(Keys.BACKSPACE)
        slider_text_field_element.send_keys(number)

    def move_slider_to(self, number):
        slider_element = self.driver.find_element(By.XPATH, '//span[contains(@class, "MuiSlider-thumb")]')
        action = ActionChains(self.driver)
        action.click_and_hold(slider_element).perform()

        current_value_element = self.driver.find_element(By.XPATH, '//span[contains(@class, "MuiSlider-thumb")]/child::input')
        current_value = int(current_value_element.get_attribute('value'))

        key_to_press = Keys.RIGHT
        iterations = number - current_value
        if current_value > number:
            key_to_press = Keys.LEFT
            iterations = current_value - number

        for _ in range(iterations):
            action.send_keys(key_to_press).perform()

    def verify_slider_percentage(self, number):
        expected_percentage = (number * 100) / 2000
        slider_element = self.driver.find_element(By.XPATH, '//span[contains(@class, "MuiSlider-thumb")]')
        style_attr_value = slider_element.get_attribute('style')
        actual_percentage = float(style_attr_value.replace("left: ", "").replace("%;", "").strip())

        if actual_percentage != expected_percentage:
            raise ValueMismatchException(
                f'Slider Percentage is incorrect. Actual = {actual_percentage}%, Expected = {expected_percentage}%'
            )
        print('Slider Percentage is Correct - ', actual_percentage)

    def get_cpt_checkbox_locator(self, cpt_value):
        return f"//*[text()='{cpt_value}']/parent::*/descendant::input[@type='checkbox']"

    def is_cpt_checkbox_checked(self, cpt_value):
        class_value = self.driver.find_element(By.XPATH, self.get_cpt_checkbox_locator(cpt_value)).find_element(By.XPATH, './parent::*').get_attribute('class')
        return 'Mui-checked' in class_value

    def check_cpt_checkbox(self, cpt_value, check):
        is_checked = self.is_cpt_checkbox_checked(cpt_value)
        if check != is_checked:
            checkbox_element = self.driver.find_element(By.XPATH, self.get_cpt_checkbox_locator(cpt_value))
            checkbox_element.click()

    def verify_total_recurring_reimbursement_per_month(self, expected):
        actual = self.driver.find_element(By.XPATH, "//*[text()='Total Recurring Reimbursement for all Patients Per Month']/following-sibling::p").text
        if actual != expected:
            raise ValueMismatchException(
                f'Total Recurring Reimbursement Per Month is incorrect. Actual = {actual}, Expected = {expected}'
            )
        print('Total Revenue Gross Per Year is Success. Revenue = ' + actual)