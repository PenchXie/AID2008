# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    issued_time = scrapy.Field()
    responsibility = scrapy.Field()
    requirement = scrapy.Field()