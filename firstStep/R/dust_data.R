library(readxl)
dustdata <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/dustdata.xlsx")
View(dustdata)
str(dustdata)

library(dplyr)
dustdata_anal <- dustdata[, c("날짜", "성북구", "중구")]
View(dustdata_anal)

is.na(dustdata_anal)
sum(is.na(dustdata_anal))

library(psych)
describe(dustdata_anal$성북구)
describe(dustdata_anal$중구)

boxplot(dustdata_anal$성북구, dustdata_anal$중구, main = "finedust_compare", xlab = "AREA", names = c("성북구", "중구"), ylab = "FINEDUST_PM", col = c("blue", "green"))

var.test(dustdata_anal$중구, dustdata_anal$성북구)

t.test(dustdata_anal$중구, dustdata_anal$성북구, var.equal = T)

exdata1 <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/Sample1.xlsx")
exdata1

boxplot(formula = Y20_CNT ~ AREA, data = exdata1)

anova(lm(Y20_CNT ~ AREA, data = exdata1))

oneway.test(data = exdata1, Y20_CNT ~ AREA, var.equal = T)

