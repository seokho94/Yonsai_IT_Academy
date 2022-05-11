import pandas as pd
import pyupbit as upbit
from threading import Thread
from datetime import datetime

##Top_coin -> UI에 출력하기 위한 코인 이름과 심볼에 대한 Dictionary
##Target_coin -> 필요한 정보들 호출을 위한 리스트
Top_coin = {"BTC" : "비트코인" , "ETH" : "이더리움", "XRP" : "리플", "SOL" : "솔라나", "ADA" : "에이다", "DOGE" : "도지코인", "AVAX" : "아발란체",  "DOT" : "폴카닷", "TRX" : "트론", "MATIC" : "폴리곤"}

Target_coin = ["KRW-BTC","KRW-ETH","KRW-XRP","KRW-SOL","KRW-ADA","KRW-DOGE","KRW-AVAX","KRW-DOT","KRW-TRX","KRW-MATIC"]

##current Price 호출 함수
def Call_current(target) :
    return upbit.get_current_price([target])


##증감계산식 : (현재가 - 전날종가) / 전날종가 * 100
def Rate_current(target) :
    close_price = Yesterday_price(target)
    return ((upbit.get_current_price([target])-close_price)/close_price)*100

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
    return Volume[0]

##코인 이름과 심볼 출력
def print_name(target):
    name = target[4:]
    return Top_coin[name] + "(" + name + ")"

def data_input(data) :
    for target in Target_coin :
        data.append([print_name(target),Call_current(target),Rate_current(target),Today_volume(target)])
    return data

def total() :
    data = [['코인이름', '현재가', '전일대비', '거래대금']]
    data = data_input(data)
    return data
    
output_data = total()