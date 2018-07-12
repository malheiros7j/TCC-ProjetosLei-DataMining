# -*- coding: utf-8 -*-

from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request

from time import sleep


class PegaprojetoseleniumSpider(Spider):

    name = 'PegaProjetoSelenium'
    allowed_domains = ['www.cmm.am.gov.br/tipo-leis-projetos/projeto-lei/']


    def start_requests(self):
    	self.driver = webdriver.Chrome('/home/jordanmalheiros/chromedriver')
    	self.driver.get('http://www.cmm.am.gov.br/tipo-leis-projetos/projeto-lei/')

    	sel = Selector(text=self.driver.page_source)
    	links = sel.xpath('.//td/a/@href').extract()

    	for link in links:
    		url = '' + link
    		yield Request(url, callback=self.parse_link)

    	for i in range (105):
    		next_page = self.driver.find_element_by_xpath('//*[@class="next page-numbers"]')
    		sleep(1)
    		next_page.click()
    	
    		sel = Selector(text=self.driver.page_source)
    		links = sel.xpath('.//td/a/@href').extract()
    		for link in links:
    			url = '' + link
    			yield Request(url, callback=self.parse_link)

    def parse_link(self,response):
    	url = response.request.url
    	yield {'url' : url }

    		






   





