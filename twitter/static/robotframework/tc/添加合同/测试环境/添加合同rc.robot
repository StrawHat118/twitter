*** Settings ***
Library   Selenium2Library
Library     Collections
Resource    rclib/rc.robot




*** Test Cases ***
添加合同--002
    open browser   ${loginUrlTest}    chrome
    CrmLogin
    Through_Menu_Test