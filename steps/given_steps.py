from behave import *
from selenium import webdriver


@given('launch chrome browser with website')
def step(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://rozetka.com.ua/")


@given('launch chrome browser with laptops category')
def step(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://rozetka.com.ua/notebooks/c80004/")


@given('launch chrome browser with suburl = "{sub_url}"')
def step(context, sub_url):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://rozetka.com.ua/" + sub_url)
