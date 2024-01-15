from selenium.webdriver.common.by import By
import time

def test_add_to_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    try:
        item = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    except:
        item = None
    assert item, 'The "Add to basket" button not found'
    