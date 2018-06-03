*** Settings ***
Library     Selenium2Library
Library     pylib.AddContract
#Library     pylib.WebOpAdmin
Resource    rclib/rc.robot

Variables    pylib/cfg.py

*** Test Cases ***
添加合同
#
    openbrowsers
    login               https://escrowcrm1.tourongjia.com/
#    through_menu_test

#    SetupWebTests
#    login
#    through_menu_test
#     open browser        ${loginUrlTest}     chrome
#     set selenium implicit wait              10
     CrmLogin
#     through_menu_test
#    login_test
#    through_menu_test

