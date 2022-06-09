import threading
import pyupbit as upbit
import request_test
import time
from datetime import datetime
# import cur_ui as cui

#업비트 원화 마켓에 있는 코인의 개수 : 114

count = 0   ##쓰레드 실행 횟수
close_price = {'coin' : 0}  ##전날 종가에 대한 딕셔너리
krw_price = [] ##원화마켓 코인에 대한 리스트
Kor_name = {'Symbol' : 'kor'}
cur_data = []

#원화 마켓에 있는 전체 코인의 데이터를 가공하는 과정
def current_all() :
    global krw_price
    global close_price
    global Kor_name
    global cur_data
    current_price = [] ##코인의 이름, 등락률, 현재가에 대한 리스트

    all_coin = upbit.get_current_price(krw_price) ##원화로 분리된 코인들의 현재가에 대한 데이터를 요청하는 함수
    
    for coin in all_coin : ##화면에 출력할 데이터를 가공하는 과정 / [코인이름 / 전날대비% / 현재가]
        yester = close_price.get(coin)
        current = all_coin.get(coin)
        rate = round((current - yester) / yester * 100, 2)
        name = Kor_name.get(coin) + '/' + coin[4:]
        # 계산 값을 확인하는 과정
        ##print("coin : " + coin + " yester : {} current : {} rate : {}".format(yester, current, rate))
        current_price.append([name, str(rate)+'%', current])
      
    # data 확인 과정  
    # for i in range(len(current_price)) :
    #     print(current_price[i])
    
    #data 초기화 및 입력
    cur_data = current_price
    print(cur_data)
    #데이터 복사 확인 과정
    # print(len(cur_data))
    # for i in range(len(cur_data)) :
    #     print(cur_data[i])
    

def ticker_data() :
    global krw_price
    coins = upbit.get_tickers() ##코인 이름에 대한 정보를 요청하는 함수
    for coin in coins : ##모든 코인들에 대한 정보에서 원화 마켓 코인을 분류하는 작업
        if 'KRW-'  in coin :
            krw_price.append(coin)

#전날 종가에 대한 데이터를 받아와 가공하는 작업 -> 프로그램 실행시 1회만 실행 -> 09시 기준 업데이트
def close_data() :
    global close_price
    global krw_price
    request_count = 0
    start_time = time.time() #실행 시간 확인용
    
    for coin in krw_price :
        data = request_test.request_data(function='ohlcv', ticker=coin, interval='day', count=1)
        close = data['close'][0]
        close_price[coin] = close
        #***********단위 시간당 과도한 데이터 요청으로 인한 에러 예외 처리 부분***************
        # try : 
        #     close = data['close'][0]
        #     close_price.append([coin, close])
        # except TypeError :
        #     data = request_test.request_data(function='ohlcv', ticker=coin, interval='day', count=1)
        #     close = data['close'][0]
        #     close_price.append([coin, close])
        request_count = request_count + 1
        if(request_count>=5) :
            request_count=0
            time.sleep(0.27)
    
    print("실행 시간 : {}" .format(time.time()-start_time)) #실행 시간 확인용

#원화마켓에 거래되는 모든 가상화폐의 Symbol과 한국어 명칭에 대한 정보 추출
def coin_info() :
    global Kor_name
    coinData = upbit.get_tickers(fiat="KRW", verbose=True)
    for i in range (len(coinData)) :
        Kor_name[coinData[i].get('market')] = coinData[i].get('korean_name')
    
#현재가를 갱신하기 위한 스레드
#업비트 기준 am 09:00:00으로 장이 시작되므로 전날 종가를 09시 기준으로 업데이트
def thread_1() :
    now = datetime.now()
    global count
    current_all()
    # count = count + 1
    # print("*********************** {} ************************".format(count))
    cur_thread = threading.Timer(1, thread_1)
    if(now.hour==9) and (now.minute==0) and (now.second==0) :
        cur_thread.cancel()
        time.sleep(1)
        update_close()
        print("------------종가 갱신 완료------------")
        thread_1()
    else :
        cur_thread.start()

#종가에 dic을 초기화 함과 동시에 업데이트
def update_close() :
    global close_price
    close_price = {'coin' : 0}
    close_data()

# def start() :
#     ticker_data()
#     coin_info()
#     close_data()
#     current_all()


ticker_data()
coin_info()
close_data()
thread_1()
# current_all()