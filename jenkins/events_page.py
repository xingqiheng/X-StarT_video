#!/user/bin/env python
# -*-encoding:utf-8-*-
from selenium.webdriver.common.by import By
import base_page
import time
class EventsPage(base_page.Action):
    #【报事管理】页面
    wulian_logo_loc = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[1]/ul/li[1]/span")
    events_manage_main_loc = (By.XPATH, "//div[@id='app']/div/div/div[2]/ul/li/div/span")
    events_manage_loc = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/ul/li[1]/ul/li/div/span")

    #重大事件上报
    click_events_loc = (By.XPATH, "//*[@id='tableExcel']/tbody/tr[1]/td[11]/span")
    click_look_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div[3]/span")
    major_event_information_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[3]/div/div/div/form/div/div/div/textarea")
    determine_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[3]/div/div/div[2]/button[2]")

    #处理重大事件
    click_major_events_loc = (By.XPATH, "//*[@id='tableExcel']/tbody/tr[1]/td[11]/span")
    deal_events_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div[3]/div/div[2]/p[2]/span")
    click_photo_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[3]/div/div/div/form/div[2]/div/div")
    send_photo_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[3]/div/div/div/form/div[2]/div/input")
    remarks_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[3]/div/div/div/form/div[3]/div/div/textarea")
    destruction_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[3]/div/div/div[2]/button[2]")

#=============== 以下为断言元素 ===============
    #是否进入【报事管理】界面
    events_manage = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div[1]/ul/li[4]/span")

    #是否销项成功
    sales_success = (By.XPATH, "//*[@id='tableExcel']/tbody/tr[1]/td[10]")


    def enter_report(self):
        self.find_element(*self.wulian_logo_loc).click()
        time.sleep(1)
        self.find_element(*self.events_manage_main_loc).click()
        time.sleep(1)
        self.find_element(*self.events_manage_loc).click()
        time.sleep(2)

    def report_major_event(self):
        self.find_element(*self.click_events_loc).click()
        time.sleep(1)
        self.find_element(*self.click_look_loc).click()
        time.sleep(2)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.find_element(*self.major_event_information_loc).send_keys(u"重大事件上报，" + current_time)
        time.sleep(1)
        self.find_element(*self.determine_loc).click()
        time.sleep(2)

    def deal_major_events(self,driver):
        self.find_element(*self.click_major_events_loc).click()
        time.sleep(1)
        self.find_element(*self.deal_events_loc).click()
        time.sleep(1)
        self.find_element(*self.click_photo_loc).click()
        time.sleep(1)
        # print(type(self.find_element(*self.send_photo_loc)))
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[3]/div/div/div[3]/div/div/div/form/div[2]/div/input").send_keys("/Users/koukihisashi/Desktop/test_picture.png")
        # self.find_element(*self.send_photo_loc).send_keys("/Users/koukihisashi/Desktop/python+selenium/ceshi018/PO/test_picture.png")
        time.sleep(1)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.find_element(*self.remarks_loc).send_keys(u"重大事件上报，" + current_time)
        time.sleep(1)
        self.find_element(*self.destruction_loc).click()
        time.sleep(2)

#=============== 以下为断言 ===============
    #判断是否进入【报事管理】
    def result_events_manage(self):
        return self.find_element(*self.events_manage).text

    #判断是否销项成功
    def result_sales_success(self):
        return self.find_element(*self.sales_success).text

