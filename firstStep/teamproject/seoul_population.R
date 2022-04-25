#library 불러옵니다
library(readxl)
library(dplyr)
library(ggplot2)
library(descr)
#전처리 과정 (pop으로 엑셀 불러오고 colnames를 3개만 지정해 준 후 파이프연산자를 이용해서 3개만 추출, 그다음 division값이 계인 열만 반환하기 위해 filter함수를 사용했습니다.)
pop <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/teamproject/Report_population.xls")
colnames(pop) <- c("City_name","Division","Sum")
seoul_pop <- pop %>% select("City_name","Division","Sum")
seoul_population <- filter(seoul_pop, Division == "계")
#option함수를 이용해 큰 숫자를 표현
options(scipen = 100)

#barplot을 이용해 인구추이 표현했습니다.
barplot(seoul_population$Sum, xlab = "행정구역", ylab = "인구수",names = seoul_population$City_name , ylim = c(0 , max(seoul_population$Sum)+100000), main = "서울시 인구추이", col='skyblue')
