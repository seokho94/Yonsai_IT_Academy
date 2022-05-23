drop database tabledb;
create database tabledb;

use tabledb;
drop table if exists buytbl, usertbl;
create table usertbl(
	userID char(8),
    name varchar(10),
    birthYear int,
    addr char(2),
    mobile1 char(3),
    mobile2 char(8),
    height smallint,
    mDate date
);

create table buytbl(
	num int,
    userid char(8),
    prodName char(6),
    groupName char(4),
    price int,
    amount smallint
);

alter table usertbl modify column userID char(8) not null;
alter table usertbl modify column name varchar(10) not null;
alter table usertbl modify column birthYear int not null;
alter table usertbl modify column addr char(2) not null;
alter table usertbl modify column mobile1 char(3) null;
alter table usertbl modify column mobile2 char(8) null;
alter table usertbl modify column height smallint null;
alter table usertbl modify column mDate date null;
alter table usertbl modify column userID char(8) primary key;

alter table buytbl modify column num int not null primary key;
alter table buytbl modify column userid char(8) not null;
alter table buytbl modify column prodName char(6) not null;
alter table buytbl modify column groupName char(4) null;
alter table buytbl modify column price int not null;
alter table buytbl modify column amount smallint not null;
alter table buytbl add foreign key(userid) references usertbl(userID);


insert into usertbl values('LSG', '이승기', 1987, '서울', '011', '11111111', 182, '2008-8-8');
insert into usertbl values('KBs', '김범수', 1979, '경남', '011', '22222222', 173, '2012-4-4');
insert into usertbl values('kkh', '김경호', 1971, '전남', '019', '33333333', 177, '2007-7-7');

describe usertbl;
describe buytbl;

drop table if exists buyTBL, usertBl;

create table userTBL(
userID char(8) not null primary key,
name varchar(10) not Null,
birthYear int not null
);
create table buyTBL(
	num int auto_increment not null primary key,
    userID char(8) not null,
    prodName char(6) not null,
    foreign key(userID) references userTBL(userID)
);

drop table if exists buyTBL;
create table buyTBL(
	num int auto_increment not null primary key,
    userID char(8) not null,
    prodName char(6) not null,
    constraint FK_userTBL_buyTBL foreign key(userID) references userTBL(userID)
    );
    
show index from buytbl;
    
alter table buytbl
	drop foreign key FK_userTBL_buyTBL;
alter table buytbl
	add constraint FK_usertbl_buytbl
	foreign key (userID)
	references usertbl(userID)
	on update cascade;
        
use tabledb;
drop table if exists buytbl, usertbl;
create table usertbl
(	userID char(8) not null primary key,
	name varchar(10) not null,
    birthYear int not null,
    email char(30) null unique
);
drop table if exists userTBL;
create table userTBL(
	userID char(8) not null primary key,
    name varchar(10) not null,
    birthYear int not null,
    email char(30) null,
    constraint AK_email unique (email)
);

drop table if exists userTBL;
create table userTBL(
	userID char(8) primary key,
    name varchar(10),
    birthYear int check (birthYear >= 1900 and birthYear <= 2023),
    mobile1 char(3) null,
    constraint CK_name CHECK(name is Not null)
);

alter table usertbl
	add constraint CK_mobile1
    check (mobile1 in('010', '011', '016', '017', '018', '019'));
    
drop table if exists userTBL;
create table userTBL(
	userID char(8) not null primary key,
    name varchar(10) not null,
    birthYear int not null default -1,
    addr char(2) not null default '서울',
    mobile1 char(3) null,
    mobile2 char(8) null,
    height smallint null default 170,
    mDate date null
);

drop table if exists userTBL;
create table userTBL(
	userID char(8) not null primary key,
    name varchar(10) not null,
    birthYear int not null,
    addr char(2) not null,
    mobile1 char(3) null,
    mobile2 char(8) null,
    heigth smallint null,
    mDate date null
);
alter table userTBL
	alter column birthYear SET default -1;
alter table userTBL
	alter column addr set default '서울';
alter table userTBL
	alter column heigth set default 170;
    
insert into usertbl values ('LHL', '이혜리', default, default, '011', '1234567', default, '2023-12-12');
insert into usertbl(userID, name) values('KAY', '김아영');
insert into usertbl values ('WB', '원빈', 1982, '대전', '019', '9876543', 176, '2020-5-5');
select * from usertbl;

create database if not exists compressDB;
use compressDB;
create table normalTBL(emp_no int , first_name varchar(14));
create table compressTBL(emp_no int, first_name varchar(14)) row_format=compressed;
insert into normalTBL select emp_no, first_name from employees.employees;
insert into compressTBL select emp_no, first_name from employees.employees;

show table status from compressDB;
drop database if exists compressDB;

use employees;
create temporary table if not exists temptbl (id int, name char(5));
create temporary table if not exists employees (id int, name char(5));
describe temptbl;
describe employees;

insert into temptbl values(1, 'This');
insert into employees values(2, 'MySQL');
select * from temptbl;
select * from employees;
drop table temptbl;

