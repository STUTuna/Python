# -*- coding: utf-8 -*-
#此程式用來爬取巴哈姆特動畫瘋之最新動畫
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep#拿來做延遲

urls = 'https://ani.gamer.com.tw/index.php' #動漫的網址

html = requests.get(urls)
sp = BeautifulSoup(html.text,'html.parser')

browser = webdriver.Chrome()
browser.maximize_window()#瀏覽器最大化

data = sp.select('.newanime__content')

new_url = data[0].get("href")#new_url為最新的動漫網址

print("前往的網址：" + new_url)

browser.get(new_url)

browser.find_element_by_id('adult').click()#點擊同意按鈕
sleep(30)#等待30秒的廣告
browser.find_element_by_class_name('vast-skip-button enabled').click()#跳過廣告


