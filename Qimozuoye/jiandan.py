import requests
import threading
import re
import time
page_s=input('请输入开始页码(1-92):')
page_e=input('请输入结束页码(1-92):')
while page_s>page_e :#除了开始页码大于结束页码的输入都会被要求重新输入
    print('请重新输入页码')
    page_s = input('请输入开始页码(1-92):')
    page_e = input('请输入结束页码(1-92):')

def get_pic(page):
    url = 'http://jandan.net/ooxx/page-%s#comments' % page
    req=requests.get(url)
    txt=req.text
    pic=re.findall(r'(w.*large.*.(jpg|gif)).*.(jpg|gif)',txt)
    for i in pic:
        html=requests.get('http://'+i[0])
        with open('D:\python study\crossin\Qimozuoye\pic\%s'% i[0][-36:],'wb') as f:
            f.write(html.content)
            print(i[0][-36:]+'下载完成')

for page in range(int(page_s),int(page_e)+1):
    t = threading.Thread(target=get_pic,args=(str(page),))
    t.start()