# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
import time
import random

#==============================================================================
def init(browser):
    #定义driver
    if browser == 'chrome':

#        Options = webdriver.ChromeOptions()
#        Options.add_argument("--disable-bundled-ppapi-flash")
        driver = webdriver.Chrome()


    else:
#        Profile = webdriver.FirefoxProfile()
#        Profile.set_preference('permissions.default.stylesheet', 2)
#        Profile.set_preference('permissions.default.image', 2)
#        Profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
#        Profile.set_preference("http.response.timeout", 5)
#        Profile.set_preference("dom.max_script_run_time", 5)
        driver = webdriver.Firefox()
    return driver

def play(urllist,timelist,mode,t,time0,browser):

    #随机列表
    source = random.sample(range(len(urllist)), len(urllist))

    #设置初始值
    element      = '//div[@class="player"]'
    if not t:
        t            = 1
    if not time0:
        time0        = 5
    i            = int(t) - 1
    time0        = int(time0)
    timeofload   = time0*2
    timeofbuffer = time0
    timeofnext   = time0

    #
    driver = init(browser)

    while True:
        index = source[i]
        if mode == 'r' or mode == 'recycle':
            index = i
        try:
            #防止网页缓冲过长
            driver.set_page_load_timeout(timeofload)
            driver.get(urllist[index].strip())
            print()
            print('第'+str(index+1)+'个视频缓冲时间少于'+str(timeofload))
        except Exception:
            print()
            print('第'+str(index+1)+'个视频缓冲超时，吃药之后萌萌哒')
        try:
            #最大化浏览器,不想最大化的话就注释掉
            driver.maximize_window()
            #最大化播放器,不想最大化的话就注释掉
            driver.find_element_by_xpath\
            (element+'/div[@id="bilibiliPlayer"]/div[@class="bilibili-player-area video-state-pause"]/div[@class="bilibili-player-video-control"]/div[@name="browser_fullscreen"]').click()
            print()
            print('第'+str(index+1)+'个视频全屏成功')
            #防止命令太近反应不过来
            time.sleep(timeofbuffer)
            #播放
            driver.find_element_by_xpath(element).click()
            print()
            print('第'+str(index+1)+'个视频播放成功')

            #随时检测是否在播放，一旦关闭播放器就重新开一个
            try:
                for j in range(int(int(timelist[index].strip())/timeofnext)):
                    driver.current_url
                    #视频持续时间
                    time.sleep(timeofnext)
            except:
                print()
                print('手动开始播放下一视频')
                driver = init(browser)

        except Exception:
            #如果有错误，先测试浏览器是否关闭，若关闭则打开一个新的，若没有关闭，加1指数，继续循环
            try:
                driver.current_url
            except:
                driver = init(browser)
            print()
            print('致命错误，切到下个视频萌萌哒')
            i = i+1
            if i == len(urllist):
                i = 0
            continue
        #一切正常后加1指数循环
        i = i+1
        #防止指数溢出
        if i == len(urllist):
            i = 0

#==============================================================================
if __name__=='__main__':

    #视频网址
    urlobject = open('urllist.txt','r')
    urllist   = urlobject.readlines()
    urlobject.close()

    #视频持续播放时间，与网址相对应（单位 秒）
    timeobject = open('timelist.txt','r')
    timelist   = timeobject.readlines()
    timeobject.close()
    print()
    input('B站播放列表小程序bililist,源码https://github.com/tedoreve/. 按回车继续：')
    print()
    mode          = input('(默认随机,输入r代表循环播放,输入s代表随机播放)  请输入参数设定播放模式: ')
    print()
    index         = input('(默认第一个,播放列表不能为空,随机的话就无效了)  请设定从第几个视频开始播放：')
    print()
    timeofbuffer  = input('(默认5,推荐3~7,网络慢就用大一些的值)            请设定缓冲时间：')
    print()
    browser       = input('(默认firefox,输入chrome或者firefox)             请设定浏览器:')

    play(urllist,timelist,mode,index,timeofbuffer,browser)
