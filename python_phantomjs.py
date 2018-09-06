# -*- coding:utf-8 -*-
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
headers_base = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Connection': 'keep-alive',
            'Host': 'tu.duowan.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
            'Referer': 'http://tu.duowan.com',
        }
url = "http://tu.duowan.com"
def main(url,name):
    vv = get_page_source(url)
    soup = BeautifulSoup(vv, 'html.parser')
    content = soup.findAll("em")
    # print(content)
    for con in content:
        text = con.find("a", {'target': '_blank'}).text
        url=con.find("a",{'target':'_blank'}).get('href')
        if url[-4:] == 'html':
           print(text)
           print(url)
        else:
           print('null')
        onelist(url,text,name)



# 懒加载处理首页
def get_page_source(url):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get(url)

    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(1)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight

    element = driver.find_element_by_id('content')
    outerhtml = element.get_attribute("outerHTML")
    driver.quit()
    return outerhtml



# 懒加载处理单页
def get_page_source1(url):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get(url)

    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(1)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight

    element = driver.find_element_by_id('image-show')
    outerhtml = element.get_attribute("outerHTML")
    driver.quit()
    return outerhtml



def one(cc,name,dir):
    # print(cc)
    soup = BeautifulSoup(cc, 'html.parser')
    content = soup.findAll("div", {'class': 'show-img'})
    # print(content)
    for con in content:
        try:
            text = con.find('img').get('alt')
            url = con.find('img').get('src')
        except :
            break
        else:
           print(text)
           print(url)
        fp = open(dir + '/' + name+'.txt', 'a')
        fp.write(text)
        fp.write('\n')
        fp.write(url)
        fp.write('\n')
        fp.close()


def onelist(u,name,dir):
    for i in range(1, 51):
        c = str(u)+'#p'+str(i)
        cc = get_page_source1(c)
        one(cc,name,dir)



def check_dir(name):
    '''
    检查目录创建目录
    '''
    name_ = 'D:/py/demo1/'
    ping_name = name_ + name
    if not os.path.exists(ping_name):
        os.mkdir(ping_name)
    return ping_name

def test():
    cc = get_page_source1("http://tu.duowan.com/gallery/137480.html#p3")
    soup = BeautifulSoup(cc, 'html.parser')
    content = soup.findAll("div", {'class': 'show-img'})
    for con in content:
        try:
            text = con.find('img').get('alt')
            url = con.find('img').get('src')
        except:
            break
            print('t='+text)
            print('u='+url)
    print(content)


dir = input('请输入文件名：')
name = check_dir(dir)
main(url,name)
# test()