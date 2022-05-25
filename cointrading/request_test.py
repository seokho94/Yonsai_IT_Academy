from datetime import datetime
import pyupbit
import threading
import time

def request_data(function, ticker, interval='minute1', to=datetime.today().strftime('%Y-%m-%d'), count = 1) :
    data = []
    if function == 'current' :
        price = current_price(ticker)
        return price
    elif function == 'order' :
        data = order_book(ticker)
        return data
    elif function == 'ohlcv' :
        data = ohlcv(ticker, interval, to, count)
        return data

def current_price(ticker) :
    price = pyupbit.get_current_price([ticker])
    return price

def order_book(ticker) :
    orderbook = pyupbit.get_orderbook(ticker)
    return orderbook

def ohlcv(ticker, interval, to, count) :
    data = pyupbit.get_ohlcv(ticker = ticker, interval = interval, count = count, to = to)
    return data


# def thread_1() :
#     print('Thread_1 Start')
#     request_data('current', 'KRW-BTC')
#     time.sleep(1)
#     thread1.run()
    
# def thread_2() :
#     print('Thread_2 Start')
#     request_data('order', 'KRW-BTC')
#     time.sleep(1)
#     thread2.run()
    
# def thread_3() :
#     print('Thread_3 Start')
#     request_data('ohlcv', 'KRW-BTC', 'minute1', count = 10)
#     time.sleep(1)
#     thread3.run()
    
    
# thread1 = threading.Timer(1, thread_1)
# thread2 = threading.Timer(1, thread_2)
# thread3 = threading.Timer(1, thread_3)

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()