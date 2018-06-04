#coding=utf-8
from appium import webdriver
import time,traceback
import baiduSearch
# import ci.static.appium.chongdingdahui.baidu
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'test'
desired_caps['appPackage'] = 'com.handsgo.jiakao.android'
desired_caps['appActivity'] = '.splash.Login'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
try:
    driver.implicitly_wait(1000)
    baiduSearch.Open()
    baiduSearch.clear()
    ele = driver.find_element_by_id("com.handsgo.jiakao.android:id/center_button")
    ele.click()
    raw_input('是否开始？')
    while True:
        ele1 = driver.find_element_by_id('com.handsgo.jiakao.android:id/practice_content_text')
        txt1 = ele1.text
        time.sleep(0.2)
        baiduSearch.query(txt1)
        print txt1
        time.sleep(0.2)
        baiduSearch.clear()
except:
    print traceback.format_exc()



