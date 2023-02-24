#导入 urllib库的request模块
import urllib.request
#指定要抓取的网页url，必须以http开头的
url = r'http://fund.eastmoney.com/340007.html?spm=search'
#调用 urlopen（）从服务器获取网页响应（respone），其返回的响应是一个实例
res = urllib.request.urlopen(url)
#调用返回响应示例中的read（）函数，即可以读取html，但需要进行解码，具体解码写什么，要在你要爬取的网址右键，查看源代码
html = res.read().decode('utf-8')
print(html)
