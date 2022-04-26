#사실 이정도의 library는 필요없습니다. 제가 시작할때 라이브러리 모두 다 받아놓는 습관이있어서 ㅠ
library(readxl)
library(dplyr)
library(XML)
library(jsonlite)
library(ggplot2)
library(psych)
library(reshape2)
library(stringr)

#Report_rate.xls를 불러와서 computer에 저장한 후 행이름을 All_Type,Type,DayUsedTime으로 바꿈
computer <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/teamproject/Report_rate.xls")
colnames(computer) <- c("All_Type","Type","DayUsedTime")

#computer에서 상황별 값을 뽑아오기 위해 filter함수를 사용함
sexvalue <- filter(computer, All_Type == "성별")
agevalue <- filter(computer, All_Type == "연령별")
cooperationvalue <- filter(computer,All_Type == "학력별")
incomevalue <- filter(computer,All_Type == "소득별")
marriagevalue <- filter(computer,All_Type == "혼인상태별")
areavalue <- filter(computer,All_Type == "지역대분류")

#Data 목록 만들기
#sex <- c("남성","여성")
#age <- c("10대","20대","30대","40대","50대","60대 이상")
#cooperation <- c("중졸 이하","고졸 이하","대졸 이하","대학원 이상")
#income <- c("100 만원 미만","100~200만 미만","200~300만 미만","300~400만 미만","400~500만 미만","500만 이상")
#marriage <- c("기혼","미혼","이혼/별거","사별")
#area <- c("도심권","동북권","서북권","서남권","동남권")

#Data목록 이름 만들어 주기 (fill에 대입될 이름)
colnames(sexvalue) <- c("All_Type","성별","DayUsedTime")
colnames(agevalue) <- c("All_Type","연령별","DayUsedTime")
colnames(cooperationvalue) <- c("All_Type","학력별","DayUsedTime")
colnames(incomevalue) <- c("All_Type","소득별","DayUsedTime")
colnames(marriagevalue) <- c("All_Type","혼인상태별","DayUsedTime")
colnames(areavalue) <- c("All_Type","지역대분류","DayUsedTime")

##+ labs(title = "서울시 1일 평균 인터넷 사용시간(성별)")
#그래프 표시 ggplot을 이용해서 그래프 표시, geom_bar를 사용해서 그래프형식으로 만들었다가 coord_polar를 이용해서 pie형식으로 변환,
#geom_text를 이용해서 value의 시간 표시하고 theme_void()를 사용해서 깔끔하게 보이게 함, labs를 이용해 제목표시 했으며 theme을 이용해 제목을 가운데 정렬 했음
ggplot(sexvalue,aes(x = "", y = DayUsedTime, fill = 성별)) + geom_bar(width = 1, stat = "identity") +
    coord_polar("y") + geom_text(aes(label = paste0(round(DayUsedTime,10),"시간")),position = position_stack(vjust = 0.5)) + theme_void() + labs(title = "서울시 1일 평균 인터넷 사용시간(성별)") + theme(plot.title = element_text(hjust = 0.6, family='notosanskr'))

ggplot(agevalue,aes(x = "", y = DayUsedTime, fill = 연령별)) + geom_bar(width = 1, stat = "identity") + coord_polar("y") +
    geom_text(aes(label = paste0(round(DayUsedTime,10),"시간")),position = position_stack(vjust = 0.5)) + theme_void() + labs(title = "서울시 1일 평균 인터넷 사용시간(연령별)") + theme(plot.title = element_text(hjust = 0.6, family='notosanskr'))

ggplot(cooperationvalue,aes(x = "", y = DayUsedTime, fill = 학력별)) + geom_bar(width = 1, stat = "identity") + coord_polar("y") +
    geom_text(aes(label = paste0(round(DayUsedTime,10),"시간")),position = position_stack(vjust = 0.5)) + theme_void() + labs(title = "서울시 1일 평균 인터넷 사용시간(학력별)") + theme(plot.title = element_text(hjust = 0.6, family='notosanskr'))

ggplot(incomevalue,aes(x = "", y = DayUsedTime, fill = 소득별)) + geom_bar(width = 1, stat = "identity") + coord_polar("y") +
    geom_text(aes(label = paste0(round(DayUsedTime,10),"시간")), position = position_stack(vjust = 0.5)) + theme_void() + labs(title = "서울시 1일 평균 인터넷 사용시간(소득별)") + theme(plot.title = element_text(hjust = 0.6, family='notosanskr'))

ggplot(marriagevalue,aes(x = "",y = DayUsedTime, fill = 혼인상태별)) + geom_bar(width = 1, stat = "identity") + coord_polar("y") +
    geom_text(aes(label = paste0(round(DayUsedTime,10),"시간")), position = position_stack(vjust = 0.5)) + theme_void() + labs(title = "서울시 1일 평균 인터넷 사용시간(혼인상태별)") + theme(plot.title = element_text(hjust = 0.6, family='notosanskr'))

ggplot(areavalue,aes(x = "", y = DayUsedTime, fill = 지역대분류)) + geom_bar(width = 1, stat = "identity") + coord_polar("y") +
    geom_text(aes(label = paste0(round(DayUsedTime,10),"시간")), position = position_stack(vjust = 0.5)) + theme_void() + labs(title = "서울시 1일 평균 인터넷 사용시간(지역대분류)") + theme(plot.title = element_text(hjust = 0.6, family='notosanskr'))

