# -*- coding: utf-8 -*-

# Scrapy settings for music project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music'

SPIDER_MODULES = ['music.spiders']
NEWSPIDER_MODULE = 'music.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'music (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
DEFAULT_REQUEST_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        # "Cookie": "_ntes_nnid=825b4dc594d9317b392b5eb07d3340c5,1512955897763; _ntes_nuid=825b4dc594d9317b392b5eb07d3340c5; _iuqxldmzr_=32; vjuids=-3b1da70ef.1605e5e08c4.0.807cbde916537; __e_=1514512434019; usertrack=ezq0pVppmc9QPg7nBDMgAg==; _ga=GA1.2.1180874737.1516870099; mail_psc_fingerprint=968fe8952daea2f8e6ef7990514c74d4; __gads=ID=63e18c04aae884a8:T=1517208778:S=ALNI_MZro7wT4DGlaDmAKLhNRZ0_9JBpPw; UM_distinctid=16140b0bad52f7-0e65b8ef44c77f-4323461-1fa400-16140b0bad6e7a; __f_=1517561993329; Province=0349; City=0351; P_INFO=jakejie@163.com|1519709982|0|other|00&99|shx&1519692896&other#shx&140100#10#0#0|&0|imooc|jakejie@163.com; __utmz=94650624.1519714396.2.2.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/sunhuaqiang1/article/details/72821694; vjlast=1513411709.1519883768.11; vinfo_n_f_l_n3=f7ace340dffdbaba.1.3.1513411709138.1519629164475.1519883964657; JSESSIONID-WYYY=6Uk0GtEqOGGI5whotQ2ZDQobgGnQ8gO05vnNRMUaMqJtaI%2BIWjvR9meoH1HoUsdXhKORCJkqAlR5SvNf7xpaT3aZ5D733m6SkVCfDUvZPJeImnaav088RVNFvZ0U%2FTggkiMVvD%2B5%2BoFs%2B7fSoAXZeYSkKbJQKM6YdDbZjSH%5C9b3Z%5CO%5Cr%3A1520391285024; __utma=94650624.1976315094.1512955900.1519714396.1520389485.3; __utmc=94650624; __utmb=94650624.19.10.1520389485",
        "Host": "music.163.com",
        "Pragma": "no-cache",
        "Referer": "http://music.163.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'music.middlewares.MusicSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'music.middlewares.MusicDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'music.pipelines.MusicPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
