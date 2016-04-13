import scrapy
import json

from ra_scrape.items import RaScrapeItem

class RaScrapeSpider(scrapy.Spider):
    name = "ra_scrape"
    allowed_domains = ["remote-associates-test.com"]
    start_urls = [
            "http://www.remote-associates-test.com/"
    ]

    def parse(self, response):
        for sel in response.xpath('//tr'):
            item = RaScrapeItem()
            item['prompt'] = sel.xpath('td[@style="padding-top:13px"]/a/text()').extract()
            item['answer'] = sel.xpath('td/span[@class="solution hidden"]/text()').extract()
            item['difficulty'] = sel.xpath('td/span[contains(@class, "label")]/text()').extract()
            print "Prompt: {0} \n\t Ans: {1} \n\t Diff: {2}".format(item['prompt'], item['answer'], item['difficulty'])
            yield item
