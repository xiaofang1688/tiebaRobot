# -*- coding: utf-8 -*-
from selenium import webdriver  # 导入网页内驱动模块
from selenium.webdriver.common.keys import Keys  # 导入按键类
from selenium.webdriver.common.action_chains import ActionChains  # 导入动作类
from random import choice
from time import sleep
import re
import pyautogui  # 导入自动控制鼠标的库

'''
IT编程学习平台:java，python，php,C++,前端开发，ui设计，建站，运维及电商运营等课程学习资料，方包博客网址：https://fang1688.cn
公众号：“优派编程”，回复关键词获取对应的学习资料！
'''


# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'


profile = webdriver.FirefoxProfile(r'C:\Users\Administrator.fangbao-PC\AppData\Roaming\Mozilla\Firefox\Profiles\i0j77088.default')
# profile.set_preference("general.useragent.override", user_agent)
browser = webdriver.Firefox(profile, timeout=300)  # 使用profile可以实现自动登录

def auto():
    currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置
    print(currentMouseX, currentMouseY)
    # 控制鼠标移动,duration为持续时间
    for i in range(2):
        pyautogui.moveTo(100, 100, duration=0.25) # 移动到 (100,100)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

def cookie():
    cookies = '''
    		BA_HECTOR = a5ah8g0l04a5a4a5vc1fshgrj0r;
            BAIDUID = F45E0D68906EC7332288F0AD0A78D2E6:FG=1;
            bdshare_firstime = 160632222992838584;
            此处省略....
            st_key_id = 15;
            st_sign = 7a82bb01e;
            STOKEN = bad8d6b3520cc3a5db92dcdf8fb88d0e7a3d8f6dbafc536db0ef04bfe1fe2330;
            TIEBA_USERTYPE = 6bec7c328d1423243d8b359d53;
            TIEBAUID = 5a13ed66e6322e1113233a2da1144;
            wise_device = 0;  
    '''
    cookiesList = re.findall(r'([\S\s]*?)=([\S\s]*?);', cookies)
    for cookie in cookiesList:
        ck = {'name': cookie[0].strip(), 'value': cookie[1].strip()}
        browser.add_cookie(ck)  # 添加cookie到浏览器测试对象


def get_content():
    file = open('reply.txt', 'r').readlines()  # 读取所有评论
    return (choice(file).strip())  # 随机获取一行评论并返回



def reply():
    content = get_content()  # 获取评论内容
    js = "document.getElementById('ueditor_replace').innerHTML='%s'" % content  # 编写js脚本
    browser.execute_script(js)  # 执行js脚本


def main():
    count = 0
    for url in open('url.txt', encoding='utf-8').readlines():
        print (url)
      # 逐行读取url文件
        count += 1
        if count >= 1:
            browser.get(url)  # 打开地址
            sleep(7)
            cookie()  # 添加cookie
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 滚动到页面底部
            
            # fang = browser.find_element_by_css_selector('.poster_submit')
            # browser.execute_script("arguments[0].scrollIntoView();",fang)  
            reply()  # 写入回复内容
            auto() # 执行鼠标自动控制脚本
            sleep(6) 
            # ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()  # 关闭网页
            # 提交评论
            browser.find_element_by_css_selector('.poster_submit').click() 
            sleep(5) 
            # browser.execute_script("location.reload()")
            # 刷新页面
            # browser.refresh()
    # 退出浏览器
    browser.quit()
if __name__ == '__main__':
    main()
    print ("评论完成")