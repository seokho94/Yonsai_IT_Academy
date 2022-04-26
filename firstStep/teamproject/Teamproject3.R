#사실 이정도의 library는 필요없습니다. 제가 시작할때 라이브러리 모두 다 받아놓는 습관이있어서 ㅠ
install.packages("readxl")
install.packages("dplyr")
install.packages("XML")
install.packages("jsonlite")
install.packages("ggplot2")
install.packages("psych")
install.packages("reshape2")
install.packages("stringr")
install.packages("gridExtra")
install.packages("scales")


library(readxl)
library(dplyr)
library(XML)
library(jsonlite)
library(ggplot2)
library(psych)
library(reshape2)
library(stringr)
library(gridExtra)
library(scales)

computer <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/teamproject/Report_spread_map.xls")
computer
colnames(computer) <- c("All_Type","Type","t1%","t2%","t3%","t4%")
colnames(computer)

sexvalue <- filter(computer, All_Type == "성별")
agevalue <- filter(computer, All_Type == "연령별")
cooperationvalue <- filter(computer,All_Type == "학력별")
incomevalue <- filter(computer,All_Type == "소득별")
marriagevalue <- filter(computer,All_Type == "혼인상태별")
areavalue <- filter(computer,All_Type == "지역대분류")


sex <- c("남성","여성")
age <- c("10대","20대","30대","40대","50대","60대 이상")
cooperation <- c("중졸 이하","고졸 이하","대졸 이하","대학원 이상")
income <- c("100 만원 미만","100~200만 미만","200~300만 미만","300~400만 미만","400~500만 미만","500만 이상")
marriage <- c("기혼","미혼","이혼/별거","사별")
area <- c("도심권","동북권","서북권","서남권","동남권")


colnames(sexvalue) <- c("All_Type","Type","1시간 이하","1-3시간","3-5시간","5시간 초과")
colnames(agevalue) <- c("All_Type","Type","1시간 이하","1-3시간","3-5시간","5시간 초과")
colnames(cooperationvalue) <- c("All_Type","Type","1시간 이하","1-3시간","3-5시간","5시간 초과")
colnames(incomevalue) <- c("All_Type","Type","1시간 이하","1-3시간","3-5시간","5시간 초과")
colnames(marriagevalue) <- c("All_Type","Type","1시간 이하","1-3시간","3-5시간","5시간 초과")
colnames(areavalue) <- c("All_Type","Type","1시간 이하","1-3시간","3-5시간","5시간 초과")

test0 <- melt(sexvalue,id.vars = c("All_Type","Type"))
test1 <- melt(agevalue,id.vars = c("All_Type","Type"))
test2 <- melt(cooperationvalue,id.vars = c("All_Type","Type"))
test3 <- melt(incomevalue,id.vars = c("All_Type","Type"))
test4 <- melt(marriagevalue,id.vars = c("All_Type","Type"))
test5 <- melt(areavalue,id.vars = c("All_Type","Type"))

test5

ggplot(test0,aes(x = Type , y =value)) +
  geom_point(aes(colour = factor(variable))) +
  labs(title = "서울시 1일 평균 인터넷 사용시간(성별분류)") +
  theme(plot.title = element_text(hjust = 0.6)) +
  geom_text(aes(label = variable, vjust = 0, hjust = 0))

ggplot(test1,aes(x = Type , y =value)) +
  geom_point(aes(colour = factor(variable))) +
  labs(title = "서울시 1일 평균 인터넷 사용시간(연령별분류)") +
  theme(plot.title = element_text(hjust = 0.6)) +
  geom_text(aes(label = variable, vjust = 0, hjust = 0))

ggplot(test2,aes(x = Type , y =value)) +
  geom_point(aes(colour = factor(variable))) +
  labs(title = "서울시 1일 평균 인터넷 사용시간(학력별분류)") +
  theme(plot.title = element_text(hjust = 0.6)) +
  geom_text(aes(label = variable, vjust = 0, hjust = 0))

ggplot(test3,aes(x = Type , y =value)) +
  geom_point(aes(colour = factor(variable))) +
  labs(title = "서울시 1일 평균 인터넷 사용시간(소득별분류)") +
  theme(plot.title = element_text(hjust = 0.6)) +
  geom_text(aes(label = variable, vjust = 0, hjust = 0))

ggplot(test4,aes(x = Type , y =value)) +
  geom_point(aes(colour = factor(variable))) +
  labs(title = "서울시 1일 평균 인터넷 사용시간(혼인상태별분류)") +
  theme(plot.title = element_text(hjust = 0.6)) +
  geom_text(aes(label = variable, vjust = 0, hjust = 0))

ggplot(test5,aes(x = Type , y =value)) +
  geom_point(aes(colour = factor(variable))) +
  labs(title = "서울시 1일 평균 인터넷 사용시간(지역별분류)" ) +
  theme(plot.title = element_text(hjust = 0.6)) +
  geom_text(aes(label = variable, vjust = 0, hjust = 0))
