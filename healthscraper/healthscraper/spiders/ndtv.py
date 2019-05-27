# -*- coding: utf-8 -*-
import scrapy


class NdtvSpider(scrapy.Spider):
    name = 'ndtv'
    allowed_domains = ['www.ndtv.com/health']
    start_urls = ['http://www.ndtv.com/health/page-{i}'.format(i=i) for i in range(1,15)]

    def parse(self, response):

        titles = response.xpath('//div[@class="nstory_header"]/a/text()').extract()
        urls = response.xpath('//div[@class="nstory_header"]/a/@href').extract()
        image_links = response.xpath('//*[(@id = "ins_storylist")]//img/@src').extract()
        summaries = response.css('.nstory_intro::text').extract()

        for item in zip(titles,urls,image_links,summaries):
           scraped_info = {
               'title' : item[0],
               'url' : item[1],
               'image_link' : item[2],
               'summary' : item[3]
           }

           yield scraped_info
		