use employees;
select * from employees;

use tabledb;
alter table usertbl
	add homepage varchar(30)
		default 'http://www.hanbit.co.kr'
        null;
alter table usertbl
	drop column mobile1;
alter table usertbl
	change column name iName varchar(20) null;
alter table usertbl
	drop primary key;
alter table buytbl
	drop foreign key buytbl_ibfk_1;

use tabledb;
drop table if exists buytbl, usertbl;
create table usertbl(
	userID char(8),
    name varchar(10),
    birthYear int,
    addr char(2),
    mobile1 char(3),
    mobile2 char(8),
    height smallint,
    mDate date
);

create table buytbl(
	num int auto_increment primary key,
    userid char(8),
    prodName char(6),
    groupName char(4),
    price int,
    amount smallint
);

insert into usertbl values('KKH', '김경호', 1871, '전남', '019', '33333333', 177, '2007-7-7');
insert into usertbl values('LSG', '이승기', 1987, '서울', '011', '11111111', 182, '2008-8-8');
insert into usertbl values('KBS', '김범수', null, '경남', '011', '22222222', 173, '2012-4-4');
insert into usertbl values('JYP', '조용필', 1950, '경기', '011', '44444444', 166, '2009-4-4');

insert into buytbl values(null, 'KBS', '운동화', null, 30, 2);
insert into buytbl values(null, 'KBS', '노트북', '전자', 1000, 1);
insert into buytbl values(null, 'JYP', '모니터', '전자', 200, 1);
insert into buytbl values(null, 'BBK', '모니터', '전자', 200, 5);

alter table usertbl
	add constraint PK_usertbl_userID
    primary key(userID);
    
desc usertbl;
show index from usertbl;
select * from buytbl;
desc buytbl;
show index from buytbl;

delete from buytbl where userid = 'BBK';

alter table buytbl
	add constraint FK_usertbl_buytbl
    foreign key (userID)
    references usertbl(userID);

set foreign_key_checks = 0;
insert into buytbl values(null, 'BBK', '모니터', '전자', 200, 5);
insert into buytbl values(null, 'KBS', '청바지', '의류', 50, 3);
insert into buytbl values(null, 'BBK', '메모리', '전자', 80, 10);
insert into buytbl values(null, 'SSK', '책', '서적', 15, 5);
insert into buytbl values(null, 'EJW', '책', '서적', 15, 2);
insert into buytbl values(null, 'EJW', '청바지', '의류', 50, 1);
insert into buytbl values(null, 'BBK', '운동화', null, 30, 2);
insert into buytbl values(null, 'EJW', '책', '서적', 15, 1);
insert into buytbl values(null, 'BBK', '운동화', null, 30, 2);


alter table usertbl
	add constraint CK_birthYear
    Check( (birthYear >= 1900 and birthYear <=2023) and (birthYear is not null));

update usertbl set birthYear=1979 where userID='KBS';
update usertbl set birthYear=1971 where userID='KKH';

insert into usertbl values('SSK', '성시경', 1979, '서울', null, null, 186, '2013-12-12');
insert into usertbl values('LJB', '임재범', 1963, '서울', '016', '66666666', 182, '2009-9-9');
insert into usertbl values('YJS', '윤종신', 1969, '경남', null, null, 170, '2005-5-5');
insert into usertbl values('EJW', '은지원', 1972, '경북', '011', '88888888', 174, '2014-3-3');
insert into usertbl values('JKW', '조관우', 1965, '경기', '018', '99999999', 172, '2010-10-10');
insert into usertbl values('BBK', '바비킴', 1973, '서울', '010', '00000000', 173, '2013-5-5');

update usertbl set userID = 'VVK' where userID = 'BBK';
set foreign_key_checks = 1;

select B.userid, U.name, B.prodName, U.addr, concat(U.mobile1, U.mobile2) AS '연락처' from buytbl B inner join usertbl U on B.userid=U.userid;
select count(*) from buytbl;

select B.userid, U.name, B.prodName, U.addr, concat(U.mobile1, U.mobile2) AS '연락처' from buytbl B left outer join usertbl U on B.userid = U.userid order By B.userid;

set foreign_key_checks = 0;
update usertbl set userID = 'BBK' where userID = 'VVK';
set foreign_key_checks = 1;

alter table buytbl drop foreign key FK_usertbl_buytbl;
alter table buytbl add constraint FK_usertbl_buytbl foreign key (userID) references usertbl(userID) on update cascade;

update usertbl set userID = 'VVK' where userID='BBK';
select B.userid, U.name, B.prodName, U.addr, concat(U.mobile1, U.mobile2) as '연락처' from buytbl B inner join usertbl U on B.userid = U.userid order by B.userid;

alter table buytbl drop foreign key FK_usertbl_buytbl;
alter table buytbl add constraint FK_usertbl_buytbl foreign key(userID) references usertbl(userID) on update cascade on delete cascade;

delete from usertbl where userID = 'VVK';
select * from buytbl;

alter table usertbl drop column birthYear;
select * from usertbl;