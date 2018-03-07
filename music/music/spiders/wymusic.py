# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from music.items import MusicItem


class WymusicSpider(CrawlSpider):
    name = 'wymusic'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/discover/'), follow=True),
        Rule(LinkExtractor(allow=r'/artist'), follow=True),
        Rule(LinkExtractor(allow=r'/song'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MusicItem()
        print(response.url)
        mete = response.xpath('/html/head/meta[7]/@content').extract()
        print(mete)
        sid = re.findall(re.compile(r'id=([0-9]{1,20})'), response.url)
        name = re.findall(re.compile(r'歌手：(.*?)。'), "".join(mete))
        belong = re.findall(re.compile(r'所属专辑：(.*?)。'), "".join(mete))
        print(name, belong)

        item["song_id"] = "".join(sid)
        item["down_url"] = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format("".join(sid))

        item["name"] = "".join(name)
        item["belong"] = "".join(belong)

        return item
