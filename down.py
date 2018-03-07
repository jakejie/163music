# coding:utf-8

import requests


def download(sid, name):
    """根据 sid 下载歌曲并保存为 name.mp3"""
    url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(sid)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Referer': url,
    }
    r = requests.get(url, headers=headers)
    print("begin to save {}.mp3...".format(name))
    with open(name + '.mp3', 'wb') as f:
        f.write(r.content)
    print("{}.mp3 has been saved...\n==================".format(name))


# download(528273169, '000')

def test():
    headers = {
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

    url = "http://music.163.com/song?id=528273169"

    response = requests.get(url, headers=headers)
    print(response.text)
    """
    获取评论信息 
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(song_id)
    个人信息
    url = "http://music.163.com/song?id=528273169"
    下载地址
    url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(sid)
    """


test()
