import requests
from lxml import etree
import pymysql

# 链接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='meng')
# 设置字符编码
db.set_charset('utf8')
# 创建游标对象, 用于执行sql语句
cursor = db.cursor()


url = 'http://www.rensheng5.com/gushihui/gshxh/'
headers = {
	'User-Agent':
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		'Chrome/119.0.0.0 Safari/537.36'
}

resp = requests.get(url, headers=headers)
resp.encoding = 'gbk'
html = etree.HTML(resp.text)
url_list = html.xpath('//ul[@class="p7"]/li/a/@href')
for url in url_list:
	resp = requests.get(url)
	resp.encoding = 'gbk'
	html = etree.HTML(resp.text)
	title = str(html.xpath('//h1/text()')[0])
	print(title)
	print(type(title))
	content = ''.join(html.xpath('//div[@class="artbody"]/p/text()'))
	print(type(content))
	print(content)
	try:
		# 把标题和内容写入数据库内
		sql = f'insert into story values(null, "{title}", "{content}")'
		cursor.execute(sql)
		db.commit()
		print('写入完成')
	except:
		db.rollback()

sql = 'select * from story'
cursor.execute(sql)
print(cursor.fetchall())
db.close()