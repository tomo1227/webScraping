#coding UTF-8
#日本経済新聞のページタイトルの抽出

import urllib3
import requests
from bs4 import BeautifulSoup

#アクセスするURL
url = "http://www.nikkei.com/"

#URLにアクセスする htmlが帰ってくる(requestの場合)

html = requests.get(url)

#htmlをBeatilfulSoupで扱う

soup = BeautifulSoup(html.text, 'html.parser')


#http = urllib3.PoolManager()
#html = http.request('GET', url)
#soup = BeautifulSoup(html.data, 'html.parser')

#タイトル要素を取得する
title_tag = soup.title

#要素の文字列を取得する
title = title_tag.string

#タイトル要素を出力
print (title_tag)

#タイトルの文字列を出力
print (title)
