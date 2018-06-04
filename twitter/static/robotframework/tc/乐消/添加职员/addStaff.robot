*** Settings ***
Library     Selenium2Library
Library     Dialogs
*** Test Cases ***
添加职员
    [Documentation]  添加职员
    set selenium implicit wait          10
    open browser                        https://wapescrow.tourongjia.com/#/login///         chrome
#输入注册账号--商户账号
     input text          css=#MobileNum          18367151022
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
    #点击职员管理
    click element       css=#react-placeholder > div > div > div > div.screen-content.my-merchant > div.-merchant-menu > dl:nth-child(3) > dd
    #点击添加职员
    click element       css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.staff-manage > div.fixed-bottom > a
#输入职员手机号码
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.staff-manage-detail > div > div:nth-child(1) > span > input[type="tel"]
    ...                 18367171860
#输入职员姓名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.staff-manage-detail > div > div:nth-child(2) > span > input[type="text"]
    ...                 沈惟敬
#输入职员职位
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.staff-manage-detail > div > div:nth-child(3) > span > input[type="text"]
    ...                 会计
    #休息一些
    execute manual step     是否继续添加
    #点击添加
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.staff-manage-detail > div > div.cell-control.-bg-gray > button
