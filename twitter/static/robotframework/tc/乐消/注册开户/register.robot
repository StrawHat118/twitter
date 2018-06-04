*** Settings ***
Library    Selenium2Library
Library   Dialogs
#Library   config/cfg
*** Test Cases ***
注册
    [Documentation]     注册手机号并开户
    set selenium implicit wait      10
    open browser        https://wapescrow.tourongjia.com/#/login///         chrome
#输入手机号码--投融家注册号码
    input text          css=#MobileNum          15921305491
    #点击下一步
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div > div > button
    #输入密码
    input text          css=#PwdNum             m123456
    #点击登录
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div > div > button
    #点击账户
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-tabs > div > a:nth-child(8)
    #休息一下
    execute manual step         是否继续执行
    #点击商户入驻
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-tabs > ion-nav-view > ion-view > ion-content > div.scroll > div.shopsWeal > ul > li:nth-child(3)
    #点击授权确认
    click element       css=#react-placeholder > div > div:nth-child(2) > div > div > a.accredit_btn