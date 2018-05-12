#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from weibo import models

# Create your views here.
def index(request):
    # years = range(1960,2021)
    # urfcolor = request.GET.getlist('fcolor')
    # names = request.GET["user_id",False]
    template = get_template('index.html')

    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods =models.Mood.objects.all()
    #获取前端提交的数据
    try:
        mood = request.GET['mood']
        nickname = request.GET['nickname']
        message = request.GET['message']
        dell_pass = request.GET['dell_pass']
    except:
        nickname =  None
        tips = '如果需要张贴信息,则每一个字段都要填写'

    if nickname !=None:
        mood = models.Mood.objects.get(status=mood)
        post = models.Post.objects.create(mood=mood, nickname=nickname, dell_pass=dell_pass, message = message  )
        post.save()
        tips ='成功存储!请记得您的编辑密码[{}]!, 信息必须经过审核才能显示'.format(dell_pass)

    html = template.render(locals())
    return HttpResponse(html)

def posting(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)