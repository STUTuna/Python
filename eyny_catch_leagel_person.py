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
result = '下載項目' in data[2]
print(result)


string1 = '下載項目123'
string2 = '下'
result2 = string1.find(string2)
print( result2 )

print("Done！")