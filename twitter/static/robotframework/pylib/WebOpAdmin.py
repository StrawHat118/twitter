#coding=utf-8
from selenium import  webdriver
from selenium.webdriver.support.ui import Select
# import config.cfg
import  cfg
import time

class WebOpAdmin():
    #中文
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'



    def SetupWebTests(self,driverType='chrome'):
        if driverType == 'chrome':
            self.cur_wd = webdriver.Chrome()
        elif driverType == 'firefox':
            self.cur_wd = webdriver.Firefox()
        else:
            raise Exception('unknow type of webdriver %s'% driverType)
        self.cur_wd.implicitly_wait(2)

    def TeardownWebs(self):
        self.cur_wd.quit()

    # def LoginWebSites(self,username,password):
    #     self.cur_wd.get(cfg.MgrLoginUrl)
    #     self.cur_wd.find_element_by_id('username').send_keys(username)
    #     self.cur_wd.find_element_by_id('password').send_keys(password)
    #     self.cur_wd.find_element_by_tag_name('button').click()


    def LoginWebSite(self):
        self.cur_wd.get('https://escrowcrm1.tourongjia.com/')
        self.cur_wd.find_element_by_css_selector('#userNo').send_keys("zhangchong")
        self.cur_wd.find_element_by_css_selector('#pwd').send_keys("888888x")
        self.cur_wd.find_element_by_css_selector('#login_btn').click()

    def login_test(self):
        self.cur_wd.get('https://escrowcrm1.tourongjia.com/')
        self.cur_wd.find_element_by_css_selector('#userNo').send_keys("zhangchong")
        self.cur_wd.find_element_by_css_selector('#pwd').send_keys("888888x")
        self.cur_wd.find_element_by_css_selector('#login_btn').click()



    def through_menu_test(self):
        self.cur_wd.find_element_by_css_selector(
            '#menuGroup > div:nth-child(3) > div.panel-header.accordion-header > div.panel-tool > div').click()
        self.cur_wd.find_element_by_css_selector('#menu185 > li:nth-child(1) > div > span.tree-title').click()
        self.cur_wd.switch_to.frame('work_frame')

    def DeleteAll(self,objName):
        if objName == 'course':
            self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        if objName == 'teacher':
            self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        time.sleep(2)

        while True:
            delButton = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')
            if delButton == []:
                break

            delButton[0].click()
            time.sleep(1)

            self.cur_wd.find_element_by_css_selector('.modal-footer .btn-primary').click()
            time.sleep(1)

    # def DeleteAllTeacher(self):
    #     self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]')
    #     while True:
    #         delButton = self.cur_wd.find_element_by_css_selector('*[ng-click^=delOne]')
    #         if delButton == []:
    #             break
    #
    #         delButton[0].click()
    #         self.cur_wd.find_element_by_css_selector('.modal-footer .btn-primary').click()
    #         time.sleep(1)

    def addTeachers(self,realname,username,desc,idx,lesson):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        time.sleep(1)

        self.cur_wd.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(realname)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(username)

        ele = self.cur_wd.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        ele = Select(self.cur_wd.find_element_by_css_selector("select[ng-model*=courseSelected]"))
        ele.select_by_visible_text(lesson)
        self.cur_wd.find_element_by_css_selector("button[ng-click='addOne()']").click()
        time.sleep(1)

    def addCourses(self,name,desc,idx):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        time.sleep(1)

        self.cur_wd.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addData.name']")
        ele.clear()
        ele.send_keys(name)

        ele = self.cur_wd.find_element_by_css_selector("textarea[ng-model='addData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        self.cur_wd.find_element_by_css_selector("button[ng-click='addOne()']").click()
        time.sleep(1)

    def getTeacherList(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ui-sref=teacher]")
        time.sleep(1)

        eles = self.cur_wd.find_elements_by_css_selector("tr>td:nth-child(2)")
        return [ele.text for ele in eles]

    def getCourseList(self):
        self.cur_wd.find_element_by_css_selector("ul.nav a[ui-sref=course]")
        time.sleep(1)

        eles = self.cur_wd.find_elements_by_css_selector("tr>td:nth-child(2)")
        return [ele.text for ele in eles]

