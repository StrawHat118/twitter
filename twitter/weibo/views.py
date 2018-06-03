#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from weibo import models,tests
from releaseProgram import ReleaseProgram
from addContract import AddContract
# Create your views here.
def index(request):
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)

def posting(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)

def changeTime(request):
    template = get_template('changeTime.html')
    changeTimes = models.ChangeTime.objects.all()
    try:
        day_change = request.GET['day_change']
        hour_change = request.GET['hour_change']
        num = request.GET['num']

    except:
        day_change = None
        tips = "每个字段都要填写"

    if day_change != None:
        changeTime = models.ChangeTime.objects.create(day_change=day_change, hour_change=hour_change, num=num)
        changeTime.save()
        date = "date -s '{day} {hour}'".format(day=day_change, hour=hour_change)
        tests.run(date)
        GMDD_get1 = "fim_CNT1_{date}".format(date=day_change)
        GMDD_get2 = "GMDD{date}".format(date=day_change)

        GMCDD_get1 = "fim_CNT1_{date}".format(date=day_change)
        GMCDD_get2 = "GMCDD{date}".format(date=day_change)

        OECW_get1 = "fim_CNT1_{date}".format(date=day_change)
        OECW_get2 = "OECW{date}".format(date=day_change)

        tests.run(date)
        tests.counter(GMDD_get1, GMDD_get2, GMCDD_get1, GMCDD_get2, OECW_get1, OECW_get2, num)

    html = template.render(locals())
    return HttpResponse(html)

def add_contract_test_v(request):
    template        = get_template('addContractTest.html')
    contracts = models.Contract.objects.all()
    try:
        contract_num    = int( request.GET['contract_num'])#因为get获得的参数是str,需要转化成int
        deadline        = int(request.GET['deadline'])
        amount          = request.GET['amount']
        rate            = request.GET['rate']
        times           = int(request.GET['time'])
        project_type    = int(request.GET['project_type'])
        customer_num    = int(request.GET['customer_num'])
        url = 'https://escrowcrm1.tourongjia.com'
    except:
        contract_num = None
        tips = "每个字段都要填写"
    if contract_num != None:
        addContract = AddContract()
        addContract.open_browser()
        addContract.login(url=url)
        addContract.through_menu_test()

        for i in range(0, times):
            if i < times:
                contract = models.Contract.objects.create(contract_num=contract_num, deadline=deadline, amount=amount,
                                                       rate=rate)
                contract.save()

                addContract.add_contract_test("TRJ{contract_num}".format(contract_num=contract_num) ,deadline ,amount ,rate ,customer_num ,project_type )
                contract_num +=1

        addContract.close_browser()
    html = template.render(locals())
    return HttpResponse(html)
def add_contract_yw_v(request):
    template = get_template('addContractYw.html')
    contractsYw = models.ContractYw.objects.all()

    try:
        contract_num = int(request.GET['contract_num'])  # 因为get获得的参数是str,需要转化成int
        deadline = int(request.GET['deadline'])
        amount = request.GET['amount']
        rate = request.GET['rate']
        times = int(request.GET['time'])
        project_type = int(request.GET['project_type'])
        customer_num = int(request.GET['customer_num'])
        url = 'http://jrtestcrm.tourongjia.com/'
    except:
        contract_num = None
        tips = "每个字段都要填写"
    if contract_num != None:
        addContract = AddContract()
        addContract.open_browser()
        addContract.login(url=url)
        addContract.through_menu_yw()
        for i in range(0, times):
            if i < times:
                contract = models.ContractYw.objects.create(contract_num=contract_num, deadline=deadline, amount=amount,
                                                          rate=rate)
                contract.save()
                addContract.add_contract_yw("TRJ{contract_num}".format(contract_num=contract_num), deadline, amount, rate,
                                              customer_num, project_type)
                contract_num += 1
        addContract.close_browser()
    html = template.render(locals())
    return HttpResponse(html)

