import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('find and click characteristics button on item page')
def step(context):
    characteristics = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@href, '" + context.driver.current_url + "characteristics/')]"))
    )
    characteristics.click()


@then('click comments button on item page')
def step(context):
    context.driver.find_element(By.XPATH,
                                "//a[contains(@href, '" + context.driver.current_url + "comments/')]").click()
    time.sleep(2)
