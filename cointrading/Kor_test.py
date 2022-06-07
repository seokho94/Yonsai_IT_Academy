import pyupbit as upbit

tickers = upbit.get_tickers(fiat="KRW",verbose=True)

for i in range(len(tickers)) :
    print("Symbol : "+tickers[i].get('market') + " KorName : " + tickers[i].get('korean_name'))