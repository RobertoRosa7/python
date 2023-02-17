# -*- coding: utf-8 -*-
import scrapy


def parse(response):
  prices = response.css('span.price--big span::text').extract()
  yield {'prices': prices}


class BuscapePriceDellSpider(scrapy.Spider):
  name = 'buscape_price_dell'
  allowed_domains = ['https://www.buscape.com/notebook/dell']
  start_urls = ['https://www.buscape.com/notebook/dell/']
