import behave_webdriver
from behave_webdriver.steps import *

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome()  # Use `context.behave_driver`

def after_all(context):
    context.behave_driver.quit()