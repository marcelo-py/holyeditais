import scrapy


class EditaisiFMA(scrapy.Spider):
    name = 'editais'
    start_urls = ['https://sjpatos.ifma.edu.br/concursos-e-seletivos/']

    def parse(self, response):
        editais = response.xpath('*//div[@class="row-fluid page-editais--edital"]')
        for edital in editais:
            yield {
                'titulo': edital.xpath(
                    '*//a/h2[@class="page-editais--edital__titulo"]/text()').get().replace('\n', '').strip(),
                'descricao': edital.xpath(
                    './/div[@class="page-editais--edital__descricao page-editais--'
                    'edital__descricao--3-linhas"]/text()').get().replace('\n', '').replace('\r', ' ').strip(),
                'postado': edital.xpath(
                    '*//div[@class="page-editais--edital__informacoes"]'
                    '/ul/li/text()').getall()[1].replace('\n ', '').strip(),
                'status': edital.xpath(
                    '*//div[@class="page-editais--edital__informacoes"]/ul/li/'
                    'span[@class="page-editais--edital__situacao--verde"]/text()').get()
            }

        proxima_pagina = response.xpath('*//div[@class="pagination"]/a[@class="next page-numbers"]/@href').get()
    #executa a primeira pagina acabou os editais nela ele executa a proxima pagina e volta a fazer denovo com o callback chamadno o parse
    #Acontece recursivamente até não encontrar mais uma pagina com edital(tais)
        if proxima_pagina is not None:
            yield scrapy.Request(proxima_pagina, callback=self.parse)

