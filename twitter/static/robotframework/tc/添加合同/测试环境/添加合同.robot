*** Settings ***
Library     Selenium2Library
Library     pylib.AddContract


*** Test Cases ***
添加合同--001
    #打开浏览器
    openbrowsers
    #登录
    login               https://escrowcrm1.tourongjia.com/
    #进入二级菜单
    through_menu_test
    #添加合同
    add_contract_test       20180604026     3   10000   9      0     10
