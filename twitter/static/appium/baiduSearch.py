from selenium import  webdriver

driver = webdriver.Chrome(r'D:\tools\webdrivers\chromedriver.exe')
driver.implicitly_wait(10)
def Open():
    driver.get('https://www.baidu.com')
    return
def query(kewwords):
    driver.find_element_by_css_selector('#kw').send_keys(kewwords)
    driver.find_element_by_css_selector('#su').click()
def clear():
    driver.find_element_by_css_selector('#kw').clear()