import scrapy
import re

class Git2Spider(scrapy.Spider):
    name = 'git2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # 从登陆页面响应中解析
        token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        post_data = {
            "commit": "Sign in",
            "authenticity_token": token,
            "login": "PandaCoding2020",
            "password": "zzz828168",
            "webauthn-support": "supported"
        }

        print(post_data)

        # 针对登陆usl发送post请求
        yield scrapy.FormRequest(
            url='https://github.com/session',
            callback=self.after_login,
            formdata=post_data
        )

    def after_login(self, response):
        yield scrapy.Request('https://github.com/PandaCoding2020', callback=self.check_login)

    def check_login(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())
