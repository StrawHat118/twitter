*** Settings ***
Library     Selenium2Library
Library     Dialogs
Resource    rflibr/affirm.robot
#Library   config/cfg
*** Test Cases ***
添加子BD
    [Documentation]     注册手机号并开户
    set selenium implicit wait      10
    open browser        https://wapescrow.tourongjia.com/#/login///         chrome
    bdAffirm            18367150802         18367180866        朱常洛
