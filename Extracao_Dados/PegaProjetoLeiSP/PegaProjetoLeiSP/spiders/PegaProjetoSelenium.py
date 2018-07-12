# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep

class PegaprojetoseleniumSpider(Spider):
    name = 'PegaProjetoSelenium'
    allowed_domains = ['documentacao.camara.sp.gov.br/cgi-bin/wxis.bin/iah/scripts/?IsisScript=iah.xis&form=A&format=standard.pft&navBar=OFF&hits=200&lang=pt&nextAction=search&base=proje&conectSearch=init&exprSearch=%22PROJETO%20DE%20LEI%22&indexSearch=%5EnCm%5ELTipo+de+projeto%5Etshort%5Ex%2F20%5EyDATABASE']
 


    def start_requests(self):
    	self.driver = webdriver.Chrome('/home/jordanmalheiros/chromedriver')
    	self.driver.get('http://documentacao.camara.sp.gov.br/cgi-bin/wxis.bin/iah/scripts/?IsisScript=iah.xis&form=A&format=standard.pft&navBar=OFF&hits=200&lang=pt&nextAction=search&base=proje&conectSearch=init&exprSearch=%22PROJETO%20DE%20LEI%22&indexSearch=%5EnCm%5ELTipo+de+projeto%5Etshort%5Ex%2F20%5EyDATABASE')

    	sel = Selector(text=self.driver.page_source)
    	links = sel.xpath('.//a/@href').extract()

    	for link in links:
    		if '/iah/fulltext/' in link:
    			url = 'http://documentacao.camara.sp.gov.br/' + link
    			yield Request(url, callback=self.parse_link)

    	#PEGA OS LINKS DOS PDF'S DA PAGINA 2-800
    	for i in range(2,800):
    		next_page = self.driver.find_element_by_xpath('//*[@name="Page' + str(i) + '"]')
    		sleep(1)
    		next_page.click()

    		sel = Selector(text=self.driver.page_source)
    		links = sel.xpath('.//a/@href').extract()
    		for link in links:
    			if '/iah/fulltext/' in link:
   						url = 'http://documentacao.camara.sp.gov.br/' + link
   						yield Request(url, callback=self.parse_link)
	

    def parse_link(self, response):
        url = response.request.url
        yield {'url': url}