def releaseProgrsmTestV(request):
    template = get_template('releaseProgramTest.html')
    try:
        config_num   = int(request.GET['config_num'])
        config_type  = int(request.GET['config_type'])
        end_time     = int(request.GET['end_time'])
        contract_quantity = int(request.GET['contract_quantity'])
        url          = 'https://escrowadm1.tourongjia.com/'


    except:
        config_num = None

    if config_num != None:
        releaseProgram = ReleaseProgram()
        releaseProgram.open_browser()
        releaseProgram.login(url=url)
        releaseProgram.release_program(config_num=config_num ,config_type=config_type)
        if contract_quantity == 1: #普通标
            releaseProgram.choice_release_one()
            releaseProgram.audit(end_time)

            releaseProgram.audit_access_child()
        if contract_quantity == 2:
            #选择第一个合同
            releaseProgram.choice_release_one()
            #选择第二个合同
            releaseProgram.choice_release_two()
            #审核
            releaseProgram.audit(end_time)
            #查看子标信息
            releaseProgram.child_information()
            #审核第一个合同
            releaseProgram.choice_audit_one()
            releaseProgram.choice_audit_two()
            #审核通过
            releaseProgram.audit_access_collect()
        if contract_quantity == 3:
            releaseProgram.choice_release_one()
            releaseProgram.choice_release_two()
            releaseProgram.choice_release_three()
            releaseProgram.audit(end_time)
            releaseProgram.child_information()
            # 审核第一个合同
            releaseProgram.choice_audit_one()
            releaseProgram.choice_audit_two()
            releaseProgram.choice_audit_three()
            # 审核通过
            releaseProgram.audit_access_collect()

        if contract_quantity == 4:
            # 选择第一个合同
            releaseProgram.choice_release_one()
            # 选择第二个合同
            releaseProgram.choice_release_two()
            releaseProgram.choice_release_three()
            releaseProgram.choice_release_four()
            # 审核
            releaseProgram.audit(end_time)
            # 查看子标信息
            releaseProgram.child_information()
            # 审核第一个合同
            releaseProgram.choice_audit_one()
            releaseProgram.choice_audit_two()
            releaseProgram.choice_audit_three()
            releaseProgram.choice_audit_four()
            # 审核通过
            releaseProgram.audit_access_collect()

        if contract_quantity == 5:
            # 选择第一个合同
            releaseProgram.choice_release_one()
            # 选择第二个合同
            releaseProgram.choice_release_two()
            releaseProgram.choice_release_three()
            releaseProgram.choice_release_four()
            releaseProgram.choice_release_five()
            # 审核
            releaseProgram.audit(end_time)
            # 查看子标信息
            releaseProgram.child_information()
            # 审核第一个合同
            releaseProgram.choice_audit_one()
            releaseProgram.choice_audit_two()
            releaseProgram.choice_audit_three()
            releaseProgram.choice_audit_four()
            releaseProgram.choice_audit_five()
            # 审核通过
            releaseProgram.audit_access_collect()
    html = template.render(locals())
    return HttpResponse(html)

def releaseProgramYwV(request):
    template = get_template('releaseProgramYw.html')
    try:
        config_num   = int(request.GET['config_num'])
        config_type  = int(request.GET['config_type'])
        end_time     = int(request.GET['end_time'])
        contract_quantity = int(request.GET['contract_quantity'])
        url          = 'http://jrtestadm.tourongjia.com/'


    except:
        config_num = None
    if config_num != None:
        releaseProgram = ReleaseProgram()
        releaseProgram.open_browser()
        releaseProgram.login(url=url)
        releaseProgram.release_program(config_num=config_num ,config_type=config_type)
        if contract_quantity == 1: #普通标
            releaseProgram.choice_release_one()
            releaseProgram.audit(end_time)

            releaseProgram.audit_access_child()
        if contract_quantity == 2:
            #选择第一个合同
            releaseProgram.choice_release_one()
            #选择第二个合同
            releaseProgram.choice_release_two()
            #审核
            releaseProgram.audit(end_time)
            #查看子标信息
            releaseProgram.child_information()
            #审核第一个合同
            releaseProgram.choice_audit_one()
            releaseProgram.choice_audit_two()
            #审核通过
            releaseProgram.audit_access_collect()
        if contract_quantity == 3:
            releaseProgram.choice_release_one()
            releaseProgram.choice_release_two()
            releaseProgram.choice_release_three()
            releaseProgram.audit(end_time)
            releaseProgram.child_information()
            # 审核第一个合同
            releaseProgram.choice_audit_one()
            releaseProgram.choice_audit_two()
            releaseProgram.choice_audit_three()
            # 审核通过
            releaseProgram.audit_access_collect()

        if contract_quantity == 4:
            # 选择第一个合同
            releaseProgram.choice_release_one()
            # 选择第二个合同
            releaseProgram.choice_release_two()
            releaseProgram.choice_release_three()
            releaseProgram.choice_release_four()
            # 审核
            releaseProgram.audit(end_time)
            # 查看子标信息
            releaseProgram.child_information()
            # 审核第一个合同
            releaseProgram.choice_audit_one()
            releaseProgram.choice_audit_two()
            releaseProgram.choice_audit_three()
            releaseProgram.choice_audit_four()
            # 审核通过
            releaseProgram.audit_access_collect()

        if contract_quantity == 5:
            # 选择第一个合同
            releaseProgram.choice_release_one()
            # 选择第二个合同
            releaseProgram.choice_release_two()
            releaseProgram.choice_release_three()
            releaseProgram.choice_release_four()
            releaseProgram.choice_release_five()
            # 审核
            releaseProgram.audit(end_time)
            # 查看子标信息
            releaseProgram.child_information()
            # 审核第一个合同
            releaseProgram.choice_audit_one()
            releaseProgram.choice_audit_two()
            releaseProgram.choice_audit_three()
            releaseProgram.choice_audit_four()
            releaseProgram.choice_audit_five()
            # 审核通过
            releaseProgram.audit_access_collect()

    html = template.render(locals())
    return HttpResponse(html)






