#coding: UTF-8

import feedparser
import requests
from bs4 import BeautifulSoup

# 取得するRSSのURL
RSS_URL = "https://headlines.yahoo.co.jp/rss/trendy-all.xml"

# RSSから取得する
feed = feedparser.parse(RSS_URL)

# 記事の情報をひとつずつ取り出す
for entry in feed.entries:

    # タイトルを出力
    print (entry.title)

     # URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入った
     #instanceが帰ってきます
    instance = requests.get(RSS_URL)

    # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
    soup = BeautifulSoup(instance.text, "html.parser")

    # 例としてタイトル要素のみを出力する
    print (soup.title)
