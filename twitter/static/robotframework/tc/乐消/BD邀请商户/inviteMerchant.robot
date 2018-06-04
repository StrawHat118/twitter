*** Settings ***
Library    Selenium2Library
Library   Dialogs
#Library   config/cfg
Resource    rflibr/affirm.robot
*** Test Cases ***
邀请商户
    [Documentation]     注册手机号并开户
    set selenium implicit wait      10
    open browser        https://wapescrow.tourongjia.com/#/login///         chrome
    inviteMerchant      18367150802         18367180865     东林一党        顾宪成
