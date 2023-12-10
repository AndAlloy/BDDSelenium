from behave import *
from selenium.webdriver.common.by import By


@when('input search text')
def step(context):
    context.driver.find_element(By.NAME, "search").send_keys("314213398")


@when('run search')
def step(context):
    context.driver.find_element(By.XPATH, "//form//button[contains(@class, 'button')]").click()
    context.driver.quit()
