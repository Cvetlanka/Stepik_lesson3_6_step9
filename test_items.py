import selenium.common.exceptions
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_basket_available(browser):
    browser.get(link)
#    time.sleep(30)      # для рецензента
    try:
        btn_basket = browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button")
    except:
        btn_basket = False

    assert btn_basket, "Button for basket not found!"

