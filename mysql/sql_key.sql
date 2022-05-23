drop database if exists shopdb;
drop database if exists modesldb;
drop database if exists sqldb;
drop database if exists tabledb;

create database tabledb;
use tabledb;

create table tabledb.usertbl (
	userID char(8) not null,
    name varchar(10) not null,
    birthYear int not null,
    addr char(2) not null,
    mobile1 char(3) null,
    mobile2 char(8) null,
    height smallint null,
    mDate date null,
	primary key(userID)
 );

create table tabledb.buytbl (
	num int not null auto_increment,
    userid char(8) not null,
    prodName char(6) not null,
    groupName char(4) null,
    price int not null,
    amount smallint not null,
    primary key(num),
    foreign key (userid) references usertbl(userID)
);
