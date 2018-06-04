#coding=utf-8
from twitter import settings
from selenium import webdriver
import time
class AddContract():
    def open_browser(self,driver_type='chrome'):
        if  driver_type == 'chrome':
            self.driver = webdriver.Chrome(executable_path=settings.executable_path)
            self.driver.implicitly_wait(10)

    def login(self,url):
        self.driver.get(url)
        self.driver.find_element_by_css_selector('#userNo').send_keys("zhangchong")
        self.driver.find_element_by_css_selector('#pwd').send_keys("888888x")
        self.driver.find_element_by_css_selector('#login_btn').click()
    def through_menu_test(self):
        self.driver.find_element_by_css_selector(
            '#menuGroup > div:nth-child(3) > div.panel-header.accordion-header > div.panel-tool > div').click()
        self.driver.find_element_by_css_selector('#menu185 > li:nth-child(1) > div > span.tree-title').click()
        # 进入frame
        self.driver.switch_to.frame('work_frame')
    def add_contract_test(self,contract_num ,deadline ,amount ,rate ,customer_num ,project_type ):
        customer_num_css = '#cb_personalDataTable_{}'.format(customer_num)
        project_type_css = 'body > div:nth-child(15) > div > div:nth-child({project_type})'.format(project_type=project_type)
        time.sleep(1.5)
        # 点击新增
        self.driver.find_element_by_css_selector('body > div.func_tool_area > a:nth-child(1) > span > span').click()

        # 点击客户
        self.driver.find_element_by_css_selector('#contractInfo_custName').click()
        time.sleep(1)
        # 选择 王卫龙
        self.driver.find_element_by_css_selector(customer_num_css).click()
        # 点击选择
        self.driver.find_element_by_css_selector('#chooseCustInfoSelect > span > span').click()
        # 输入合同编号
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2) > input').send_keys(contract_num)
        # 输入合同金额
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2) > input').send_keys(1000000)
        # 输入起始时间
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(2) > input').send_keys("2018-04-15")
        # 点击投资资金转入账号
        self.driver.find_element_by_css_selector('#fundAccount > span > span').click()
        # 选择建设银行
        self.driver.find_element_by_css_selector('body > div.panel.xcombobox-panel > div > div:nth-child(2)').click()
        # 点击 日期类型选择
        self.driver.find_element_by_css_selector('#timeLimitUnit > span > span').click()
        # 点击 月份
        # time.sleep(1)
        self.driver.find_element_by_css_selector('body > div:nth-child(14) > div > div:nth-child(2)').click()
        # 输入月数
        self.driver.find_element_by_css_selector('#time').send_keys(deadline)
        # 选择产品类型
        self.driver.find_element_by_css_selector('#prjType > span > span').click()
        # 选择鑫企贷

        self.driver.find_element_by_css_selector(project_type_css).click()
        # 输入 合同日期
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4) > input').send_keys("2018-04-15")
        # 输入融资金额
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(4) > input').send_keys(amount)
        # 输入结束时间
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(4) > input').send_keys("2020-04-05")
        # 输入年化利率
        self.driver.find_element_by_css_selector('#rate').send_keys(rate)
        self.driver.find_element_by_css_selector('#repayWay > span > span').click()
        self.driver.find_element_by_css_selector('body > div:nth-child(16) > div > div:nth-child(2)').click()
        # 点击保存
        self.driver.find_element_by_css_selector('#doSave > span > span').click()
    def close_browser(self):
        self.driver.close()
    def through_menu_yw(self):
        self.driver.find_element_by_css_selector(
            '#menuGroup > div:nth-child(4) > div.panel-header.accordion-header > div.panel-tool > div').click()

        self.driver.find_element_by_css_selector('#menu185 > li:nth-child(1) > div > span.tree-title').click()
        # 进入frame
        self.driver.switch_to.frame('work_frame')
    def add_contract_yw(self,contract_num, deadline, amount, rate, customer_num, project_type):
        customer_num_css = '#cb_personalDataTable_{}'.format(customer_num)
        project_type_css = 'body > div:nth-child(15) > div > div:nth-child({project_type})'.format(project_type=project_type)

        # 点击合同管理  测试环境

        # 点击合同管理    运维环境
        # self.driver.find_element_by_css_selector('#menuGroup > div:nth-child(4) > div.panel-header.accordion-header > div.panel-tool > div').click()
        # 点击合同管理

        time.sleep(1)
        # 点击新增
        self.driver.find_element_by_css_selector('body > div.func_tool_area > a:nth-child(1) > span > span').click()

        # 点击客户
        self.driver.find_element_by_css_selector('#contractInfo_custName').click()
        time.sleep(1)
        # 选择 王卫龙
        self.driver.find_element_by_css_selector(customer_num_css).click()
        # 点击选择
        self.driver.find_element_by_css_selector('#chooseCustInfoSelect > span > span').click()
        # 输入合同编号
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2) > input').send_keys(contract_num)
        # 输入合同金额
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2) > input').send_keys(1000000)
        # 输入起始时间
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(2) > input').send_keys("2018-04-15")
        # 点击投资资金转入账号
        self.driver.find_element_by_css_selector('#fundAccount > span > span').click()
        # 选择建设银行
        self.driver.find_element_by_css_selector('body > div.panel.xcombobox-panel > div > div:nth-child(2)').click()
        # 点击 日期类型选择
        self.driver.find_element_by_css_selector('#timeLimitUnit > span > span').click()
        # 点击 月份
        # time.sleep(1)
        self.driver.find_element_by_css_selector('body > div:nth-child(14) > div > div:nth-child(2)').click()
        # 输入月数
        self.driver.find_element_by_css_selector('#time').send_keys(deadline)
        # 选择产品类型
        self.driver.find_element_by_css_selector('#prjType > span > span').click()
        # 选择鑫企贷

        self.driver.find_element_by_css_selector(project_type_css).click()
        # 输入 合同日期
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4) > input').send_keys("2018-04-15")
        # 输入融资金额
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(4) > input').send_keys(amount)
        # 输入结束时间
        self.driver.find_element_by_css_selector(
            '#addForm > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(4) > input').send_keys("2020-04-05")
        # 输入年化利率
        self.driver.find_element_by_css_selector('#rate').send_keys(rate)
        # 点击保存
        self.driver.find_element_by_css_selector('#doSave > span > span').click()

