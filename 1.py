import requests
from bs4 import BeautifulSoup
import bs4
import requests
from bs4 import BeautifulSoup
def getHTMLText(url):#获取html数据
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"
def fillUnivList(ulist, html):
    soup =BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string,])

def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
    print("Suc"+ str(num))
def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    b = printUnivList(uinfo,20)
    with open(r'C:\Users\adam\Desktop\data.txt','r+') as f:
        print(b, file=f)
    file_handle.close()
main()
