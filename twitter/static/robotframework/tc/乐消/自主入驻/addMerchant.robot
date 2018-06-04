*** Settings ***
Library    Selenium2Library
Library    Dialogs
#Library   config/cfg
*** Test Cases ***
自主入驻
    [Documentation]     注册手机号并开户
    set selenium implicit wait      10
    open browser        https://wapescrow.tourongjia.com/#/login///         chrome
#输入手机号码---投融家注册号码
    input text          css=#MobileNum          18367151122
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
#    click element       css=#react-placeholder > div > div:nth-child(2) > div > div > a.accredit_btn
    #点击 自主入驻
    click element       css=#react-placeholder > div > div > div > div.screen-content.merchant-settled > div.btn-wrap > button
#输入商户名
    input text          css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.merchant-settled > div > div > div:nth-child(1) > div.-value > input[type="text"]
    ...                 高老庄
#输入法人姓名
    input text          css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.merchant-settled > div > div > div:nth-child(2) > div.-value > input[type="text"]
    ...                 悟能
    #输入营业执照
    input text          css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.merchant-settled > div > div > div:nth-child(3) > div.-value > input[type="text"]
    ...                 123456789012345678
    #输入商户电话
    input text          css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.merchant-settled > div > div > div:nth-child(4) > div.-value > input[type="text"]
    ...                 010-12345678
    #输入商户地址
    input text          css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.merchant-settled > div > div > div:nth-child(6) > div > input[type="text"]
    ...                 龙翔桥地铁站A出口
    #输入商户介绍
    input text          css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.merchant-settled > div > div > div:nth-child(6) > div.-value > div > textarea
    ...                 这是一个商户
    execute manual step     请输入商户商户地址
    #点击 提交
    click element       css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.merchant-settled > div > div > div.cell-control > button
