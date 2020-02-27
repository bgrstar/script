#coding:utf-8
#飘天文学网小说爬虫,python3
import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def getRun():
	bUrl="https://www.piaotian5.com/book/16257/{}.html"
	for id in range(10464413,10466313,1):
		f=open("read.txt","a+",encoding='utf-8')
		url=bUrl.format(id);print("try: ",url)
		try:
			content=requests.get(url,headers=headers).text
			soup = BeautifulSoup(content, 'html.parser')
			temp=soup.find_all('div', class_='content')[0]
			title=temp.find('h1').text
			cContent=temp.find(id="content").text
			str1=title+"\n"+cContent
			f.write(str1)
			f.close()
			print("done",url)
		except:
			print("error",url,"\n\n\n\n")
			f.close()

getRun()


def test():
	url="https://www.piaotian5.com/book/16257/10464413.html"
	content=requests.get(url,headers=headers).text
	soup = BeautifulSoup(content, 'html.parser')
	temp=soup.find_all('div', class_='content')[0]
	title=temp.find('h1').text
	print(temp.find(id="content").text)
#test()

