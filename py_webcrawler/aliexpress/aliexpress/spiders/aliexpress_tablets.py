# -*- coding: utf-8 -*-
import scrapy


class AliexpressTabletsSpider(scrapy.Spider):
    name = 'aliexpress_tablets'
    #allowed_domains = ['https://www.aliexpress.com/category/200216607/tablets.html']
    #start_urls = ['http://https://www.aliexpress.com/category/200216607/tablets.html/',
                #'https://www.aliexpress.com/category/200216607/tablets/2.html?site=glo&g=y&tag=']

    allowed_domains = ['tecnoblog']
    start_urls = ['http://tecnoblog.net/']

    # Modo recursivo seguindo links
    def parse(self, response):
        for article in response.css('article'):
            link = article.css('div.texts h2 a::attr(href)').extract_first()
            # prices = response.css('span.price--big span::text').extract()

            # seguindo o link
            yield response.follow(link, self.parse_article)

        next_page = response.css('a#mais::attr(href)').extract_first()
        if next_page is not None:
            yield response.css(next_page, self.parse)

    def parse_article(self, response):
        link = response.url
        title = response.css('title::text').extract_first()
        author = response.css('span.author::text').extract_first()
        text = ''.join(response.css('div.entry::text').extract())

        yield {
        'link':link,
        'title':title,
        'author':author,
        'text':text
        }
    # def parse(self, response):
    #     print('processing...', response.url)
    #     for article in response.css('article'):
    #         link = article.css('div.texts h2 a::attr(href)').extract()
    #         title = article.css('div.texts h2 a::text').extract_first()
    #         author = article.css('div.texts div.info a::text').extract_first()
    #
    #     yield {'link': link, 'title': title, 'author': author}



        # extracting py_data using css
        #product_name = response.css('.product::text').extract()
        #price_range = response.css('.value::text').extract()

        # extracting py_data using xpath
        #orders = response.xpath('//em[@title="Total Orders"]/text()').extract()
        #name_company = response.xpath('//a[@class="store $p4pLog"]/text()').extract()

        # compact using zip
        #row_data = zip(product_name, price_range, orders, name_company)

        # make py_data extracted row wise
        # for item in row_data:
        #     # create a dictionary to store ths scraped info
        #     scraped_info = {
        #         'page': response.url,
        #         'product_name': item[0],
        #         'price_range': item[1],
        #         'orders': item[2],
        #         'name_company': item[3]
        #     }
        #
        #     yield scraped_info # function generator
