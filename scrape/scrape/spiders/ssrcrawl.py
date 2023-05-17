import os
import time
from urllib.parse import urljoin

import scrapy

from ..items import movie


class SsrcrawlSpider(scrapy.Spider):
    name = "ssrcrawl"
    custom_settings = dict(
        DOWNLOAD_DELAY=0.5,
        LOG_LEVEL=os.environ.get("LOG_LEVEL", "DEBUG"),
    )
    allowed_domains = []

    # start_urls = []
    def start_requests(self):
        for i in range(1, 100):
            for i in range(1, 11):
                url = f"https://ssr1.scrape.center/page/{i}"
                yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        divs = response.css("#index .el-col.el-col-18.el-col-offset-3 >div")
        for div in divs:
            name = div.css("a.name h2::text").get()
            page_url = div.css("a.name::attr(href)").get()
            page_url = urljoin(response.url, page_url)
            score = div.css(".score.m-t-md.m-b-n-sm::text").get()
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            item = movie()
            item["page_url"] = page_url
            item["name"] = name
            item["create_time"] = create_time
            item["score"] = score.strip()
            yield item
