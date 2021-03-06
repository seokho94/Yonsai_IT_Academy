# Hello, world!
#
# This is an example function named 'hello'
# which prints 'Hello, world!'.
#
# You can learn more about package authoring with RStudio at:
#
#   http://r-pkgs.had.co.nz/
#
# Some useful keyboard shortcuts for package authoring:
#
#   Install Package:           'Ctrl + Shift + B'
#   Check Package:             'Ctrl + Shift + E'
#   Test Package:              'Ctrl + Shift + T'

hello <- function() {
  print("Hello, world!")
}

hello()

ex_vector1 <- c(-1,0,1)
ex_vector1
mode(ex_vector1)
str(ex_vector1)
length(ex_vector1)

ex_vector2 <- c("Hello", "Hi~!")
ex_vector2

ex_vector3 <- c("1", "2", "3")
ex_vector3

mode(ex_vector2)
str(ex_vector2)
mode(ex_vector3)
str(ex_vector3)

ex_vector4 <- c(TRUE, FALSE, TRUE, FALSE)
ex_vector4
mode(ex_vector4)
str(ex_vector4)

ex_vector5 <- c(2, 1, 3, 2, 1)
ex_vector5
cate_vector5 <- factor(ex_vector5, labels = c("Apple", "Banana", "Cherry"))
cate_vector5

x <- c(1, 2, 3, 4, 5, 6)
matrix(x, nrow = 2, ncol = 3)
matrix(x, nrow = 3, ncol = 2)

y <- c(1, 2, 3, 4, 5, 6)
array(y, dim = c(2, 2, 3))

list1 <- list(c(1,2,3), "Hello")
list1

str(list1)

a <- 10

if (a %% 2 == 0){
  print("짝수입니다.")
}else{
  print("홀수입니다.")
}

b <- 80

if (b >= 90){
  print("A학점입니다.")
}else if(b >=80){
  print("B 학점입니다.")
}else{
  print("C 학점입니다.")
}

for(i in 1:9){
  a <- 2*i
  print(a)
}

for(i in 2:9){
  for(j in 1:9){
    print(paste(i, " * ", j , " = ", i*j))
  }
}

x <- matrix(1:4, 2, 2)
x

apply(x, 1, sum)

iris

apply(iris[, 1:4], 2, sum)


View(iris)

apply(iris[, 1:4], 2, sum)
apply(iris[, 1:4], 2, mean)
apply(iris[, 1:4], 2, min)
apply(iris[, 1:4], 2, max)

lapply(iris[, 1:4], sum)
sapply(iris[, 1:4], mean)

library(dplyr)
summarize(iris)

ID <- c(1, 2, 3, 4, 5)
ID
SEX <- c("F", "M", "F", "M", "F")
SEX
DATA <- data.frame(ID = ID, SEX = SEX)
View(DATA)

ex_data <- read.table("C:/Users/YONSAI/Documents/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex.txt", encoding = "EUC-KR", fileEncoding = "UTF-8")
View(ex_data)

ex_data1 <- read.table("C:/Users/YONSAI/Documents/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex.txt", encoding = "EUC-KR", fileEncoding = "UTF-8", header = TRUE)
View(ex_data1)

varname <- c("ID", "SEX", "AGE", "AREA")
ex1_data <- read.table("C:/Users/YONSAI/Documents/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex_col.txt", encoding = "EUC-KR", fileEncoding = "UTF-8", col.names = varname)
View(ex1_data)

ex_data2 <- read.table("C:/Users/YONSAI/Documents/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex.txt", encoding = "EUC-KR", fileEncoding = "UTF-8", header = TRUE, skip=2)
View(ex_data2)

ex_data3 <- read.table("C:/Users/YONSAI/Documents/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex.txt", encoding = "EUC-KR", fileEncoding = "UTF-8", header = TRUE, nrows = 7)
View(ex_data3)

ex_data4 <- read.table("C:/Users/YONSAI/Documents/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex1.txt", encoding = "EUC-KR", fileEncoding = "UTF-8", header = TRUE, sep = ",")
View(ex_data4)

library(readxl)

excel_data_ex <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex.xlsx")
View(excel_data_ex)

library(XML)
xml_data <- xmlToDataFrame("C:/Users/YONSAI/Documents/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex.xml")
View(xml_data)

library(jsonlite)
json_data <- fromJSON("C:/Users/YONSAI/Documents/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/data_ex.json")
str(json_data)

data("iris")

str(iris)

ncol(iris)
nrow(iris)
dim(iris)

ls(iris)

head(iris)

tail(iris, n=3)

mean(iris$Sepal.Length)
median(iris$Sepal.Length)

min(iris$Sepal.Length)
max(iris$Sepal.Length)
range(iris$Sepal.Length)

