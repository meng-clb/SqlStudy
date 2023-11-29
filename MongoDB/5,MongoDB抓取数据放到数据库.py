import requests
from lxml import etree
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor

# 链接数据库
conn = MongoClient('localhost')
db = conn.meng  # 选择数据库


def get_insert(url):
	try:
		resp = requests.get(url)
		resp.encoding = 'gbk'
		html = etree.HTML(resp.text)
		title = str(html.xpath('//h1/text()')[0])
		# print(title)
		# print(type(title))
		content = ''.join(html.xpath('//div[@class="artbody"]/p/text()'))
		# print(type(content))
		# print(content)
		db.story.insert_one({'title': f'{title}', 'content': f'{content}'})
		print(f'{title}写入完成')
	except:
		print(f'{url}抓取失败')


if __name__ == '__main__':
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
	with ThreadPoolExecutor(20) as t:
		t.map(get_insert, url_list)
