#!/user/bin/env python
# -*-encoding:utf-8-*-
import unittest
from selenium import webdriver
from login_page import *
from video_page import *
from logout_page import *
from events_page import *
import time
import os

class video_and_events(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        chrome_driver = '/usr/local/bin/chromedriver'
        os.environ["webdriver.Chrome.driver"] = chrome_driver
        option.add_argument('disable-infobars')
        option.add_argument("--user-data-dir=/Users/koukihisashi/Library/Application Support/Google/Chrome/Default")
        self.driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)
        self.url = "https://xymind.net:3000/#/login"
        self.driver.implicitly_wait(10)  # 隐式等待

    def test_login(self):
        """登录 --> 视频巡检报事 --> 处理重大事件 --> 退出登录"""
        sp = LoginPage(self.driver)
        sp.open(self.url)
        sp.login("xmjl001","123456")
        self.assertEqual(sp.get_msg01(), u"项目经理01", msg="验证失败！")

        sp = VideoPage(self.driver)
        sp.enter_wulian()
        sp.enter_video_surveillance()
        self.assertAlmostEqual(sp.result_enter_video(),u"项目经理计划0430", msg="未能进入【视频巡检】")
        sp.enter_abnormal()
        self.assertAlmostEqual(sp.result_enter_abnormal(),u"安全巡视异常报事", msg="未能进入异常上报界面")
        sp.abnormal()
        sp.enter_lookmore()
        self.assertAlmostEqual(sp.result_enter_lookmore(),u"视频巡检",msg="未能进入【查看更多】界面")

        sp = EventsPage(self.driver)
        sp.enter_report()
        sp.report_major_event()
        sp.deal_major_events(self.driver)
        sp.enter_report()
        self.assertAlmostEqual(sp.result_sales_success(),u"已销项",msg="销项失败")

        sp = LogoutPage(self.driver)
        sp.logout()
        self.assertEqual(sp.get_msg02(), u"忘记密码?", msg="验证失败！")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()