quantile(iris$Sepal.Length)
quantile(iris$Sepal.Length, probs = 0.25)
quantile(iris$Sepal.Length, probs = 0.5)
quantile(iris$Sepal.Length, probs = 0.75)
quantile(iris$Sepal.Length, probs = 0.80)

var(iris$Sepal.Length)
sd(iris$Sepal.Length)

library(psych)
kurtosi(iris$Sepal.Length)
skew(iris$Sepal.Length)

library(descr)
freq_test <- freq(iris$Sepal.Length, plot = F)
freq_test

library(readxl)
exdata1 <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/Sample1.xlsx")
freq(exdat1$SEX, plot = T, main = '성별(barplot)')
dist_sex <- table(exdata1$SEX)
dist_sex

barplot(dist_sex)
barplot(dist_sex, ylim = c(0, 14), main = "BARPLOT", xlab = "SEX", ylab = "FREQUENCY", names = c("Female", "Male"))

barplot(dist_sex, ylim = c(0, 14), main = "BARPLOT", xlab = "SEX", ylab = "FREQUENCY", names = c("Female", "Male"), col = c("pink", "navy"))

boxplot(exdata1$Y21_CNT, exdata1$Y20_CNT)

boxplot(exdata1$Y21_CNT, exdata1$Y20_CNT, ylim = c(0, 60), main="boxplot", names = c("21년건수","20년건수"), col =  c("green", "yellow"))

hist(exdata1$AGE, xlim = c(0,60), ylim = c(0,7), main = "AGE분포")
iris
mtcar
mtcars

data(mtcars)
x <- table(mtcars$gear)
x
pie(x)

x = c(1, 2, 3, 4, 7, 8, 8, 5, 9, 6, 9)
x
stem(x)

library(psych)
data(iris)
pairs.panels(iris)

library(descr)

library(dplyr)

library(psych)

library(readxl)

library(reshape2)

library(XML)

library(jsonlite)

library(plyr)

exdata1 <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/Sample1.xlsx")
freq(exdata1$SEX, plot = T, main = '성별(barplot)')
dist_sex <- table(exdata1$SEX)
dist_sex

barplot(dist_sex)
barplot(dist_sex, ylim = c(0, 14), main = "BARPLOT", xlab = "SEX", ylab = "FREQUENCY", names = c("Female", "Male"))

barplot(dist_sex, ylim = c(0, 14), main = "BARPLOT", xlab = "SEX", ylab = "FREQUENCY", names = c("Female", "Male"), col = c("pink", "navy"))

boxplot(exdata1$Y21_CNT, exdata1$Y20_CNT)

boxplot(exdata1$Y21_CNT, exdata1$Y20_CNT, ylim = c(0, 60), main="boxplot", names = c("21년건수","20년건수"), col =  c("green", "yellow"))

hist(exdata1$AGE, xlim = c(0,60), ylim = c(0,7), main = "AGE분포")
iris
mtcar

exdata1 %>% select(ID)
exdata1 %>% select(ID, AREA, Y21_CNT)
exdata1 %>% select(-AREA)
exdata1 %>% select(-AREA, -Y21_CNT)
exdata1 %>% filter(AREA == '서울')
exdata1 %>% filter(AREA == '서울' & Y21_CNT >= 10)
exdata1 %>% arrange(AGE)
exdata1 %>% arrange(desc(Y21_AMT))
exdata1 %>% arrange(AGE, desc(Y21_AMT))
exdata1 %>% summarise(TOT_Y21_AMT = sum(Y21_AMT))
exdata1 %>% group_by(AREA) %>% summarise(SUM_Y21_AMT = sum(Y21_AMT))

m_history <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/Sample2_m_history.xlsx")
f_history <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/Sample3_f_history.xlsx")
View(m_history)
View(f_history)

exdata_bindjoin <- bind_rows(m_history, f_history)
View(exdata_bindjoin)

jeju_y21_history <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/Sample4_y21_history.xlsx")
jeju_y20_history <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/Sample5_y20_history.xlsx")
View(jeju_y21_history)
View(jeju_y20_history)
bind_col <- left_join(jeju_y21_history, jeju_y20_history, by="ID")
View(bind_col)

bind_col_inner <- inner_join(jeju_y21_history, jeju_y20_history, by="ID")
View(bind_col_inner)

bind_col_full <- full_join(jeju_y21_history, jeju_y20_history, by="ID")
View(bind_col_full)

head(airquality)
names(airquality) <- tolower(names(airquality))
head(airquality)

melt_test <- melt(airquality)
head(melt_test)

tail(melt_test)

melt_test2 <- melt(airquality, id.vars = c("month", "wind"), measure.vars = "ozone")
head(melt_test2)

