*** Settings ***
Library     Selenium2Library
Library     Dialogs
*** Test Cases ***
商户添加福利券
    [Documentation]   添加福利券
    set selenium implicit wait          10
    open browser                        https://wapescrow.tourongjia.com/#/login///         chrome
#输入注册账号--商户账号
     input text          css=#MobileNum          18367151162
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
    #点击福利券管理
    click element       css=#react-placeholder > div > div > div > div.screen-content.my-merchant > div.-merchant-menu > dl:nth-child(4) > dd
    #点击添加福利券
    click element       css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.coupon.tabs.-notborder.-fixed > div.fixed-bottom > a:nth-child(2)
    #输入消费金额
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(2) > div.-value > input[type="text"]
    ...                 2
    #输入优惠金额
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(3) > div.-value > input[type="text"]
    ...                 20
    #输入发行数量
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(4) > div.-value > input[type="text"]
    ...                 530
    #选择时间
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(6) > div.-value
    #选择 周三
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(2) > div > div:nth-child(3)
    #选择 确定
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure
    #选择使用时段
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(7) > div.-value
    #选择时间
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)
    #点击确定
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure
    #选择平台有效期
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(8) > div.-value
    #选择时间
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(2) > div > div:nth-child(4)
    #点击确定
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure
    #选择平台展示期
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(9) > div.-value
    #选择时间
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(2) > div > div:nth-child(4)
    #点击确定
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure
    #点击 是否免费推广
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(10) > div.-value
    #点击 是
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div.picker-column > div > div:nth-child(1)
    #点击 确定
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure
    #点击适用门店
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(11) > div.-value
    #选择门店
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.drop-down-list > ul > li > p > span
    #点击确定
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.title > span:nth-child(3)
    #输入使用规则
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.addcoupon-form > div.cell.-right-line.coupon-wrap > div:nth-child(12) > div.-value > input[type="text"]
    ...                 满2048元减1024元
    #休息一下
    execute manual step     是否继续
    #点击提交审核
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.coupon-add > div.fixed-bottom-control > button.btn-primary

