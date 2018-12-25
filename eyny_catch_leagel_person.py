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

url = 'http://www07.eyny.com/thread-10669524-1-3DN3CFFH.html' #欲檢查的網址

html = requests.get(url)
sp = BeautifulSoup(html.text,'html.parser')

#browser = webdriver.Chrome()
#browser.maximize_window()#瀏覽器最大化

data = sp.find_all("td", class_="t_f")
                 
#data2 = data.find_all("td", class_="t_f")
str1 = data[5].text
print(str1)

result = str1.find('心得：')
print(result)

print("字串長度為：" , len(str1))

print(str1.split('心得：')[1])

print("Done！")