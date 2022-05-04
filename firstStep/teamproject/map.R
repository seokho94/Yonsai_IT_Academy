library(ggmap)
library(ggplot2)
library(raster)
library(rgeos)
library(maptools)
library(rgdal)
library(ggmap)
register_google(key = 'API키')
##-------------------test-------------------------------------------

##p <- read.csv("~/GitHub/Yonsai_IT_Academy/firstStep/R/sample.csv", header = TRUE)
##map <- shapefile("~/GitHub/Yonsai_IT_Academy/firstStep/R/SIG_201703/TL_SCCO_SIG.shp")

##map <- spTransform(map, CRSobj = CRS('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'))

##new_map <- fortify(map, region = "SIG_CD")
##View(new_map)

##new_map$id <- as.numeric(new_map$id)
##seoul_map <- new_map[new_map$id <= 11740,]
##View(seoul_map)

##P_merge <- merge(seoul_map, p, by = 'id')
##View(P_merge)

##ggplot() + geom_polygon(data = P_merge, aes(x=long, y=lat, group=group), fill = 'white', color = 'black')

##----------------------------data test-------------------------
map <- shapefile("~/GitHub/Yonsai_IT_Academy/firstStep/teamproject/SIG_201703/TL_SCCO_SIG.shp")

map <- spTransform(map, CRSobj = CRS('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'))

new_map <- fortify(map, region = "SIG_CD")
View(new_map)

new_map$id <- as.numeric(new_map$id)
seoul_map <- new_map[new_map$id <= 11740,]
View(seoul_map)

library(readxl)
data <- read_xls("~/GitHub/Yonsai_IT_Academy/firstStep/teamproject/Report.xls")
View(data)
internet_data <- data

library(dplyr)

##Report.xls에사 대분류에서 구로 끝나는 데이터 행 추출
internet_data <- internet_data[grep("구", internet_data$대분류),]
View(internet_data)

##구로 끝나는 데이터 행에서 1~3까지 데이터 열만 추출
internet_data <- internet_data[,c(1:3)]
View(internet_data)

##분류(2열) 열 삭제
internet_data <- internet_data[,-c(2)]
View(internet_data)

##인터넷 데이터의 "1일평균사용시간(시간) 열 이름을 "하루평균사용시간"으로 변경
##변경 이유 : string + int가 합쳐져 1이 int로 인식
internet_data <- rename(internet_data,"하루평균사용시간" = "1일평균사용시간(시간)")

##맵데이터와 internet_data를 연결하기 위해 id 값을 추가
internet_data[,'id'] <- c(11110,11140, 11170, 11200, 11215, 11230, 11260, 11290, 11305, 11320, 11350, 11380, 11410, 11440, 11470, 11500, 11530, 11545, 11560, 11590, 11620, 11650, 11680, 11710, 11740)
View(internet_data)

##seoul_map과 internet_data 값을 id로 병합 연결
merge_result <- merge(seoul_map, internet_data, by="id")
View(merge_result)

map_g <- ggplot() + geom_polygon(data=merge_result, aes(x=long, y=lat, group=group, fill=하루평균사용시간), color = 'white') + labs(x='위도', y='경도', fill='인터넷 하루평균사용시간') + scale_fill_gradient(low='#4374D9', high='#000042')

map_g
##yellow => red
##g <- map_g+scale_fill_gradient(low='yellow', high='red')
##map_g

