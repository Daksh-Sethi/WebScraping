import scrapy
import json
from ..items import HmTshirtsItem

class TshirtsSpider(scrapy.Spider):
    name = "hm"
    allowed_domains = ["www2.hm.com"]
    start_urls = ["https://www2.hm.com/en_in/men/shop-by-product/tshirts-tank-tops.html?sort=stock&image-size=small&image=model&offset=0&page-size=400"]

    def parse(self, response):
        
        links = response.css('a.link::attr(href)').extract()
        print(len(links))


        for link in links:
            yield scrapy.Request(url=response.urljoin(link),callback=self.parse_item)

    def parse_item(self, response):
        script_content= response.css('script#product-schema::text').get()
        item=HmTshirtsItem()
        if script_content:
            json_data = json.loads(script_content)
            
            
            item['name'] = json_data.get('name'),
            item['color']= json_data.get('color'),
            item['description']= json_data.get('description'),
            item['sku']= json_data.get('sku'),
            item['brand']= json_data.get('brand', {}).get('name'),
            item['price'] = json_data.get('offers', [{}])[0].get('price')
            item['availability']= json_data.get('offers',[{}])[0].get('availability').split('/')[-1]

            yield item