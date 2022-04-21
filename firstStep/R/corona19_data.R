library(readxl)
xlsdata <- read_excel("~/GitHub/Yonsai_IT_Academy/firstStep/R/data_ex/20211125194459.xls")
View(xlsdata)

data_raw <- xlsdata[, c(2:5)]
head(data_raw)

names(data_raw)
names(data_raw) <- c("state", "city", "name", "addr")
names(data_raw)

table(data_raw$state)
barplot(table(data_raw$state))

library(dplyr)
data_raw %>% count(city)

daejeon_data <- data_raw[data_raw$state == "대전",]
head(daejeon_data)
nrow(daejeon_data)

library(ggmap)
ggmap_key <- ggmapkey
register_google(ggmap_key)
daejeon_data <- mutate_geocode(data = daejeon_data, location = addr, source = 'google')
head(daejeon_data)
head(daejeon_data$lon)

daejeon_map <- get_googlemap('대전', maptype = 'roadmap', zoom = 11)
ggmap(daejeon_map) + geom_point(data = daejeon_data, aes(x = lon, y = lat, color = factor(name)), size = 3)

daejeon_data_marker <- data.frame(daejeon_data$lon, daejeon_data$lat)
daejeon_map <- get_googlemap('대전', maptype = 'roadmap', zoom = 11, markers = daejeon_data_marker)
ggmap(daejeon_map) + geom_text(data = daejeon_data, aes(x = lon, y = lat, ), size = 3, label = daejeon_data$name)

