library(readxl)
entrance_xls <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/entrance.xls")
str(entrance_xls)
head(entrance_xls)
colnames(entrance_xls) <- c("country", "JAN", "FEB", "MAR", "APR", "JUN", "JUL", "AUG", "SEP",
                            "OCT", "NOV", "DEC")
entrance_xls$country <- gsub(" ", "", entrance_xls$country)
entrance_xls

entrance_xls |> nrow()
top5_country <- entrance_xls[order(entrance_xls$JAN),] |> head(n = 5)
top5_country

library(reshape2)
top5_melt <- melt(top5_country, id.vars = 'country', variable.name = 'mon')
head(top5_melt)

library(ggplot2)
ggplot(top5_melt, aes(x = mon, y = value, group = country)) + geom_line(aes(color = country))

ggplot(top5_melt, aes(x = mon, y = value, group = country)) + geom_line(aes(color = country)) + ggtitle("2020년 국적별 입국 수 변화 추이") + scale_y_continuous(breaks = seq(0, 500000, 50000))

ggplot(top5_melt, aes(x = mon, y = value, fill = country)) + geom_bar(stat = "identity", position = "dodge")

ggplot(top5_melt, aes(x = mon, y = value, fill = country)) + geom_bar(stat = "identity", position = "stack")