##지도에 text 삽입을 위한 데이터 가공
map_text <- internet_data
View(map_text)
map_text[,'lat'] <- c(mean(merge_result[grep("종로구", merge_result$대분류),]$lat), mean(merge_result[grep("중구", merge_result$대분류),]$lat), mean(merge_result[grep("용산구", merge_result$대분류),]$lat)-0.002, mean(merge_result[grep("성동구", merge_result$대분류),]$lat), mean(merge_result[grep("광진구", merge_result$대분류),]$lat), mean(merge_result[grep("동대문구", merge_result$대분류),]$lat), mean(merge_result[grep("중랑구", merge_result$대분류),]$lat), mean(merge_result[grep("성북구", merge_result$대분류),]$lat), mean(merge_result[grep("강북구", merge_result$대분류),]$lat), mean(merge_result[grep("도봉구", merge_result$대분류),]$lat), mean(merge_result[grep("노원구", merge_result$대분류),]$lat), mean(merge_result[grep("은평구", merge_result$대분류),]$lat), mean(merge_result[grep("서대문구", merge_result$대분류),]$lat), mean(merge_result[grep("마포구", merge_result$대분류),]$lat)-0.005, mean(merge_result[grep("양천구", merge_result$대분류),]$lat)-0.01, mean(merge_result[grep("강서구", merge_result$대분류),]$lat), mean(merge_result[grep("구로구", merge_result$대분류),]$lat)+0.005, mean(merge_result[grep("금천구", merge_result$대분류),]$lat)+0.002, mean(merge_result[grep("영등포구", merge_result$대분류),]$lat), mean(merge_result[grep("동작구", merge_result$대분류),]$lat)+0.01, mean(merge_result[grep("관악구", merge_result$대분류),]$lat), mean(merge_result[grep("서초구", merge_result$대분류),]$lat), mean(merge_result[grep("강남구", merge_result$대분류),]$lat), mean(merge_result[grep("송파구", merge_result$대분류),]$lat), mean(merge_result[grep("강동구", merge_result$대분류),]$lat))

map_text[,'long'] <- c(mean(merge_result[grep("종로구", merge_result$대분류),]$long), mean(merge_result[grep("중구", merge_result$대분류),]$long), mean(merge_result[grep("용산구", merge_result$대분류),]$long), mean(merge_result[grep("성동구", merge_result$대분류),]$long)+0.015, mean(merge_result[grep("광진구", merge_result$대분류),]$long), mean(merge_result[grep("동대문구", merge_result$대분류),]$long), mean(merge_result[grep("중랑구", merge_result$대분류),]$long), mean(merge_result[grep("성북구", merge_result$대분류),]$long), mean(merge_result[grep("강북구", merge_result$대분류),]$long), mean(merge_result[grep("도봉구", merge_result$대분류),]$long), mean(merge_result[grep("노원구", merge_result$대분류),]$long)+0.01, mean(merge_result[grep("은평구", merge_result$대분류),]$long), mean(merge_result[grep("서대문구", merge_result$대분류),]$long)-0.005, mean(merge_result[grep("마포구", merge_result$대분류),]$long), mean(merge_result[grep("양천구", merge_result$대분류),]$long)-0.002, mean(merge_result[grep("강서구", merge_result$대분류),]$long), mean(merge_result[grep("구로구", merge_result$대분류),]$long), mean(merge_result[grep("금천구", merge_result$대분류),]$long)+0.002, mean(merge_result[grep("영등포구", merge_result$대분류),]$long)+0.005, mean(merge_result[grep("동작구", merge_result$대분류),]$long), mean(merge_result[grep("관악구", merge_result$대분류),]$long), mean(merge_result[grep("서초구", merge_result$대분류),]$long), mean(merge_result[grep("강남구", merge_result$대분류),]$long), mean(merge_result[grep("송파구", merge_result$대분류),]$long), mean(merge_result[grep("강동구", merge_result$대분류),]$long))

View(map_text)
##map_g에 표현하기
map_all <- map_g + geom_text(map_text, mapping = aes(x=long, y=lat, label = paste(대분류)), size=2.3, color = 'white')

map_all

base_map = get_map("seoul", zoom=11, maptype = "hybrid")
ggmap(base_map)

test_map <- ggmap(base_map)+geom_polygon(data=merge_result, aes(x=long, y=lat, group=group, fill=하루평균사용시간),alpha = 0.5, color = 'white') + labs(x='위도', y='경도', fill='하루평균사용시간', color='서울특별시 자치구')+ scale_fill_gradient(low='#4374D9', high='#000042')

test_map
