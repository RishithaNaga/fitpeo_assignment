from selenium import webdriver

from com.fitpeo.exceptions.valuemismatchexception import ValueMismatchException
from com.fitpeo.pages.homepage import HomePage
from com.fitpeo.pages.revenuecalculatorpage import RevenueCalculatorPage

# STEP 1 - Open Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Create Page Objects
home_page = HomePage(driver)
revenue_calculator_page = RevenueCalculatorPage(driver)

try:
    # STEP 2 - Launch Application URL (Already done in open_browser method)
    driver.get('https://www.fitpeo.com/')

    # STEP 3 - Navigate To Revenue Calculator Page
    home_page.navigate_to_revenue_calculator()

    # STEP 4 - Type into text field and verify slider percentage
    revenue_calculator_page.type_in_slider_text_field(560)
    revenue_calculator_page.verify_slider_percentage(560)

    # STEP 5 - Move slider and verify slider percentage
    revenue_calculator_page.move_slider_to(820)
    revenue_calculator_page.verify_slider_percentage(820)

    # STEP 6 - Check CPT checkboxes
    revenue_calculator_page.check_cpt_checkbox('CPT-99091', True)
    revenue_calculator_page.check_cpt_checkbox('CPT-99453', True)
    revenue_calculator_page.check_cpt_checkbox('CPT-99454', True)
    revenue_calculator_page.check_cpt_checkbox('CPT-99474', True)

    # STEP 7 - Verify Total Recurring Per Month
    revenue_calculator_page.verify_total_recurring_reimbursement_per_month('$110700')

except ValueMismatchException as e:
    print(f"Error: {e}")
finally:
    driver.quit()
