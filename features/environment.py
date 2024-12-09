import behave_webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    context.behave_driver = behave_webdriver.Chrome(options=chrome_options)

def after_all(context):
    if hasattr(context, 'behave_driver'):
        context.behave_driver.quit()