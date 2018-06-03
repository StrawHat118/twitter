#coding=utf-8
from django.db import models

# Create your models here.
class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)
    def __unicode__(self):
        return self.status

class Post(models.Model):
    #心情
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    #昵称
    nickname = models.CharField(max_length=10, default='不愿意透露身份的人')
    #张贴信息
    message = models.TextField(null=False)
    #清除密码
    dell_pass = models.CharField(max_length=10)
    #提交时间
    pub_time = models.DateTimeField(auto_now=True)
    #是否激活
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.message


class ChangeTime(models.Model):
    #修改天数
    day_change  = models.CharField(max_length=10)
    #修改小时
    hour_change = models.CharField(max_length=10)
    #订单编号
    num         = models.CharField(max_length=10)

class Contract(models.Model):
    #合同编号
    contract_num = models.CharField(max_length=10)
    #合同期限
    deadline     = models.CharField(max_length=10)
    #合同金额
    amount       = models.CharField(max_length=10)
    #合同利率
    rate         = models.CharField(max_length=10)

class ContractYw(models.Model):
    #合同编号
    contract_num = models.CharField(max_length=10)
    #合同期限
    deadline     = models.CharField(max_length=10)
    #合同金额
    amount       = models.CharField(max_length=10)
    #合同利率
    rate         = models.CharField(max_length=10)
