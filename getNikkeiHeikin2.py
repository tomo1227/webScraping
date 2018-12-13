#coding: UTF-8

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time

time_flag = True

#永久に実行する
while True:

    #時間が59分以外の場合は58秒待機する
    if datetime.now().minute != 59:
        time.sleep(58)
        continue

    #csvを追記モードで開く
    f = open('nikkei_heikin.csv', 'a')
    writer = csv.writer(f, lineterminator = '\n')

    while datetime.now().second != 59:
        time.sleep(1)

    # 処理が早く終わり二回繰り返してしまうのでここで一秒間待機します
    time.sleep(1)

    #csvに記述するレコードの作成
    csv_list = []

    #現在の時刻の取得(年月日時分秒)
    time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    #1カラム目に時間を挿入
    csv_list.append(time_)

    #アクセスするURL
    url = "http://www.nikkei.com/markets/kabu/"

    # URLにアクセスする htmlが帰ってくる
    html =requests.get(url)

    #htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html.text, 'html.parser')

    # span要素全てを摘出する→全てのspan要素が配列に入ってかえされます
    span = soup.find_all('span')

    #print時のエラーとならないように最初に宣言しておきます。
    #nikkei_heiking: str

    for tag in span:
        # classの設定がされていない要素は、tag.get("class").pop(0)を
        #行うことのできないでエラーとなるため、tryでエラーを回避する
        try:
            # tagの中からclass="n"のnの文字列を摘出します。
            #複数classが設定されている場合があるのでget関数では配列で帰ってくる。
            #そのため配列の関数pop(0)により、配列の一番最初を摘出する
            # <span class="hoge" class="foo">  →   ["hoge","foo"]  →
            # hoge
            string_ = tag.get('class').pop(0)

            # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを
            #調べます
            if string_ in "mkc-stock_prices":
                # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を
                #.stringであぶり出します
                nikkei_heikin = tag.string
                break
        except:
            pass #何も処理しない

    # 摘出した日経平均株価を出力
    print (time_, nikkei_heikin)

    # 2カラム目に日経平均を記録
    csv_list.append(nikkei_heikin)

    # csvに追記
    write.writerow(csv_list)

    f.close()
