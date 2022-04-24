library(ggmap)
library(ggplot2)
library(raster)
library(rgeos)
library(maptools)
library(rgdal)

p <- read.csv("~/GitHub/Yonsai_IT_Academy/firstStep/R/sample.csv", header = TRUE)
map <- shapefile("~/GitHub/Yonsai_IT_Academy/firstStep/R/SIG_201703/TL_SCCO_SIG.shp")

map@proj4string

##map <- spTransform(map, CRSobj = CRS('+proj=tmerc +lat_0=38 +lon_0=127.5 +k=0.9996 +x_0=1000000 +y_0=2000000 +ellps=GRS80
##+units=m +no_defs'))

map <- spTransform(map, CRSobj = CRS('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'))

new_map <- fortify(map, region = "SIG_CD")
View(new_map)

new_map$id <- as.numeric(new_map$id)
seoul_map <- new_map[new_map$id <= 11740,]
View(seoul_map)

P_merge <- merge(seoul_map, p, by = 'id')
View(P_merge)

ggplot() + geom_polygon(data = P_merge, aes(x=long, y=lat, group=group), fill = 'white', color = 'black')

##----------------------------data 가공-------------------------
library(readxl)
data <- read_xls("~/GitHub/Yonsai_IT_Academy/firstStep/R/Report.xls")
View(data)
internet_data <- data

library(dplyr)

internet_data <- internet_data[grep("구", internet_data$대분류),]
View(internet_data)

internet_data <- internet_data[,c(1:3)]
View(internet_data)

internet_data <- internet_data[,-c(2)]
View(internet_data)

internet_data <- rename(internet_data,"하루평균사용시간" = "1일평균사용시간(시간)")

internet_data[,'id'] <- c(11110,11140, 11170, 11200, 11215, 11230, 11260, 11290, 11305, 11320, 11350, 11380, 11410, 11440, 11470, 11500, 11530, 11545, 11560, 11590, 11620, 11650, 11680, 11710, 11740)
View(internet_data)

merge_result <- merge(seoul_map, internet_data, by="id")
View(merge_result)

map_g <- ggplot() + geom_polygon(data=merge_result, aes(x=long, y=lat, group=group, fill=하루평균사용시간, color=대분류)) + labs(x='위도', y='경도', fill='하루평균사용시간', color='서울특별시 자치구') + geom_col(size=10)
map_g
map_g <- map_g+scale_fill_gradient(low='yellow', high='red')
map_g

register_google(key = '구글API키')
base_map = get_map("seoul", zoom=11, maptype = "hybrid")
ggmap(base_map)

test_map <- ggmap(base_map) + geom_polygon(data=merge_result, aes(x=long, y=lat, group=group, fill=하루평균사용시간, color=대분류),alpha = 0.7) + labs(x='위도', y='경도', fill='하루평균사용시간', color='서울특별시 자치구')+ scale_fill_gradient(low='yellow', high='red')

test_map

