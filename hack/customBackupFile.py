#python3

def getKeys(url):
	keyList = ['web','webroot','WebRoot','website','www','wwww','www1','www2','www3','www4','www5','default','log','elk','weblog',
'mysql','ftp','FTP','MySQL','redis','Redis','sa','cig','access','error','logs','data','database','sql','vpn','proxy','temp',]
	
	num1 = url.find('.')#5,
	num2 = url.find('.', num1 + 1)#9
	keyList.append(url[num1 + 1:num2])#主域名名称小写
	keyList.append(url[num1 + 1:num2].upper())#主域名名称大写
	keyList.append(url)  #域名
	keyList.append(url.upper())#域名大写
	keyList.append(url.replace('.', '_'))  #点换下划线,www_baidu_com
	keyList.append(url.replace('.', '_').upper())#点换下划线,大写WWW_BAIDU_COM
	keyList.append(url.replace('.', ''))  # 点换空格wwwbaiducom
	keyList.append(url.replace('.', '').upper())# 点换空格，大写WWWBAIDUCOM
	keyList.append(url[num1 + 1:])  #主域名baidu.com
	keyList.append(url[num1 + 1:].upper())#主域名大写BAIDU.COM
	keyList.append(url[num1 + 1:].replace('.', '_'))  #主域名.换_ 小写：baidu_com
	keyList.append(url[num1 + 1:].replace('.', '_').upper())#主域名.换_ 小写：BAIDU_COM
	return keyList


def getBackupFile(fname,keys):
	f=open(fname,"a+")
	suffix = ['.rar','.zip','.sql','.gz','.tar','.ba2','.tar.bz2','.bak','.dat','.txt','.mdb','.doc','.lst','.tmp','.temp','.xml']
	for key in keys:
		for suff in suffix:
			f.write(key+suff+"\n")
	f.close()
	print("done")


target="www.baidu.com"
fname="CustomBackupFile_"+target+".txt"
getBackupFile(fname,getKeys(target))
