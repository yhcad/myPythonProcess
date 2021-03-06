#date:2018.11.29
#issue:check image before download

from html_parser import HtmlParser
from download import Download
from url_manager import UrlManger
from save_results import SaveResult

class SpiderImages():
	
	#init all instance
	def __init__(self):
		self.download = Download()
		self.htmlparser = HtmlParser()
		self.urlmanager = UrlManger()
		self.saveresult = SaveResult()
	
	def run(self,urls):
		i = 1	
		for url in urls:
			file_dir = url.split('/')[-1]
			self.urlmanager.add_new_url(url)

			while self.urlmanager.has_new_url():
				
				new_url = self.urlmanager.get_new_url()
				
				html_cont = self.download.download(new_url)
				
				new_urls,name,html_cont,t = self.htmlparser.parser(html_cont)
				#print(name)
				
				self.urlmanager.add_new_urls(new_urls)
				
				self.saveresult.save(html_cont,file_dir,name,t)
				print("{} {}".format(i,new_url))
				if i == 100:
					break
				i += 1	
			
			
	def main(self,url):
		#self.craw(url)
		self.run(url)
		
url = ["https://www.jianshu.com/p/cafdb41e186a","https://www.jianshu.com/p/d2a1490c785c","https://www.jianshu.com/p/cce86949fc9a"]
spider = SpiderImages()
spider.main(url)
		
		
