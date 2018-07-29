# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:06:22 2018

@author: Tuna
"""

from selenium import webdriver
#import getpass
#from selenium.webdriver.support.ui import Select
from time import sleep

#my_id = input("請輸入帳號")
#my_password = getpass.getpass("請輸入密碼")
my_id = 's15113114'
my_password = '123'
browser = webdriver.Chrome()
browser.maximize_window()
 
urls = 'https://info.stu.edu.tw/login/syslogin.asp'

browser.get(urls)

browser.find_element_by_id('edAccount').send_keys(my_id)
browser.find_element_by_id('edPassword12').send_keys(my_password)
my_captcha = input("請輸入驗證碼：")
browser.find_element_by_id('txt_captcha').send_keys(my_captcha)
browser.find_element_by_id('btnSubmit').click()
#xpath_result = browser.find_element_by_xpath("//")
sleep(3)
print(browser.find_element_by_id('clock').text())
browser.find_element_by_link_text('加退選').click()


firstMenu = browser.find_elements_by_class_name('firstMenu')

#for i in firstMenu:
#    scr_str = i.find_element_by_tag_name('img').get_attribute('src')
#    print(scr_str)
#print(firstMenu[1].text)
print("Done")


#select.select_by_value(my_orderquantity)

