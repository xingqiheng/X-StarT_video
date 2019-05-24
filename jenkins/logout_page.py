#!/user/bin/env python
# -*-encoding:utf-8-*-
from selenium.webdriver.common.by import By
import base_page
import time
class LogoutPage(base_page.Action):
    # 退出登录元素
    topname_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/span")
    logout_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[2]")



    # 退出成功 - 断言元素
    msg_forget_pwd = (By.XPATH, "//div[@id='app']/div/div/div/form/div/span[2]")


    def logout(self):
        self.find_element(*self.topname_loc).click()
        time.sleep(3)
        self.find_element(*self.logout_loc).click()
        time.sleep(2)


    def get_msg02(self):
        return self.find_element(*self.msg_forget_pwd).text  #退出登录成功获取页面信息