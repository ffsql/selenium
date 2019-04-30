# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:57:34 2019

@author: Admin
"""
import sys
import time
import random
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pytesseract
from PIL import Image
#import pymysql
import time
import urllib.request as ul
import urllib.parse as uz
import http.cookiejar as cookielib

def ChromeDriverNOBrowser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driverChrome = webdriver.Chrome(chrome_options=chrome_options)
    return driverChrome

def get_code(url):#获取验证码的步骤
    c=cookielib.LWPCookieJar()#先把cookie对象存储为cookiejar的对象
    cookie = ul.HTTPCookieProcessor(c)#把cookiejar对象转换为一个handle
    opener = ul.build_opener(cookie)#建立一个模拟浏览器，需要handle作为参数
    ul.install_opener(opener)
    req = ul.Request(url)
    code_file = opener.open(req).read()#此时为浏览器的open而不再是ul.urlopen,下同
    with open(r'C:\Users\Admin\Anaconda3\Lib\site-packages\pytesseract\yzm.png','wb')as f:
        f.write(code_file)


#driver = ChromeDriverNOBrowser()
driver = webdriver.Chrome()
driver.get("http://ssstoday.com/")
time.sleep(1)
driver.switch_to_frame('mem_index')

driver.find_element_by_xpath('//*[@id="username"]').send_keys('qwe222')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123qwe')
driver.find_element_by_xpath('//*[@id="vImg"]').click()
time.sleep(1)
yzm = driver.find_element_by_xpath('//*[@id="vImg"]').get_attribute("src")
get_code(yzm)
time.sleep(1)
Image.open(r'C:\Users\Admin\Anaconda3\Lib\site-packages\pytesseract\yzm.png').show()
imgs = pytesseract.image_to_string(Image.open(r'C:\Users\Admin\Anaconda3\Lib\site-packages\pytesseract\yzm.png'),lang='eng')
print(imgs)
driver.close()
sys.exit()

driver.find_element_by_xpath('//*[@id="rmNum"]').send_keys('12')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginarea"]/div[1]/div[2]/input').click()
time.sleep(1)
driver.switch_to_frame('mem_index')  #进入fram框架
driver.find_element_by_xpath('//*[@id="main"]/div[1]/table/tbody/tr/td[2]/form/input').click()
#driver.switch_to.alert.accept()
driver.maximize_window()
time.sleep(1)
article = driver.find_element_by_xpath('//*[@id="n5"]')
ActionChains(driver).move_to_element(article).perform()

driver.find_element_by_xpath('//*[@id="lottery"]/div/div/a[1]').click()
#driver.maximize_window()#放大
all_handles = driver.window_handles#获取所有句柄
driver.close()   #关闭旧的网页
driver.switch_to.window(all_handles[-1])#获得最新句柄

driver.find_element_by_xpath('//*[@id="wrapBox"]/article/div[3]/div[1]/div[3]/div[2]/div[3]/a[3]').click()
time.sleep(1)

ss = driver.find_element_by_xpath('//*[@id="h1"]').text
if int(ss[11:]) < 5:
    time.sleep(int(ss[11:])+7)
#i = random.randint(0,3)
#if i == 1:
##    大//*[@id="j-n1"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[1]
#    driver.find_element_by_xpath('//*[@id="j-n1"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[2]').click()
#elif i == 0:#小//*[@id="j-n1"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[2]
#    driver.find_element_by_xpath('//*[@id="j-n1"]/table[1]/tbody/tr[1]/td[4]').click()
#elif i == 2:#单//*[@id="j-n1"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[3]
#    driver.find_element_by_xpath('//*[@id="j-n1"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[3]').click()
#elif i == 3: #双//*[@id="j-n1"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]
#    driver.find_element_by_xpath('//*[@id="j-n1"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]').click()
driver.find_element_by_xpath('//*[@id="play-tab"]/li[3]/a').click()
for i in range(1,11):
    v = random.randint(1,10)
    if v >= 7:
        continue
    driver.find_element_by_xpath('//*[@id="j-n3"]/table/tbody/tr/td[1]/table/tbody/tr' + str([i])).click()


a = str(random.randint(10,50))
driver.find_element_by_xpath('//*[@id="parlay-ctn"]/div[1]/div[2]/form/label/input').send_keys(a)
driver.find_element_by_xpath('//*[@id="parlay-ctn"]/div[1]/div[2]/form/button[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/table/tbody/tr[3]/td/div[2]/button[2]').click()

time.sleep(5)
driver.close()