# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HmTshirtsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    sku = scrapy.Field()
    brand = scrapy.Field()
    color=scrapy.Field()
    description=scrapy.Field()
    availability=scrapy.Field()

    
