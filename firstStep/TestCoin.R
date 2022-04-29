library(jsonlite)
library(dplyr)

coinTable <- fromJSON("https://api.bithumb.com/public/ticker/ALL")
View(coinTable)

#opening_price : 00:00 기준 가격
#closing_price : 23:59 기준 가격
#min_price : 하루 최소 가격
#max_price : 하루 최대 가격

coinData <- coinTable$data; coinTable
View(coinData)
write.csv(coinData, file = "coinTotalData.csv")

xrpData <- coinData$XRP
View(xrpData)

coinDataFrame <- unlist(grep('fluctate_rate_24H', coinData, value=T))
View(coinDataFrame)

write.csv(coinDataFrame, file = "coinData(1).csv")
