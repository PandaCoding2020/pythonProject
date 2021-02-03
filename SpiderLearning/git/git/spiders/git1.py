import scrapy


class Git1Spider(scrapy.Spider):
    name = 'git1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/PandaCoding2020']

    def start_requests(self):
        url = self.start_urls[0]

        temp ='_octo=GH1.1.2143628148.1612340566; tz=Asia/Shanghai; _device_id=06f4636ee761691f01ef3e2bf0901811; has_recent_activity=1; user_session=vAUqsIM5MwS0pvtfC61E1fn-ZB67AKMEty87V1LeyUK-kk29; __Host-user_session_same_site=vAUqsIM5MwS0pvtfC61E1fn-ZB67AKMEty87V1LeyUK-kk29; tz=Asia/Shanghai; logged_in=yes; dotcom_user=PandaCoding2020; _gh_sess=G1fTio4MO+IWFfqnDLcWNDH+jEZO82g2lsOB5Y9hMQYlwlQiFeULLgCHGl+SNCHOLuctbE/FunHS/SbJcJcseb+NcUIngFOIFYuGQMZ+QMlsd8HSD0xnspeGcKMg6Fz+qppIXjqjaiHhkMojD7MqbvHwFwYH+JBNlhKI5FX2Yhc2B9jB3V0piSORbGDBAxRui10FzNeEohKKi+lGPujq0+VMy96/RqbCcbYqQGSfDhbnAUZJqRf5wMp+vN2/BvcNt3aRu8C/yB+oAuhficjy0JNYwTUmQG8sb7Jzb2HW0rnq/fvLDs8zv8yP5GB6NQCCZo07JjDTzQ5f2URi0ANasbnq3zHJKNsaNvIqWLseDxo/HeejvTrE3nDKnDRESP+4vLeFM5jsvT36hy4kPiRWyjonDm7A55TUsk9lxqVEzlTMNgmdGHPN6B8qBqEqBFMGKnFQ0LQiq5QSWC7CDie9KmV2DPSO1I1dAuklr+82fyJXG8G8KCo9IMQw7ou9OOV/ozV55h87yFVFSVaSbEZnUuDAqEIdCBW0UhNBVaR9P3kUFYrLbCQpIMeK0LvxFn8fH7ITVvvkRGsa9Wkq6QpPPKrR7K5HXVhOwmYCmSwZeWpGEl8BlPSUsvZRyq0lmLqVI1GeE4rmkAgY1WWAFqhyA+zYNBta7XIjjYauXVM4rjy8CWNMbjMwqHTKmdrJvY3XD4gn1Zoa5GoSm3i/TKqL2Jkh6kHDVj2328rNHjVzlGgZj9sALT5XopKmhvLPtc0eQoNdFZ/eTo+KIPHnmLcSAtU7Hptoog94WutpOMx9X1bkr9j5Smrrovx5JXYuLD2xmdpLhiSHA90aAtcv/goR5YqDe5DuqZbS14ihy8YBtJOLZ96bjA8mMQ//VAGrfRsxE+Q10ZxW2ZhL5+V2zw0ZBuk0KEeH5E5rGLoJrxYd5uctP/qWKMmCeVKWJNvdtvYvkKIZHixmWAsCEjfIAspeBfHD0erIfl2/GDZ5usPmF1EkpBa+/RAvQLjIfp4o0ViT2+gQl3tWIK2m316zHOjcGXgzHrR2yA/oZ6mqfm2+Df7nm6E2t04jVyIVI9cBDsdW90dQ+uP0ClLZRqo/eLmYmw==--BGIOen38O+5P04D4--fCI9QoUQZHUghee03ebJOw=='

        cookies = {data.split('=')[0]: data.split('=')[-1] for data in temp.split('; ')}

        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies
        )
    def parse(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())