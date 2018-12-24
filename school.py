# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:06:22 2018

@author: Tuna
"""

from selenium import webdriver
#import getpass
#from selenium.webdriver.support.ui import Select
from time import sleep
import os
#my_id = input("請輸入帳號")
#my_password = getpass.getpass("請輸入密碼")

def tryToAdd():
    try:
        browser.get(url_setWantId)
        
        data_msg = browser.find_element_by_class_name('data').text        
        print(data_msg)
        
        if(data_msg == '您選擇的課程已額滿!!'):
            return 0        
        else:
            return 1
            
        
    except BaseException:
        return 0
class_num = input('請輸入欲選課號如：ABC012345678911\n')
browser = webdriver.Chrome()
browser.maximize_window()
 
url_login = 'https://info.stu.edu.tw/ePortal/login.asp'
url_home = 'https://info.stu.edu.tw/aca/student/SelectCourse/StuSecondCourse/selnote.asp'
url_setWantId = 'https://info.stu.edu.tw/aca/student/SelectCourse/StuSecondCourse/StuSecondAddCourseAction.asp?COURSE_CODE='


print('執行中...請勿移動開啟之瀏覽器')
try:
    browser.get(url_login)
except:
    print('您已移動瀏覽器，造成程式失敗，請重新開啟此程式執行')
    os._exit()

input("請在瀏覽器中完成登入後，按下Enter")
browser.get(url_home)



url_setWantId = url_setWantId + class_num
#把課號加進聯結
bol_AddClass = 1

while(bol_AddClass):      
    
    if(tryToAdd()):
        bol_AddClass = 0
        print('選課完成，請按Enter結束程式')
        input()        
    else:
        bol_AddClass = 1
        print('選課失敗，將自動重複執行加選')
print("Done")
os._exit()

