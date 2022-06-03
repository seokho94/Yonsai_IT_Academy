from tracemalloc import stop
import pandas as pd
import pyupbit as upbit
from threading import Thread, Timer
import threading
from datetime import datetime
import logging
import time

##Top_coin -> UI에 출력하기 위한 코인 이름과 심볼에 대한 Dictionary
##Target_coin -> 필요한 정보들 호출을 위한 리스트
Top_coin = {"BTC" : "비트코인" , "ETH" : "이더리움", "XRP" : "리플", "SOL" : "솔라나", "ADA" : "에이다", "DOGE" : "도지코인", "AVAX" : "아발란체",  "DOT" : "폴카닷", "TRX" : "트론", "MATIC" : "폴리곤"}

##데이터를 찾기 위한 키 값
Target_coin = upbit.get_tickers()

##UI 출력을 위한 데이터 리스트
output_data = []

##Thread 종료 판별 Bool 함수
isView = False

##current Price 호출 함수
def Call_current(target) :
    return upbit.get_current_price([target])


##증감계산식 : (현재가 - 전날종가) / 전날종가 * 100
def Rate_current(target) :
    close_price = Yesterday_price(target)
    current_price = Call_current(target)
    return str(round((((current_price)-close_price)/close_price)*100, 2))+'%'

##전날 종가를 출력
def Yesterday_price(target) :
    ticker = target
    interval = 'day'
    to = datetime.today().strftime('%Y-%m-%d')
    count = 1
    target = upbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count = count)
    close_price = target['close']
    return close_price[0]

##pyupbit volume 값을 활용하여 거래대금 호출
def Today_volume(target) :
    ticker = target
    interval = 'minute1'
    count = 1
    Volume_data = upbit.get_ohlcv(ticker=ticker, interval=interval, count = count)
    Volume = Volume_data['volume']
    volume_cor = Volume[0]
    return str(round(volume_cor, 4))

##코인 이름과 심볼 출력
def print_name(target):
    name = target[4:]
    return str(Top_coin[name] + "(" + name + ")")

def data_input(data) :
    global Target_coin
    for target in Target_coin :
        data.append([print_name(target),str(Call_current(target)),Rate_current(target),Today_volume(target)])
        time.sleep(0.1)
    return data

def total() :
    global output_data
    output_data = []
    data = [['코인이름', '현재가', '전일대비', '거래대금']]
    data = data_input(data)
    output_data = data
    return output_data

# def thread_run():
#     global count 
#     total()
#     print(output_data)
#     count = count + 1
#     update = threading.Timer(3, thread_run)
#     if(count>=50) : update.cancel()
#     update.start()
    
##total()


