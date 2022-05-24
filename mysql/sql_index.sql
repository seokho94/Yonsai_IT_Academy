use sqldb;
create table tbl1(
	a int primary key,
    b int,
    c int
);

show index from tbl1;

create table tbl2(
	a int primary key,
    b int unique,
    c int unique,
    d int
);

show index from tbl2;

create table tbl3(
	a int unique,
    b int unique,
    c int unique,
    d int
);

show index from tbl3;

create table tbl4(
	a int unique not null,
    b int unique ,
    c int unique,
    d int
);
show index from tbl4;

create table tbl5(
	a int unique not null,
    b int unique,
    c int unique,
    d int primary key
);
show index from tbl5;

create database if not exists testdb;
use testdb;
drop table if exists usertbl;
create table usertbl(
	userID char(8) not null primary key,
    name varchar(10) not null,
    birthYear int not null,
    addr nchar(2) not null
);

insert into usertbl values('LSG', '이승기', 1987, '서울');
insert into usertbl values('KBS', '김범수', 1979, '경남');
insert into usertbl values('KKH', '김경호', 1971, '전남');
insert into usertbl values('JYP', '조용필', 1950, '경기');
insert into usertbl values('SSK', '성시경', 1979, '서울');
select * from usertbl;

create database if not exists testdb;
use testdb;
drop table if exists clustertbl;
create table clustertbl(
	userID char(8),
    name varchar(10)
);
insert into clustertbl values('LSG', '이승기');
insert into clustertbl values('KBS', '김범수');
insert into clustertbl values('KKH', '김경호');
insert into clustertbl values('JYP', '조용필');
insert into clustertbl values('SSK', '성시경');
insert into clustertbl values('LJB', '임재범');
insert into clustertbl values('YJS', '윤종신');
insert into clustertbl values('EJW', '은지원');
insert into clustertbl values('JKW', '조관우');
insert into clustertbl values('BBK', '바비킴');

select * from clustertbl;

alter table clustertbl add constraint PK_usertbl_userID primary key (userID);
select * from clustertbl;

create database if not exists testdb;
use testdb;
drop table if exists secondarytbl;
create table secondarytbl(
	userID char(8),
    name varchar(10)
);

insert into secondarytbl values('LSG', '이승기');
insert into secondarytbl values('KBS', '김범수');
insert into secondarytbl values('KKH', '김경호');
insert into secondarytbl values('JYP', '조용필');
insert into secondarytbl values('SSK', '성시경');
insert into secondarytbl values('LJB', '임재범');
insert into secondarytbl values('YJS', '윤종신');
insert into secondarytbl values('EJW', '은지원');
insert into secondarytbl values('JKW', '조관우');
insert into secondarytbl values('BBK', '바비킴');

alter table secondarytbl add constraint UK_secondarytbl_userID unique (userID);
select * from secondarytbl;

insert into clustertbl values('FNT', '푸니타');
insert into clustertbl values('KAI', '카아이');
select * from clustertbl;

insert into secondarytbl values('FNT', '푸니타');
insert into secondarytbl values('KAI', '카아이');
select * from secondarytbl;

create database if not exists testdb;
use testdb;
drop table if exists mixedtbl;
create table mixedtbl(
	userID char(8) not null,
    name varchar(10) not null,
    addr char(2)
);

insert into mixedtbl values('LSG', '이승기');
insert into mixedtbl values('KBS', '김범수');
insert into mixedtbl values('KKH', '김경호');
insert into mixedtbl values('JYP', '조용필');
insert into mixedtbl values('SSK', '성시경');
insert into mixedtbl values('LJB', '임재범');
insert into mixedtbl values('YJS', '윤종신');
insert into mixedtbl values('EJW', '은지원');
insert into mixedtbl values('JKW', '조관우');
insert into mixedtbl values('BBK', '바비킴');

alter table mixedtbl add constraint PK_mixedtbl_userID primary key (userID);
alter table mixedtbl add constraint UK_mixedtbl_name unique(name);
show index from mixedtbl;

select addr from mixedtbl where name = '임재범';

use sqldb;
show index from usertbl;
show table status like 'usertbl';

create index idx_usertbl_addr on usertbl(addr);
show table status like 'usertbl';

analyze table usertbl;
show table status like 'usertbl';

#create unique index idx_usertbl_birthYear on usertbl (birthYear);

create unique index idx_usertbl_name on usertbl (name);
show index from usertbl;

create index idx_usertbl_name_birthYear on usertbl(name, birthYear);
drop index idx_usertbl_name on usertbl;
show index from usertbl;

select * from usertbl where name = '윤종신' and birthYear = '1969';
select * from usertbl where name = '윤종신';

create index idx_usertbl_mobile1 on usertbl (mobile1);
select * from usertbl where mobile1 = '011';

drop index idx_usertbl_addr on usertbl;
drop index idx_usertbl_name_birthYear on usertbl;
drop index idx_usertbl_mobile1 on usertbl;

alter table usertbl drop index idx_usertbl_addr;
alter table usertbl drop index idx_usertbl_name_birthYear;
alter table usertbl drop index idx_usdrtbl_mobile1;

select table_name, constraint_name
	from information_schema.referential_constraints
	where constraint_schema = 'sqldb';

alter table buytbl drop foreign key buytbl_ibfk_1;
alter table usertbl drop primary key;

create database if not exists indexdb;
use indexdb;
select count(*) from employees.employees;

create table emp select * from employees.employees order by rand();
create table emp_c select * from employees.employees order by rand();
create table emp_Se select * from employees.employees order by rand();

select * from emp limit 5;
select * from emp_c limit 5;
select * from emp_Se limit 5;

show table status from indexdb;

alter table emp_c add primary key(emp_no);
alter table emp_Se add index idx_emp_no(emp_no);

select * from emp limit 5;
select * from emp_c limit 5;
select * from emp_Se limit 5;

analyze table emp, emp_c, emp_Se;

show index from emp;
show index from emp_c;
show index from emp_Se;
show table status;

use indexdb;
show global status like 'Innodb_pages_read';
select * from emp where emp_no = 100000;
show global status like 'Innodb_pages_read';

show global status like 'innodb_pages_read';
select * from emp_c where emp_no = 100000;
show global status like 'innodb_pages_read';

show global status like 'innodb_pages_read';
select * from emp_Se where emp_no = 100000;
show global status like 'innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp where emp_no < 11000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_c where emp_no < 11000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_c where emp_no < 500000 limit 10000000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_c Ignore index(primary) where emp_no < 500000 limit 10000000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_c limit 10000000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_Se Ignore index(primary) where emp_no < 500000 limit 10000000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_Se limit 10000000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_Se where emp_no < 11000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_Se Ignore index(idx_emp_no) where emp_no < 11000;
show global status like 'Innodb_pages_read';

show global status like 'Innodb_pages_read';
select * from emp_c Ignore index(primary) where emp_no < 400000 limit 500000;
show global status like 'Innodb_pages_read';

select * from emp_Se where emp_no < 60000 limit 500000;

select * from emp_c where emp_no = 100000;

show global status like 'Innodb_pages_read';
select * from emp_c where emp_no*1 = 100000;
show global status like 'Innodb_pages_read';

select * from emp_c where emp_no = 100000 / 1;

alter table emp add index idx_gender (gender);
analyze table Emp;
show index from Emp;

select * from emp where gender = 'M' limit 500000;

select * from emp ignore index (idx_gender) where gender = 'M' Limit 500000;

use sqldb;
select name, birthYear, addr from usertbl where userID = 'KKH';