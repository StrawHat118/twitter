*** Settings ***
Library                 Selenium2Library
*** Variables ***
${loginUrlTest}         https://escrowcrm1.tourongjia.com/
${loginUrlYw}
&{userCrm}              loginName=zhangchong        passwd=888888x
*** Keywords ***
CrmLogin
    [Documentation]     登录CRM
    input text          css=#userNo                 &{userCrm}[loginName]
    input text          css=#pwd                    &{userCrm}[passwd]
    click element       css=#login_btn
Through_Menu_Test
    [Documentation]     点击菜单
    click element       css=#menuGroup > div:nth-child(3) > div.panel-header.accordion-header > div.panel-tool > div
    click element       css=#menu185 > li:nth-child(1) > div > span.tree-title