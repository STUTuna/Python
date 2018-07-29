# -*- coding: utf-8 -*-
"""
Created on Sun May 13 01:46:18 2018

@author: Tuna
"""


#from selenium import webdriver
#
#from PIL import Image
#
#from pytesseract import image_to_string
#
#
##browser = webdriver.Chrome()
#
# 
##urls = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsH0zB9CfcT4yNIYL8UsEJo-z3Ee4p2P5MTRkzH_ZqIAjhBcvl'
#
##browser.get(urls)
#
#
#img = Image.open('images.png')
#
#print(img)
#
#print(image_to_string(img), shell=True)
#
#print("done")
# encoding=utf-8
from PIL import Image
from pytesseract import image_to_string

tessdata_dir_config = 'D:\\Tools\\tesseract-Win64\\tesseract.exe'
img = Image.open('images.png')
img_grey = img.convert('L')

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
img_out = img_grey.point(table, '1')

text = image_to_string(img_grey,lang = 'chi_sim' , config = tessdata_dir_config)  # 将图片转成字符串

print(text)
print("done")