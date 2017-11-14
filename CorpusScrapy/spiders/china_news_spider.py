#!/user/bin/env python3
# -*- coding: utf-8 -*-
# Created by Wang Haoyu on 2017/11/13

import scrapy
import datetime
import logging
import re
from CorpusScrapy.items import NewsItem

class ChinaNewsSpider(scrapy.Spider):
    name = 'chinanews'

    main_domain = 'http://www.chinanews.com/'
    scroll_domain = 'http://www.chinanews.com/scroll-news/'

    def __init__(self):
        super().__init__(self)
        self.title = dict()

    def start_requests(self):
        start_date = (2017, 11, 13)
        for url in self.url_generator(start_date):
            yield scrapy.Request(url=url,
                                 callback=self.parse)

    def url_generator(self, date):
        end_date = datetime.date.today()
        cur_date = datetime.date(date[0], date[1], date[2])

        while cur_date <= end_date:
            temp = str(cur_date).split('-')
            url = '%s/%s/%s%s/news.shtml' % (self.scroll_domain,
                                             temp[0], temp[1], temp[2])
            yield url
            cur_date += datetime.timedelta(1)

    def parse(self, response):
        new_xpath_query = '//*[@id="content_right"]/div[3]/ul/li/div[2]/a/@href'
        title_xpath_query = '//*[@id="content_right"]/div[3]/ul/li/div[1]/a/text()'

        link_list = response.xpath(new_xpath_query).extract()
        class_list = response.xpath(title_xpath_query).extract()

        for news_url, article_class in zip(link_list, class_list):
            url = response.urljoin(news_url)
            yield scrapy.Request(url=url,
                                 callback=lambda: self.page_parse(response, article_class))


    def page_parse(self, response, article_class):
        content_query = '//p/text()'
        if article_class not in self.title:
            if not article_class or len(article_class.strip()) <= 0:
                article_class = '其他'
            self.title[article_class] = 0

        self.title[article_class] += 1

        content = ''.join(response.xpath(content_query).extract())
        content = re.sub(r'\s', '', content)
        title = '%s-%d.txt' % (article_class, self.title[article_class])
        title = re.sub(r'\s', '', title)

        item = NewsItem()
        item['title'] = title
        item['content'] = content
        yield item





