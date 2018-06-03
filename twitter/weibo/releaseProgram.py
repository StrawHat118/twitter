#coding=utf-8
from selenium import webdriver
from twitter import settings
import time
import datetime
class ReleaseProgram():
    def open_browser(self,driverType='chrome'):
        if driverType == 'chrome':
            self.driver = webdriver.Chrome(executable_path=settings.executable_path)
            self.driver.implicitly_wait(10)
    def login(self,url):
        self.driver.get(url)
        # 输入账号
        self.driver.find_element_by_css_selector('#userNo').send_keys("liuchang")
        # 输入密码
        self.driver.find_element_by_css_selector('#pwd').send_keys("trj888888")
        # 点击登录
        self.driver.find_element_by_css_selector('#login_btn').click()



    def release_program(self,config_num, config_type):

        config_num_css ='#cb_dataTable_{}'.format(config_num)
        config_type_css = 'body > div.func_tool_area > a:nth-child({}) > span > span'.format(config_type)

        # driver.get('http://jrtestadm.tourongjia.com/')


        #点击 项目运营
        self.driver.find_element_by_css_selector('#menuGroup > div:nth-child(9) > div.panel-header.accordion-header > div.panel-title').click()
        #点击快速发标
        self.driver.find_element_by_css_selector('#menu181 > li:nth-child(16) > div').click()
        #进入 frame
        self.driver.switch_to.frame('work_frame')
        #选中 投融宝365天
        self.driver.find_element_by_css_selector(config_num_css).click()
        #点击 发集合标
        self.driver.find_element_by_css_selector(config_type_css).click()
        #点击确定
        self.driver.find_element_by_css_selector('body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span').click()
    def choice_release_one(self):
        #选中第一个合同
        self.driver.find_element_by_css_selector('#cb_borrowerDataTable_0').click()
    def choice_release_two(self):
        #选中第二个合同
        self.driver.find_element_by_css_selector('#cb_borrowerDataTable_1').click()
    def choice_release_three(self):
        # #选中第三个合同
        self.driver.find_element_by_css_selector('#cb_borrowerDataTable_2').click()
    def choice_release_four(self):
        #选中第4/5个合同
        self.driver.find_element_by_css_selector('#cb_borrowerDataTable_3').click()
    def choice_release_five(self):
        self.driver.find_element_by_css_selector('#cb_borrowerDataTable_4').click()
    def choice_release_six(self):
        self.driver.find_element_by_css_selector('#cb_borrowerDataTable_5').click()
    def audit(self,end_time):
        addShowTime = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
        addBeginTime = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
        addEndTime = (datetime.datetime.now() + datetime.timedelta(days=end_time)).strftime("%Y-%m-%d %H:%M:%S")

        #点击发布
        self.driver.find_element_by_css_selector('#borrowerChooser > div.win_tool_area > a:nth-child(1) > span > span').click()
        time.sleep(2)
        #点击确定
        self.driver.find_element_by_css_selector('body > div:nth-child(17) > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a').click()
        #返回主frame
        self.driver.switch_to.default_content()
        #点击 快速发标审核
        self.driver.find_element_by_css_selector('#menu181 > li:nth-child(17) > div > span.tree-title').click()
        #进入frame
        self.driver.switch_to.frame('work_frame')
        #选中第一个项目
        time.sleep(1)
        self.driver.find_element_by_css_selector('#cb_dataTable_0').click()
        #点击 审核
        self.driver.find_element_by_css_selector('body > div.func_tool_area > a:nth-child(1) > span > span').click()
        time.sleep(1)

        #清空原有的发标时间
        self.driver.find_element_by_css_selector('#showBidTime').clear()
        #输入发标时间
        self.driver.find_element_by_css_selector('#showBidTime').send_keys(addShowTime)
        #清空原有的开标时间
        self.driver.find_element_by_css_selector('#startBidTime').clear()
        #输入开标时间
        self.driver.find_element_by_css_selector('#startBidTime').send_keys(addBeginTime)
        #清空截标时间
        self.driver.find_element_by_css_selector('#endBidTime').clear()
        #输入截标时间
        self.driver.find_element_by_css_selector('#endBidTime').send_keys(addEndTime)
    def child_information(self):
        # 点击 子标信息信息
        self.driver.find_element_by_css_selector(
            '#tt > div.tabs-header > div.tabs-wrap > ul > li:nth-child(2) > a > span.tabs-title').click()
    def choice_audit_one(self):
        # 选中第一个合同
        self.driver.find_element_by_css_selector('#cb_dataTable_0').click()
    def choice_audit_two(self):
        # 选中第二个合同
        self.driver.find_element_by_css_selector('#cb_dataTable_1').click()
    def choice_audit_three(self):
        # 选中第三个合同
        self.driver.find_element_by_css_selector('#cb_dataTable_2').click()
    def choice_audit_four(self):
        # #选中di4/5个合同
        self.driver.find_element_by_css_selector('#cb_dataTable_3').click()
    def choice_audit_five(self):
        self.driver.find_element_by_css_selector('#cb_dataTable_4').click()
    def choice_audit_six(self):
        self.driver.find_element_by_css_selector('#cb_dataTable_5').click()
        # 点击 子标审核通过
    def audit_access_child(self):
        self.driver.find_element_by_css_selector('#doAudit > span > span').click()
        # 点击 确定
        self.driver.find_element_by_css_selector(
            'body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span').click()
        time.sleep(1)
        self.driver.close()
    def audit_access_collect(self):
        self.driver.find_element_by_css_selector('#doPrjAudit > span > span').click()
        # 点击 确定
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            'body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            'body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span').click()

        #点击 集合标审核通过
        self.driver.find_element_by_css_selector('#doCollectAudit > span > span').click()
        self.driver.find_element_by_css_selector('body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span').click()
        time.sleep(1)
        self.driver.close()

    # def release_proagram_yw(config_num,end_time):
    #     driver = webdriver.Chrome(executable_path=settings.executable_path)
    #     driver.implicitly_wait(10)
    #     config_num_css = '#cb_dataTable_{}'.format(config_num)
    #     addShowTime = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    #     addBeginTime = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
    #     addEndTime = (datetime.datetime.now() + datetime.timedelta(days=end_time)).strftime("%Y-%m-%d %H:%M:%S")
    #     driver.get('http://jrtestadm.tourongjia.com/')
    #
    #     # 输入账号
    #     driver.find_element_by_css_selector('#userNo').send_keys("liuchang")
    #     # 输入密码
    #     driver.find_element_by_css_selector('#pwd').send_keys("trj888888")
    #     # 点击登录
    #     driver.find_element_by_css_selector('#login_btn').click()
    #     # 点击 项目运营
    #     driver.find_element_by_css_selector(
    #         '#menuGroup > div:nth-child(9) > div.panel-header.accordion-header > div.panel-title').click()
    #     # 点击快速发标
    #     driver.find_element_by_css_selector('#menu181 > li:nth-child(16) > div').click()
    #     # 进入 frame
    #     driver.switch_to.frame('work_frame')
    #     # 选中 投融宝365天
    #     driver.find_element_by_css_selector(config_num_css).click()
    #     # 点击 发集合标
    #     driver.find_element_by_css_selector('body > div.func_tool_area > a:nth-child(2) > span > span').click()
    #     # 点击确定
    #     driver.find_element_by_css_selector(
    #         'body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span').click()
    #     # 选中第一个合同
    #     driver.find_element_by_css_selector('#cb_borrowerDataTable_0').click()
    #     # # 选中第二个合同
    #     driver.find_element_by_css_selector('#cb_borrowerDataTable_1').click()
    #     # # 选中第三个合同
    #     # driver.find_element_by_css_selector('#cb_borrowerDataTable_2').click()
    #     # 选中第4/5个合同
    #     # driver.find_element_by_css_selector('#cb_borrowerDataTable_3').click()
    #     # driver.find_element_by_css_selector('#cb_borrowerDataTable_4').click()
    #
    #     # 点击发布
    #     driver.find_element_by_css_selector(
    #         '#borrowerChooser > div.win_tool_area > a:nth-child(1) > span > span').click()
    #     time.sleep(2)
    #     # 点击确定
    #     driver.find_element_by_css_selector(
    #         'body > div:nth-child(17) > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a').click()
    #     # 返回主frame
    #     driver.switch_to.default_content()
    #     # 点击 快速发标审核
    #     driver.find_element_by_css_selector('#menu181 > li:nth-child(17) > div > span.tree-title').click()
    #     # 进入frame
    #     driver.switch_to.frame('work_frame')
    #     # 选中第一个项目
    #     time.sleep(1)
    #     driver.find_element_by_css_selector('#cb_dataTable_0').click()
    #     # 点击 审核
    #     driver.find_element_by_css_selector('body > div.func_tool_area > a:nth-child(1) > span > span').click()
    #     time.sleep(1)
    #
    #     # 清空原有的发标时间
    #     driver.find_element_by_css_selector('#showBidTime').clear()
    #     # 输入发标时间
    #     driver.find_element_by_css_selector('#showBidTime').send_keys(addShowTime)
    #     # 清空原有的开标时间
    #     driver.find_element_by_css_selector('#startBidTime').clear()
    #     # 输入开标时间
    #     driver.find_element_by_css_selector('#startBidTime').send_keys(addBeginTime)
    #     # 清空截标时间
    #     driver.find_element_by_css_selector('#endBidTime').clear()
    #     # 输入截标时间
    #     driver.find_element_by_css_selector('#endBidTime').send_keys(addEndTime)
    #     # 点击 子标信息信息
    #     driver.find_element_by_css_selector(
    #         '#tt > div.tabs-header > div.tabs-wrap > ul > li:nth-child(2) > a > span.tabs-title').click()
    #     # 选中第一个合同
    #     driver.find_element_by_css_selector('#cb_dataTable_0').click()
    #     # 选中第二个合同
    #     driver.find_element_by_css_selector('#cb_dataTable_1').click()
    #     # # 选中第三个合同
    #     # driver.find_element_by_css_selector('#cb_dataTable_2').click()
    #     # 选中di4/5个合同
    #     # driver.find_element_by_css_selector('#cb_dataTable_3').click()
    #     # driver.find_element_by_css_selector('#cb_dataTable_4').click()
    #
    #     # 点击 子标审核通过
    #     driver.find_element_by_css_selector('#doPrjAudit > span > span').click()
    #     # 点击 确定
    #     driver.find_element_by_css_selector(
    #         'body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span').click()
    #     time.sleep(1)
    #     driver.find_element_by_css_selector(
    #         'body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span').click()
    #     time.sleep(1)
    #
    #     # 点击 集合标审核通过
    #     driver.find_element_by_css_selector('#doCollectAudit > span > span').click()
    #     driver.find_element_by_css_selector(
    #         'body > div.panel.window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span').click()
    #     # driver.close()
