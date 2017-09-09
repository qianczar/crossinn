#coding=utf-8
import requests
import threading
import re
import time
page_s=input('请输入开始页码(1-92):')
page_e=input('请输入结束页码(1-92):')
while int(page_s)>int(page_e):#除了开始页码大于结束页码的输入都会被要求重新输入
    print('请重新输入页码')
    page_s = input('请输入开始页码(1-92):')
    page_e = input('请输入结束页码(1-92):')

def get_pic(page):

    url = 'http://jandan.net/ooxx/page-%s#comments' % page
    req=requests.get(url)
    try:
        txt=req.text
        id1 = re.findall(r'data-id="([0-9]*)"', txt)
        id = list(set(id1))  # 去除重复
        data = [] #【1.id，2.图片连接，3.点赞数，4.反对数】
        for i in id:
            pic = re.findall(i+r"</a></span>.*href=\"\/\/(.*large.*.(jpg|gif))", txt)
            like = re.findall(r"comment-like.*" + i + ".*\[<span>(.*)</span>\]", txt)
            unlike = re.findall(r"comment-unlike.*" + i + ".*\[<span>(.*)</span>\]", txt)
            data.append([i, pic[0][0], like[0], unlike[0]])
    except not req.ok:
        print("获取网页内容失败")
    for each in data:
        try:
            html=requests.get('http://'+each[1],timeout=1)
        except not req.ok:
            print("获取图片内容失败")
        with open("D:\python study\crossin\qimo\pic\\"+each[0]+'赞'+each[2]+'反对'+each[3]+each[1][-4:],'wb') as f:
            f.write(html.content)
            print(each[0]+'下载完成')

for page in range(int(page_s),int(page_e)+1):
    #get_pic(page)
    t = threading.Thread(target=get_pic,args=(str(page),))
    t.start()
