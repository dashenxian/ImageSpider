import requests as re
from bs4 import BeautifulSoup
import os
import threading

class Spider:
    # 传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
        u = re.get(imageURL)
        data = u.content
        f = open(fileName, 'wb')
        f.write(data)
        f.close()

    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        f.write(content.encode('utf-8'))
    #创建新目录
    def mkdir(self,path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

    def GetDeatilPage(self, url,encodeing="utf-8"):
        res = re.get(url)
        res.encoding=encodeing
        soup = BeautifulSoup(res.text, "html.parser")
        imgs = soup.select("article.article-content > p > img")
        if(len(imgs)>0):
            #检查目录是否存在，不存在就创建
            self.mkdir(imgs[0].attrs.get("alt"))
            i=1
            for img in imgs:
                imgurl = img.attrs.get("src")
                self.saveImg(imgurl, img.attrs.get("alt")+"\\"+str(i)+".jpg")
                i=i+1
    def GetAllPageUrl(self,url):
        res=re.get(url)
        soup=BeautifulSoup(res.text, "html.parser")
        urls=soup.select("div.excerpts > article.excerpt > a.focus")
        return [a.attrs.get('href') for a in urls]

# url = "http://p3.pstatp.com/large/1f7f000336b9e639763b"
# filename = "jiang.jpg"

# spider.saveImg(url, filename)
def loop(i):
    spider=Spider()
    urls=spider.GetAllPageUrl("http://www.52rkl.cn/mengmeizi/list_51_"+str(i)+".html")
    for url in urls:
        spider.GetDeatilPage(url)

for i in range(1,3):
    threading.Thread(target=loop(i))
    threading.Thread(target=loop((i)*3+1))
    threading.Thread(target=loop((i+1)*3+1))
    threading.Thread(target=loop((i+2)*3+1))
    threading.Thread(target=loop((i+3)*3+1))
    threading.Thread(target=loop((i+4)*3+1))
    threading.Thread(target=loop((i+5)*3+1))
    threading.Thread(target=loop((i+6)*3+1))
print("成功")