names(airquality)
tolower(names(airquality))
head(airquality)

aq_melt <- melt(airquality, id.vars = c("month", "day"), na.rm = TRUE)
head(aq_melt)

aq_dcast <- dcast(aq_melt, month + day ~ variable)
head(aq_dcast)

View(airquality)
View(aq_melt)
View(aq_dcast)

acast(aq_melt, day ~ month ~ variable)

acast(aq_melt, month ~ variable, mean)

dcast(aq_melt, month ~ variable, sum)

x <- c(1, 2, NA, 4, 5)
x
sum(x)
is.na(x)
table(is.na(x))

x <- c(1, 2, NA, 4, 5)
x
sum(x)
is.na(x)
sum(x, na.rm = T)

data(airquality)
airquality
is.na
sum(is.na(airquality))
table(is.na(airquality))
colSums(is.na(airquality))

data(airquality)
na.omit(airquality)

data(airquality)
airquality
airquality[is.na(airquality)] <-0
colSums(is.na(airquality))

data(mtcars)
mtcars
boxplot(mtcars$wt)

boxplot(mtcars$wt)$stats

mtcars$wt <- ifelse(mtcars$wt > 5.25, NA, mtcars$wt)

str(airquality)
ggplot(airquality, aes(x=Day, y=Temp))
ggplot(airquality, aes(x=Day, y=Temp)) + geom_point()
ggplot(airquality, aes(x=Day, y=Temp)) + geom_point(size=3, color="red")

ggplot(airquality, aes(x=Day, y = Temp)) + geom_line()

ggplot(mtcars, aes(x=cyl)) + geom_bar(width = 0.5)

mtcars
ggplot(mtcars, aes(x = factor(cyl))) + geom_bar(aes(fill = factor(gear)))

ggplot(mtcars, aes(x = factor(cyl))) + geom_bar(aes(fill = factor(gear))) + coord_polar()

ggplot(mtcars, aes(x = factor(cyl))) + geom_bar(aes(fill = factor(gear))) + coord_polar(theta = "y")

ggplot(airquality, aes(x = Day, y = Temp, group = Day)) + geom_boxplot()

ggplot(airquality, aes(Temp)) + geom_histogram()

ggplot(airquality, aes(x = Day, y =Temp)) + geom_line() + geom_point()

ggplot(airquality, aes(x = Day, y = Temp)) + geom_line(color = "red") + geom_point(size = 3)

str(economics)
ggplot(economics, aes(x = date, y = psavert)) + geom_line() + geom_abline(intercept = 12.18671, slope = -0.0005444)

ggplot(economics, aes(x = date, y = psavert)) + geom_line() + geom_hline(yintercept = mean(economics$psavert))

x_inter <- filter(economics, psavert == min(economics$psavert))$date
ggplot(economics, aes(x = date, y = psavert)) + geom_line() + geom_vline(xintercept =  x_inter)

ggplot(airquality, aes(x = Day, y = Temp)) + geom_point() + geom_text(aes(label = Temp, vjust = 0, hjust = 0))

ggplot(mtcars, aes(x = wt, y = mpg)) + geom_point() + annotate("rect", xmin = 3, xmax = 4, ymin = 12, ymax = 21, alpha = 0.5, fill = "skyblue")

ggplot(mtcars, aes(x = wt, y = mpg)) + geom_point() + annotate("rect", xmin = 3, xmax = 4, ymin = 12, ymax = 21, alpha = 0.5, fill = "skyblue") + annotate("segment", x = 2.5, xend = 3.7, y = 10, yend = 17, color = "red", arrow = arrow())

ggplot(mtcars, aes(x = wt, y = mpg)) + geom_point() + annotate("rect", xmin = 3, xmax = 4, ymin = 12, ymax = 21, alpha = 0.5, fill = "skyblue") + annotate("segment", x = 2.5, xend = 3.7, y = 10, yend = 17, color = "red", arrow = arrow()) + annotate("text", x = 2.5, y = 10, label = "point")

ggplot(mtcars, aes(x = gear)) + geom_bar() + labs(x = "기어수", y = "자동차수",  title = "변속기 기어별 자동차수수")

cor.test(exdata1$Y20_CNT, exdata1$Y21_CNT)

reg_result <- lm(Y21_CNT ~ Y20_CNT, data = exdata1)
reg_result

install.packages("ggmap")
register_google(key = "keys")
gg_seoul <- get_googlemap("seoul", maptype = "roadmap")
ggmap(gg_seoul)

geo_code <- enc2utf8("대전역") %>% geocode()
geo_data <- as.numeric(geo_code)

get_googlemap(center = geo_data, maptype = "roadmap", zoom = 13) %>% ggmap() + geom_point(data = geo_code, aes(x = geo_code$lon, y = geo_code$lat))
