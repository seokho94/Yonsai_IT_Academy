from Current_price import Yesterday_price
import request_test as req
from datetime import datetime
import time
import threading

##Top_coin -> UI에 출력하기 위한 코인 이름과 심볼에 대한 Dictionary
##Target_coin -> 필요한 정보들 호출을 위한 리스트
Top_coin = {"BTC" : "비트코인" , "ETH" : "이더리움", "XRP" : "리플", "SOL" : "솔라나", "ADA" : "에이다", "DOGE" : "도지코인", "AVAX" : "아발란체",  "DOT" : "폴카닷", "TRX" : "트론", "MATIC" : "폴리곤"}

##데이터를 찾기 위한 키 값
Target_coin = ["KRW-BTC","KRW-ETH","KRW-XRP","KRW-SOL","KRW-ADA","KRW-DOGE","KRW-AVAX","KRW-DOT","KRW-TRX","KRW-MATIC"]

count = 0;

def return_data() :
    data = [['코인이름', '현재가', '전일대비', '거래대금']]
    curDate = datetime.today().strftime('%Y-%m-%d')
    for target in Target_coin :
        
        coinName = target[4:]
        currentPrice = req.request_data('current', target)
        YesterdayPrice = req.request_data('ohlcv', target, 'day', curDate, 1)['close'][0]
        DtD = round(((currentPrice-YesterdayPrice)/YesterdayPrice)*100, 2)
        Volume = round(req.request_data('ohlcv',target)['volume'][0], 4)
        data.append([coinName, currentPrice, DtD, Volume])
        time.sleep(0.1)
    return data

def thread1() :
    global count
    output_data = return_data()
    for i in range(len(output_data)) :
        print(output_data[i])
    count = count + 1
    time.sleep(1)
    if(count >= 10) : update.cancel()
    update.run()

update = threading.Timer(1, thread1)
update.start()
update.join()