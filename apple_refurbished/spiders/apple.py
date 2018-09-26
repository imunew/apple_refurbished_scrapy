# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from apple_refurbished.items import AppleRefurbishedItem


class AppleSpider(scrapy.Spider):
    name = "apple"
    allowed_domains = ["www.apple.com"]
    start_urls = [
        'http://www.apple.com/jp/shop/browse/home/specialdeals/mac',
        'http://www.apple.com/jp/shop/browse/home/specialdeals/ipad',
        'http://www.apple.com/jp/shop/browse/home/specialdeals/ipod'
    ]

    def parse(self, response):
        parent_node_xpaths = [
            u'//div[@id="promo-bar"]//ul/li',
            u'//div[contains(@class, "refurb-list")]//table//h3'
        ]
        for xpath in parent_node_xpaths:
            for element in response.xpath(xpath):
                item_path = element.xpath('.//a/@href').extract_first()
                yield Request(
                    url=response.urljoin(item_path),
                    callback=self.parse_item
                )

    @staticmethod
    def parse_item(response):
        item = AppleRefurbishedItem()
        item['title'] = response.xpath(u'//div[@id="title"]/h1/text()').extract_first().strip()
        item['link'] = response.url
        item['price'] \
            = response.xpath(u'normalize-space(//span[@class="current_price"])').extract_first()
        yield item
