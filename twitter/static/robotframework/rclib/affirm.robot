*** Settings ***
Library     Selenium2Library
Library     Dialogs
*** Keywords ***
#BD确认
bdAffirm
    [Documentation]     bd确认
    [Arguments]         ${bdMobile}             ${childBdMobile}        ${childBdName}
    input text          css=#MobileNum          ${bdMobile}
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
    #点击BD团队管理
    click element       css=#react-placeholder > div > div > div > div.screen-content.mybusiness > div.mybusiness-menu > dl:nth-child(2)
    #点击添加子BD
    click element       css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.sub-merchant > div.fixed-bottom > a
#输入子BD的手机号
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div:nth-child(1) > span > input[type="tel"]
    ...                 ${childBdMobile}
#输入子BD的姓名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div:nth-child(2) > span > input[type="text"]
    ...                 ${childBdName}
    #输入身份证号码
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div:nth-child(3) > span > input[type="text"]
    ...                 450326198912241844

    #输入银行卡号
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div >div:nth-child(4) > span > input[type="tel"]
    ...                 6228483178200785674
    #选择开户行
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div:nth-child(5) > span
    #选择浙江省
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(11)
    #选择杭州市
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(1)
    #选择中国民生银行
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(12)
    #选择天目山支行
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(1)
    #选择负责区域
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.cell-item-add > div.cell-line > div > span > input[type="text"]
    sleep               0.5
    #选择河北省
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(3)
    #选择内蒙古
    sleep               0.5
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(5)
    sleep               0.5
    #选择吉林省
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(7)
    sleep               0.5
    #选择上海市
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(9)
    sleep               0.5
    #选择浙江省
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(11)
    sleep               0.5
    #选择江干区
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(3) > div > div:nth-child(3)
    #选择西湖区
    sleep               0.5
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(3) > div > div:nth-child(5)
    sleep               0.5
    #点击确认
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure


    # 选择 添加商户
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(1)
    #选择审核商户
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(2)
    #选择提现
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(3)
    #选择 发布商户福利
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(4)
    #选择审核商户福利
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(5)
    #添加区域
#    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.cell-item-add > div.cell-line > div > span > input[type="text"]
    execute manual step     是否继续
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.cell-control > button
    #点击 我知道了
    close browser       css=#react-placeholder > div > div > div:nth-child(3) > div.screenui-alertui-bg > div > ul > li
    execute manual step     是否接受邀请
#邀请商户
inviteMerchant
    [Arguments]     ${bdMobile}         ${merchantMobile}       ${merchantName}     ${bossName}
     input text          css=#MobileNum          ${bdMobile}
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
    #点击商户管理
    click element       css=#react-placeholder > div > div > div > div.screen-content.mybusiness > div.mybusiness-menu > dl:nth-child(1)
#    click element       css=#react-placeholder > div > div > div > div.screen-content.mybusiness > div.mybusiness-menu.menu-three > dl:nth-child(1) > dd > img
    #点击添加商户
    click element       css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.sub-merchant > div.fixed-bottom
#输入商户名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(2) > div.-value > input[type="text"]
    ...                 ${merchantName}
    #输入商户电话
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(3) > div.-value > input[type="text"]
    ...                 010-12345678
    #输入logo和商户地址
    execute manual step     请输入商户logo和商户地址
    #点击 区域
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel.-new-tab-panel > div:nth-child(1) > div:nth-child(4) > div.-value > input[type="text"]
    sleep               0.5
    #选择河北省
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(3)
    #选择内蒙古
    sleep               0.5
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(5)
    sleep               0.5
    #选择吉林省
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(7)
    sleep               0.5
    #选择上海市
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(9)
    sleep               0.5
    #选择浙江省
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(1) > div > div:nth-child(11)
    sleep               0.5
    #选择江干区
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(3) > div > div:nth-child(3)
    #选择西湖区
    sleep               0.5
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div:nth-child(3) > div > div:nth-child(5)
    sleep               0.5
    #点击确认
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure



    #输入商户地址
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(5) > div > input[type="text"]
    ...                 龙翔桥地铁站B出口
    #所属分类
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(6) > div.-value > input[type="text"]
    #选择 美食
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div.picker-column > div > div:nth-child(2)
    #选择 确定
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure
    #输入商户面积
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(7) > div.-value > input[type="number"]
    ...                 1024
    #输入员工人数
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(8) > div.-value > input[type="tel"]
    ...                 2048
    #添加商户宣传图片
    execute manual step     请添加商户宣传图片
    #输入商户介绍
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(10) > div.-textarea > textarea
    ...                 这是一个商户
#输入商户手机号---商户注册号码
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(1) > div.-value > input[type="tel"]
    ...                 ${merchantMobile}
#输入法人姓名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(2) > div.-value > input[type="text"]
    ...                 ${bossName}
#输入法人手机
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(3) > div.-value > input[type="tel"]
    ...                 ${merchantMobile}
    #添加法人身份证
    execute manual step      请添加法人身份证照片
#输入持卡人姓名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(5) > div.-value > input[type="text"]
    ...                 商汤
#输入银行卡号
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(6) > div.-value > input[type="tel"]
    ...                 6228483178500897857
    sleep               1
    #点击开户行
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(7) > div.-value
    #点击 浙江省
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(11)
    #点击浙江省杭州市
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(1)
    #点击 中国民生银行
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(12)
    #点击 天目山支行
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(1)
    #上传营业执照图片
    execute manual step     请上传营业执照图片
    #输入营业执照编号
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(8) > div.-value > input[type="text"]
    ...                 123456789012345678
    #输入邀请注册奖励
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(3) > div.add-line > div > div:nth-child(2) > div.-value > input[type="number"]
    ...                 12
    #输入首投奖励
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(2) > div.-value > input[type="number"]
    ...                 23
    #输入 福利券结算比例
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(2) > div.-value > input[type="number"]
    ...                 34
    #稍微休息
    execute manual step  是否继续
    #点击 提交审核
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-a
