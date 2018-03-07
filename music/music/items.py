# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_id = scrapy.Field()
    down_url = scrapy.Field()
    name = scrapy.Field()
    belong = scrapy.Field()
    # pass
