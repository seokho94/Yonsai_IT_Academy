import request_test as rq
import threading
import time

ask_price = [['ask_price' , 'ask_size']]
bid_price = [['bid_price' , 'bid_size']]
count = 0

def update_data(ticker) :
    global ask_price
    global bid_price
    data = rq.request_data('order', ticker)
    poll_data = data['orderbook_units']
    
    for i in range(0, 5) :
        ask_price.append([poll_data[i].get('ask_price') , poll_data[i].get('ask_size')])
        bid_price.append([poll_data[i].get('bid_price') , poll_data[i].get('bid_size')])
        
    for i in range(0, 6) :
        print("ask_price : ", ask_price[i][0])
        print("ask_size : ", ask_price[i][1])
        print("bid_price : ", bid_price[i][0])
        print("bid_size : ", bid_price[i][1])
    
    
def thread_order() :
    global count
    count=count + 1
    update_data("KRW-BTC")
    print("**********************  {}  ************************".format(count))
    time.sleep(1)
    order_update.run()    

order_update = threading.Timer(1, thread_order)
order_update.start()
order_update.join()