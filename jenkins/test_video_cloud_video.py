#!/user/bin/env python
# -*-encoding:utf-8-*-
import unittest
from selenium import webdriver
from login_page import *
from cloud_video_page import *
from logout_page import *
import time
import os

class cloud_video(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        chrome_driver = '/usr/local/bin/chromedriver'
        os.environ["webdriver.Chrome.driver"] = chrome_driver
        option.add_argument('disable-infobars')
        option.add_argument("--user-data-dir=/Users/koukihisashi/Library/Application Support/Google/Chrome/Default")
        self.driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)
        self.url="https://xymind.net:3000/#/login"
        self.driver.implicitly_wait(10)     #隐式等待

    def test_login(self):
        """登录 --> 云对讲 --> 退出登录"""
        sp = LoginPage(self.driver)
        sp.open(self.url)
        sp.login("xmjl001","123456")
        self.assertEqual(sp.get_msg01(), u"项目经理01", msg="验证失败！")

        sp = Cloud_Video_Page(self.driver)
        sp.enter_wulian(self.driver)
        sp.enter_cloud_video()
        self.assertAlmostEqual(sp.result_enter_cloud_video(), u"请在右侧选择呼叫对象", msg="未能进入【云对讲台 - 对讲中心】界面")
        sp.click_call_owner()
        sp.choose_item()
        sp.telephone_search("13556881305")
        sp.call_up()
        sp.hang_up()


        sp = LogoutPage(self.driver)
        sp.logout()
        self.assertEqual(sp.get_msg02(), u"忘记密码?", msg="验证失败！")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()