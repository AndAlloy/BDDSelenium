from behave import *
from selenium.webdriver.common.by import By


@when('switch website language')
def step(context):
    assert context.driver.current_url == "https://rozetka.com.ua/ua/"
    context.driver.find_element(By.XPATH, "//a[contains(@class, 'lang__link')]").click()
    assert context.driver.current_url == "https://rozetka.com.ua/"


@then('assert current language')
def step(context):
    assert context.driver.current_url == "https://rozetka.com.ua/"
