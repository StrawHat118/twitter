*** Settings ***
Library   Selenium2Library
Library     Collections
Library      pylib.WebOpAdmin
#Library      pylib.AddContract
Resource    rclib/rc.robot


Variables    pylia/cfg.py


*** Test Cases ***
添加老师--tc00001
    SetupWebTests
    LoginWebSites        &{adminuser}[name]      &{adminuser}[pw]
    through_menu_test
#    [Setup]     Run Keywords    SetupWebTests
#    ...         AND     LoginWebSites        &{adminuser}[name]      &{adminuser}[pw]
#    ...         AND     LoginWebSites        &{adminuser}[name]      &{adminuser}[pw]
#    ...         AND     DeleteAll       course
#    ...         AND     DeleteAll            teacher
#    ...         AND     addCourses                   初中数学        不好学         1
#    ...         AND     addCourses                   初中语文        很容易的        2
#    addTeachers      庄子      zhuangzi        庄子老师        1       初中语文
#    ${teachers}=    getCourseList
#    should be true          $teachers==[u'庄子']
#
#    addTeachers      孔子      kongzi        孔子老师        2       初中数学
#    ${teachers}=    getTeacherList
#    should be true      $teachers==[u'庄子',u'孔子']
#    [Teardown]      Run Keywords     DeleteAll   course    AND   DeleteAll     teacher