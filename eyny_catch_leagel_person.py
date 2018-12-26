# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:42:44 2018

@author: Tuna
@Goal：用來爬取eyny論壇，試圖找出違規會員
"""
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
#from time import sleep#拿來做延遲

int_str_rule = 10 #字數限制
url = 'http://www07.eyny.com/thread-10669524-1-3DN3CFFH.html' #欲檢查的網址

html = requests.get(url)
sp = BeautifulSoup(html.text,'html.parser')

#browser = webdriver.Chrome()
#browser.maximize_window()#瀏覽器最大化

data = sp.find_all("td", class_="t_f") #取得留言串 包括發文者
for i in range(len(data)):#跑整頁的留言
    str1 = data[i].text    
    user_content = str1.split('心得：')
    
    if (len(user_content) > 1) and (len(user_content[1]) <= int_str_rule):
               
        user_account = data[i].parent.parent.parent.parent.parent.parent.parent.find(class_="xw1").text #找此回應的作者
        print(user_account)
        print(user_content[1])

print("Done！")