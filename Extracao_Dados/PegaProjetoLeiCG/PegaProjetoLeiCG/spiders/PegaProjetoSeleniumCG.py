# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep

import unicodedata


class PegaprojetoseleniumSpider(Spider):
    name = 'PegaProjetoSelenium'
    allowed_domains = ['http://sgl4.net/cmcg-consulta/consulta-projetos-form.asp']

    def start_requests(self):
    	self.driver = webdriver.Chrome('/home/jordanmalheiros/chromedriver')
    	self.driver.get('http://sgl4.net/cmcg-consulta/consulta-projetos-form.asp')

    	#Select type of projeto = 'Projeto Lei Legislativo'
    	PLL = self.driver.find_element_by_xpath('//*[@value="Projeto Lei Legislativo"]')
    	PLL.click()

    	#Select the consultar(consult) button
    	consultar = self.driver.find_element_by_xpath('//*[@value="Consultar"]')
    	consultar.click()

        last_page = self.driver.find_element_by_xpath('//*[@name="LBWEB_LASTPAGE"]')
        last_page.click()


        for j in range(330):
            #Pega numero de projetos por Pagina
            sel = Selector(text=self.driver.page_source)
            projetos = sel.xpath('//*[@class="w3-row-padding w3-border"]')
            k=3

            for i in projetos:
                ver_mais = self.driver.find_element_by_xpath('/html/body/div[' + str(k) + ']/div[2]/form/input[3]')
                k += 2
                sleep(2)
                ver_mais.click()

                sel = Selector(text=self.driver.page_source)

                ## Extract the name and concatened to the url
                link = sel.xpath('.//a/text()').extract_first()

                ###Se nao possui doc/pdf para baixar --> Pega o Texto do Projeto e transformar em utf8 -> Pegar Titulo do Projeto e transformar em utf-8 --> Armazenar em Arquivo
                
                sel = Selector(text=self.driver.page_source)
                string_nome = ''.join(sel.xpath('.//u/text()').extract())
                string_numero_projeto = ''.join(sel.xpath('.//b/text()')[2].extract())
                nome_projeto = string_nome + string_numero_projeto
                nome_projeto = nome_projeto.split(',')
                nome_projeto = nome_projeto[0]
                nome_projeto_final = ''.join(nome_projeto.replace(", de", "").replace(" ","").replace("n", "-n").replace("/", "-"))



                sel = Selector(text=self.driver.page_source)
                texto_projeto = sel.xpath('//*[@id="Demo2"]').extract()
                texto_projeto = ''.join(texto_projeto)
                texto_projeto = texto_projeto.replace("<p>", "").replace("<br>", "").replace("</p>", "").replace("</div>", "").replace('<div id="Demo2" class="w3-accordion-content w3-container w3-justify">', "")

                with open(nome_projeto_final, "wb") as f:
                    f.write(texto_projeto.encode("UTF-8"))         

                ## Voltar Pagina anterior pelo Browser
                self.driver.back()


            #Volta na Página de Projetos
            avancar = self.driver.find_element_by_xpath('//*[@name="LBWEB_PREVIOUSPAGE"]')
            sleep(2)
            avancar.click()


            
