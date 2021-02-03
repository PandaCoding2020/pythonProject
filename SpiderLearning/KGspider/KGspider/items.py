# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KgspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()


if __name__ == '__main__':
    item = KgspiderItem()
    item['name'] = '王老师'
    item['title'] = '王老师'
    item['desc'] = '王老师'

    print(item)
