# -*- coding: utf-8 -*-
"""
Created on Sun May 13 13:15:41 2018

@author: Tuna
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import threading
#from time import sleep

class reflash_website(threading.Thread):
    def  __init__( self , lock , threadName):    
        '''
        @summary:初始化對象。              
        @param lock: 瑣對象。   
        @param threadName: 線程名稱。   
        '''    
        super(reflash_website,  self ).__init__(name = threadName)   #注意：一定要顯式的調用父類的初始化函數.  
        self.lock = lock    
        
    def  run( self ):
        urls = 'https://www.penghu-nsa.gov.tw/AlbumListC004800.aspx?appname=AlbumListC004800'
        browser = webdriver.Chrome()
        browser.get(urls)        
        browser.find_element_by_id('ctl00_ContentPlaceHolder1_ucAlbumList1_repList_ctl00_aLinkDetail').click()
        
        for i in range(0,10000):
            browser.refresh()                
        browser.close()
        
        
lock = threading.Lock()
for  i  in  range(10):     
    reflash_website(lock,  "thread-"  + str(i)).start()   # Open 5 隻線程
    
print("Done")