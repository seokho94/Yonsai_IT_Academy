import pyupbit as upbit
import math

##bid -> 매도 / ask -> 매수

data = upbit.get_orderbook("KRW-BTC")

print(data)

poll_data = data['orderbook_units']

print(poll_data)

ask_price = [['ask_price' , 'ask_size']]
bid_price = [['bid_price' , 'bid_size']]
# ask_total = []
# bid_total = []

for i in range(0, 5) :
    ask_price.append([poll_data[i].get('ask_price') , poll_data[i].get('ask_size')])
    bid_price.append([poll_data[i].get('bid_price') , poll_data[i].get('bid_size')])
    # ask_total.append(math.trunc(poll_data[i].get('ask_price')*poll_data[i].get('ask_size')))
    # bid_total.append(math.trunc(poll_data[i].get('bid_price')*poll_data[i].get('bid_size')))
    
print(ask_price)
print(bid_price)
# print(ask_total)
# print(bid_total)

for i in range(0, 6) :
    print("ask_price : ", ask_price[i][0])
    print("ask_size : ", ask_price[i][1])
    print("bid_price : ", bid_price[i][0])
    print("bid_size : ", bid_price[i][1])