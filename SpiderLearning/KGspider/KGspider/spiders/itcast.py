import scrapy
from KGspider.items import KgspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 2.检查域名
    allowed_domains = ['itcast.cn']
    # 1.修改起始url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']
    # 3.在parse中实现爬取逻辑
    def parse(self, response):
        # 定义对于网站的相关操作
        # with open('itcast.html','wb') as f:
        #     f.write(response.body)
        # 获取所有教师结点
        node_list = response.xpath('//div[@class = "li_txt"]')
        # print(len(node_list))
        # 遍历教师结点列表
        data_list = []
        for node in node_list:
            # temp = {}
            item = KgspiderItem()
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()').extract_first()
            item['desc'] = node.xpath('./p/text()').extract_first()

            # xpath结果只含有一个值的列表，可以使用extract_first()，如果为多个值，则用extract()
            yield item
