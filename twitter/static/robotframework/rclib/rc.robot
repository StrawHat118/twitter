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
