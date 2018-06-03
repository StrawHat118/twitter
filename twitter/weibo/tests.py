#coding=utf-8
from django.test import TestCase
import paramiko
import redis
# Create your tests here.

HostIp_Mysql     = '192.168.10.80'
HostIp_Php       = '192.168.10.82'
HostIp_Admin_pay = '192.168.10.83'
HostIp_Beanstalk = '192.168.10.84'
HostIp_Admin     = '192.168.10.86'
HostIp_Bonus     = '192.168.10.87'
HostIp_Crm       = '192.168.10.88'

#第二套环境
#
# HostIp_Mysql     = '192.168.10.76'
# HostIp_Php       = '192.168.10.71'
# HostIp_Admin_pay = '192.168.10.77'
# HostIp_Beanstalk = '192.168.10.72'
# HostIp_Admin     = '192.168.10.73'
# HostIp_Bonus     = '192.168.10.74'
# HostIp_Crm       = '192.168.10.75'




username = 'root'
password = 'tourongjia123!'
Port = '22'
day_change = '20180527'
hour_change = '16:25:50'
num = 40
date = "date -s '{day} {hour}'".format(day=day_change, hour=hour_change)

GMDD_get1 = "fim_CNT1_{date}".format(date=day_change)
GMDD_get2 = "GMDD{date}".format(date=day_change)

GMCDD_get1 = "fim_CNT1_{date}".format(date=day_change)
GMCDD_get2 = "GMCDD{date}".format(date=day_change)

OECW_get1 = "fim_CNT1_{date}".format(date=day_change)
OECW_get2 = "OECW{date}".format(date=day_change)


print date
print (GMDD_get1, GMDD_get2)
print (GMDD_get1, GMDD_get2, num)
print (GMCDD_get1, GMCDD_get2)
print (GMDD_get1, GMDD_get2, num)
print (OECW_get1, OECW_get2)
print (OECW_get1, OECW_get2, num)


def run(date):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        #admin服务器时间
        ssh.connect(HostIp_Admin, Port, username, password)
        ssh.exec_command(date)
        print "check status %s OK\n" %HostIp_Admin
        ssh.close()
        #Crm服务器时间
        ssh.connect(HostIp_Crm, Port, username, password)
        ssh.exec_command(date)
        print "check status %s OK\n" %HostIp_Crm
        ssh.close()
        #mysql服务器时间
        ssh.connect(HostIp_Mysql, Port, username, password)
        ssh.exec_command(date)
        print "check status %s OK\n" %HostIp_Mysql
        #php服务器时间
        ssh.connect(HostIp_Php, Port, username, password)
        ssh.exec_command(date)
        print "check status %s OK\n" %HostIp_Php
        #Bonus服务器时间
        ssh.connect(HostIp_Bonus, Port, username, password)
        ssh.exec_command(date)
        print "check status %s OK" %HostIp_Bonus
        ssh.close()
        #beanstalk服务器时间
        ssh.connect(HostIp_Beanstalk, Port, username, password)
        ssh.exec_command(date)
        print "check status %s OK" %HostIp_Beanstalk
        ssh.close()
        #admin_pay服务器时间
        ssh.connect(HostIp_Admin_pay, Port, username, password)
        ssh.exec_command(date)
        print "check status %s OK"%HostIp_Admin_pay
        ssh.close()
    except Exception as ex:
        print "\tError %s \n"% ex

def counter(GMDD_get1, GMDD_get2, GMCDD_get1, GMCDD_get2, OECW_get1, OECW_get2, num):
    r = redis.StrictRedis(host='192.168.10.80', port=6379, db=0,password='tourongjia123')
    r.hget(GMDD_get1, GMDD_get2)
    r.hset(GMDD_get1, GMDD_get2, num)
    r.hget(GMCDD_get1, GMCDD_get2)
    r.hset(GMCDD_get1, GMCDD_get2, num)
    r.hget(OECW_get1, OECW_get2)
    r.hset(OECW_get1, OECW_get2, num)
if __name__ == '__main__':
    print "begin"
    print type(date)
    run(date)
    # counter()

