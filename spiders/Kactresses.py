# -*- coding: utf-8 -*-
import scrapy

## https://en.wikipedia.org/wiki/List_of_South_Korean_actresses
## https://en.wikipedia.org/wiki/List_of_South_Korean_male_actors
## https://reelrundown.com/celebrities/The-20-Most-Successful-Highest-Paid-Korean-Drama-Actors-and-Actresses

## scrapy shell
## fetch("https://en.wikipedia.org/wiki/List_of_South_Korean_actresses")
## response.xpath("//a/text()").extract()
## response.xpath("//a/@href").extract()  -- Extract href

class KactressesSpider(scrapy.Spider):
    name = 'Kactresses'
    allowed_domains = ['en.wikipedia.org/wiki/List_of_South_Korean_actresses']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_South_Korean_actresses']

    def parse(self, response):
        a_tag = response.xpath('//a/text()').extract()
        #a_href = response.xpath("//a/@href").extract()
        
        yield{'a Tag': a_tag}
        #yield{'a href': a_href}