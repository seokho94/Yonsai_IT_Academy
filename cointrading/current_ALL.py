import threading
import pyupbit as upbit
import request_test
count = 0
close_price = []
krw_price = []

def current_all() :
    coins = upbit.get_tickers()
    global krw_price
    current_price = []

    for coin in coins :
        if 'KRW-'  in coin :
            krw_price.append(coin)

    all_coin = upbit.get_current_price(krw_price)
    
    for coin in all_coin :
        print(coin+" : " + "{}" .format(all_coin.get(coin)))

def close_data() :
    global close_price
    global krw_price

    for coin in krw_price :
        data = request_test.request_data(function='ohlcv', ticker=coin, interval='day', count=1)
        close = data['close']
        close_price.append([coin, close])
        
    print(close_price)
    
def thread_1() :
    global count
    current_all()
    count = count + 1
    print("*********************** {} ************************".format(count))
    # thread1.run()
    
close_data()
thread1 = threading.Timer(1, thread_1)
# thread1.start()