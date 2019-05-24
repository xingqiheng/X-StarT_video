#!/user/bin/env python
# -*-encoding:utf-8-*-
from unittest import TestSuite,makeSuite
from test_video_cloud_video import *
from test_video_and_events import *
from HTMLTestRunner import HTMLTestRunner
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
import smtplib
import unittest
import time
import os

a = TestSuite()
a.addTest(makeSuite(cloud_video,"test"))
a.addTest(makeSuite(video_and_events,"test"))
b = open('/Users/koukihisashi/Desktop/python+selenium/ceshi018/report/X-StarT_result_CloudVideo.html','wb')
c = HTMLTestRunner(b,1,u"X-StarT运行平台 - 测试报告（云对讲）",u"本次测试情况如下")
c.run(a)
b.close()

# =============== 发送邮件 ===============
def sendReport(file_new):
    msg = MIMEMultipart()
    msg['Subject'] = Header('X-StarT运行平台 - 测试报告', 'utf-8')
    msg['From'] = '457950238@qq.com'  # 发件地址
    msg['To'] = '457950238@qq.com;xingqiheng@126.com;359430225@qq.com'  # 收件人地址，多人以分号分隔
    msg.attach(MIMEText('X-StarT运行平台 - 测试报告（云对讲、视频巡检和报事处理）'))     #邮件正文
    with open(file_new, 'rb') as f:
        # MIMEBase表示附件的对象
        mime = MIMEBase('text', 'txt', filename=file_new)
        # filename是显示附件名字
        mime.add_header('Content-Disposition', 'attachment', filename="X-StarT_result_CloudVideo.html")
        # 获取附件内容
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        # 作为附件添加到邮件
        msg.attach(mime)

    smtp = smtplib.SMTP('smtp.qq.com')
    smtp.set_debuglevel(1)  #用于打印出和SMTP服务器交互的所有信息
    smtp.login('457950238@qq.com', 'pfapznjqpozacagh')  # 登录邮箱的账户和密码
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())

    smtp.quit()
    print('test report has send out!')


#=============== 查找测试报告目录，找到最新生成的测试报告文件 ===============
def newReport(testReport):
    lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    file_new = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
    print(file_new)
    return file_new


if __name__ == '__main__':
    test_dir = '/Users/koukihisashi/Desktop/python+selenium/ceshi018/jenkins'  # 测试用例所在目录
    test_report = '/Users/koukihisashi/Desktop/python+selenium/ceshi018/report'  # 测试报告所在目录

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_video*.py')      #从目录中执行所有带test_video的case

    # now = time.strftime('%Y%m%d %H%M%S')  # 获取当前时间
    # filename = test_report + now + 'X-StarT_result_CloudVideo.html'  # 拼接出测试报告名
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    # runner.run(discover)
    # fp.close()

    new_report = newReport(test_report)  # 获取最新报告文件
    sendReport(new_report)  # 发送最新的测试报告