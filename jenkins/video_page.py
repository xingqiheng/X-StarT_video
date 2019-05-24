#!/user/bin/env python
# -*-encoding:utf-8-*-
from selenium.webdriver.common.by import By
import base_page
import time
class VideoPage(base_page.Action):
    # 进入【物联监控】
    close_window_loc = (By.XPATH, "//div[@id='app']/div[3]/div[2]/div/div/div/div/span")  # 收起告警事件悬浮窗
    enter_wulian_loc = (By.XPATH, "//p")

    # 进入【视频物联监控】
    video_surveillance_loc = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/ul/li[6]/div/span")
    safety_patrol_loc = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/ul/li[6]/ul/li[1]/div/span")
    choose_plan_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div/div/ul/li/span")

    # 进入【异常报事】
    enter_abnormal_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/button[2]")

    # 执行异常报事操作
    choose_emergency_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div[3]/div/div/form/div[4]/div/label/span/span")
    choose_major_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div[3]/div/div/form/div[5]/div/div/div/span/span/i")
    choose_engineer_loc = (By.XPATH, "//body/div[2]/div/div/ul/li[2]")
    abnormal_information_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div[3]/div/div/form/div[6]/div/div/textarea")
    submission_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div[3]/div/div/div[2]/div[2]")

    #进入【查看更多】
    look_more_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div[2]/div/span[2]")

    #选择日期
    click_date_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div/div/div/input")
    choose_day01_loc = (By.XPATH, "//td[4]/div/span")
    choose_day02_loc = (By.XPATH, "//tr[3]/td[6]/div/span")

    #选择项目
    click_project_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/img")
    choose_project_loc = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/label/span/span")
    determine = (By.XPATH, "//div[@id='app']/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div[3]/div[3]/button[2]")

#=============== 以下为断言元素 ===============
    #是否进入异常上报界面
    title_abnormal_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/div/div/div[1]/p")

    #是否进入【查看更多】界面
    type_loc = (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div[3]/table/tbody/tr[1]/td[9]")



    def enter_wulian(self):
        self.find_element(*self.close_window_loc).click()
        time.sleep(1)
        self.find_element(*self.enter_wulian_loc).click()
        time.sleep(2)

    def enter_video_surveillance(self):
        self.find_element(*self.video_surveillance_loc).click()
        time.sleep(1)
        self.find_element(*self.safety_patrol_loc).click()
        time.sleep(1)
        self.find_element(*self.choose_plan_loc).click()
        time.sleep(2)

    def enter_abnormal(self):
        self.find_element(*self.enter_abnormal_loc).click()
        time.sleep(2)

    def abnormal(self):
        self.find_element(*self.choose_emergency_loc).click()
        time.sleep(1)
        self.find_element(*self.choose_major_loc).click()
        time.sleep(1)
        self.find_element(*self.choose_engineer_loc).click()
        time.sleep(1)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.find_element(*self.abnormal_information_loc).send_keys(u"不能观看视频，"+current_time)
        time.sleep(1)
        self.find_element(*self.submission_loc).click()
        time.sleep(2)

    def enter_lookmore(self):
        self.find_element(*self.look_more_loc).click()
        time.sleep(3)


#=============== 以下为断言 ===============
    #验证是否进入【视频巡检】界面
    def result_enter_video(self):
        return self.find_element(*self.choose_plan_loc).text

    #验证是否进入异常上报界面
    def result_enter_abnormal(self):
        return self.find_element(*self.title_abnormal_loc).text

    #验证是否金图【查看更多】界面
    def result_enter_lookmore(self):
        return self.find_element(*self.type_loc).text