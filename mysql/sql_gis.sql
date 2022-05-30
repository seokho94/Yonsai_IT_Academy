drop database if exists GisDB;
create database GisDB;

use GisDB;

create table StreamTbl (
	MapNumber char(10),
    StreamName char(20),
    Stream geometry);

insert into StreamTbl values('330000001', '한류천', st_geomFromText('LINESTRING (-10 30, -50 70, 50 70)'));
insert into StreamTbl values('330000001', '안양천', st_geomFromText('LINESTRING (-50 -70, 30 -10, 70 -10)'));
insert into StreamTbl values('330000001', '일산천', st_geomFromText('LINESTRING (-70 50, -30 -30, 30 -60)'));

create table BuildingTbl(
	MapNumber char(10),
    BuildingName char(20),
    Building geometry );
    
insert into BuildingTbl values('330000005', '하나은행', st_geomFromText('POLYGON ((-10 50, 10 30, -10 10, -30 30, -10 50))'));
insert into BuildingTbl values('330000005', '우리빌딩', st_geomFromText('POLYGON ((-50 -70, -40 -70, -40 -80, -50 -80, -50 -70))'));
insert into BuildingTbl values('330000005', '하나은행', st_geomFromText('POLYGON ((40 0, 60 0, 60 -20, 40 -20, 40 0))'));

select * from streamTbl;

select * from buildingtbl;

select * from streamTbl where st_length(stream) > 140;

select BuildingName, st_area(Building) from buildingTbl where st_area(building) < 500;

select * from streamtbl union all select * from buildingtbl;

select streamName, BuildingName, Building, Stream from BuildingTbl, StreamTbl where st_intersects(Building, Stream) = 1 and streamName = '안양천';

select st_buffer(stream,5) from streamtbl;

drop database if exists KingHotDB;
create database KingHotDB;

use KingHotDB;
create table restaurant(
	restID int auto_increment primary key,
    restName varchar(50),
    restAddr varchar(50),
    restPhone varchar(15),
    totSales bigint,
    restLocation geometry );
    
insert into restaurant values(null, '왕매워 짬뽕 1호점', '서울 강서구 방화동', '02-111-1111', 1000, ST_GeomFromText('POINT(-80 -30)')),
    (null, '왕매워 짬뽕 2호점', '서울 은평구 증산동', '02-222-2222', 2000, ST_GeomFromText('POINT(-50 70)')),
    (null, '왕매워 짬뽕 3호점', '서울 중랑구 면목동', '02-333-3333', 9000, ST_GeomFromText('POINT(70 50)')),
    (null, '왕매워 짬뽕 4호점', '서울 광진구 구의동', '02-444-4444', 250, ST_GeomFromText('POINT(80 -10)')),
    (null, '왕매워 짬뽕 5호점', '서울 서대문구구 북가좌동', '02-555-5555', 1200, ST_GeomFromText('POINT(-10 50)')),
    (null, '왕매워 짬뽕 6호점', '서울 강남구 논현동', '02-666-6666', 4000, ST_GeomFromText('POINT(40 -30)')),
    (null, '왕매워 짬뽕 7호점', '서울 서초구 서초동', '02-777-7777', 1000, ST_GeomFromText('POINT(30 -70)')),
    (null, '왕매워 짬뽕 8호점', '서울 영등포구 당산동', '02-888-8888', 200, ST_GeomFromText('POINT(-40 -50)')),
    (null, '왕매워 짬뽕 9호점', '서울 송파구 가락동', '02-999-9999', 600, ST_GeomFromText('POINT(60 -50)'));
    
select restName, st_buffer(restlocation, 3) as '체인점' from restaurant;

create table manager(
	ManagerID int auto_increment primary key,
	ManagerName varchar(5),
	MobilePhone varchar(15),
	Email varchar(40),
	AreaName varchar(15),
	Area geometry SRID 0);
	
insert into Manager values (Null, '존밴이', '011-123-4567', 'johnbann@kinghot.com', '서율 동/북부지역', st_geomfromtext('POLYGON((-90 0, -90 90, 90 90, 90 -90, 0 -90, 0 0, -90 0))')),
    (Null, '당탕이', '019-321-7654', 'dangtang@kinghot.com', '서율 서부지역', st_geomfromtext('POLYGON((-90 -90, -90 90, 0 90, 0 -90, -90 -90))'));

select ManagerName, Area as '당탕이' from manager where ManagerName = '당탕이';
select ManagerName, Area as '존밴이' from manager where ManagerName = '존밴이';
    
create table Road(
	RoadID int auto_increment primary key,
    RoadName varchar(20),
    RoadLine geometry );
    
insert into road values(Null, '강변북로',st_geomfromtext('linestring(-70 -70, -50 -20, 30 30, 50 70)'));

select RoadName, st_buffer(RoadLine, 1) as '강변북로' from Road;

select ManagerName, Area as '당탕이' from manager where ManagerName = '당탕이';
select ManagerName, Area as '당탕이' from manager where ManagerName = '존밴이';
select restName, st_buffer(restLocation, 3) as '체인점' from restaurant;
select RoadName, st_buffer(RoadLine, 1) as '강변북로' from Road;
    
select ManagerName, AreaName, st_area(area) as "면적 m2" from manager;

select M.ManagerName, R.restName, R.restAddr, M.AreaName from restaurant R, Manager M where ST_contains(M.area, R.restLocation) = 1 order by M.ManagerName;

select R2.restName, R2.restAddr, R2.restPhone, st_distance(R1.restLocation, R2.restLocation) 
	AS "1호점에서 거리" from Restaurant R1, Restaurant R2 where R1.restName = '왕매워 짬뽕 1호점', order by st_distance(R1.restLocation, R2.restLocation);