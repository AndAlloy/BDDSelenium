from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@when('open sort dropdown')
def step(context):
    dropdown = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[contains(@class, 'select-css')]"))
    )
    dropdown.click()


@when('select sort option = "{needed_option}"')
def step(context, needed_option):
    dropdown = context.driver.find_element(By.XPATH, "//select[contains(@class, 'select-css')]")
    select = Select(dropdown)
    select.select_by_visible_text(needed_option)


@then('check sort option = "{expected_option}"')
def step_then_verify_selection(context, expected_option):
    dropdown = context.driver.find_element(By.XPATH, "//select[contains(@class, 'select-css')]")
    select = Select(dropdown)
    selected_option = select.first_selected_option.text
    assert selected_option == expected_option
