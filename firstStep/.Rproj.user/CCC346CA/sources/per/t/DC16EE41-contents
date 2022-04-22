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

P_merge <- merge(seoul_map, p, by = 'id')

ggplot() + geom_polygon(data = P_merge, aes(x=long, y=lat, group=group), fill = 'white', color = 'black')
