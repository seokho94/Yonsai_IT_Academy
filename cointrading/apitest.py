import pyupbit

access_key = ""
secret_key = ""

myData = pyupbit.Upbit(access_key, secret_key)
print("보유 원화 총액 : {}"  .format(myData.get_balance(ticker="KRW")))
print("총 매수 금액 : {}" .format(myData.get_amount('ALL')))
print("BTC 보유 수량 : {}" .format(myData.get_balance(ticker="KRW-BTC")))
print(myData.get_chance("KRW-BTC"))
print(myData.get_order("KRW-BTC"))