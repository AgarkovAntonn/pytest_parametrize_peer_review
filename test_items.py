import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_can_see_add_to_cart_button(browser):
	browser.get(link)
	#time.sleep(30)
	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	
	try:
		button = browser.find_element_by_css_selector("button.btn-add-to-basket")
		button.click()
	except Exception:
		button = None
	assert button is not None, "There is no 'Add to cart' button"
	
	