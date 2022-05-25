use sqlDB;
drop procedure if exists userProc;
delimiter $$
create procedure userProc()
begin
	select * from usertbl;
end$$
delimiter ;

call userProc();

drop procedure if exists userProc1;
delimiter $$
create procedure userProc1(in userName varChar(10))
begin
	select * from usertbl where name = userName;
end $$
delimiter ;

call userProc1('조관우');

drop procedure if exists userProc2;
delimiter $$
create procedure userProc2(
	in userBirth int,
    in userHeight int
)
begin
	select * from usertbl
		where birthYear > userBirth and height > userHeight;
end $$
delimiter ;

call userProc2(1970, 178);

drop procedure if exists userProc3;
delimiter $$
create procedure userProc3(
	in txtvalue char(10),
	out outvalue int
)
begin 
	insert into testtbl values(null, txtvalue);
    select max(id) into outvalue from testtbl;
end $$
delimiter ;
create table if not exists testtbl(
	id int auto_increment primary key,
    txt char(10)
);

call userProc3 ('테스트값', @myValue);
select concat('현재 입력된 ID 값 ==>', @myValue);

drop procedure if exists ifelseProc;
delimiter $$
create procedure ifelseProc(
	in userName varchar(10)
)
begin
	declare bYear int;
    select birthYear into bYear From usertbl
		where name = userName;
	if (bYear >= 1980) then
		select '아직 젊군요..';
	else
		select '나이가 지긋하시네요.';
	end if;
end $$
delimiter ;

call ifelseProc('조용필');

drop procedure if exists caseProc;
delimiter $$
create procedure caseProc(
	in userName varchar(10)
)
begin
	declare bYear int;
    declare tti char(3);
    select birthYear into bYear from usertbl
		where name = userName;
	case
		when(bYear%12 =0) then set tti = '원숭이';
        when(bYear%12 =1) then set tti = '닭';
        when(bYear%12 =2) then set tti = '개';
        when(bYear%12 =3) then set tti = '돼지';
        when(bYear%12 =4) then set tti = '쥐';
        when(bYear%12 =5) then set tti = '소';
        when(bYear%12 =6) then set tti = '호랑이';
        when(bYear%12 =7) then set tti = '토끼';
        when(bYear%12 =8) then set tti = '용';
        when(bYear%12 =9) then set tti = '뱀';
        when(bYear%12 =10) then set tti = '말';
        else set tti = '양';
	end case;
    select concat(userName, '의 띠==>', tti);
end $$
delimiter ;

call caseProc('김범수');

drop table if exists gugutbl;
create table gugutbl (txt varchar(100));

drop procedure if exists whileProc;
delimiter $$
create procedure whileProc()
begin
	declare str varchar(100);
    declare i int;
    declare k int;
    set i = 2;
    
    while(i < 10) do
		set str = '';
        set k = 1;
        while (k < 10) do
			set str = concat(str, ' ', i, 'x', k, '=', i*k);
            set k = k + 1;
		end while;
        set i = i + 1;
        insert into gugutbl values(str);
	end while;
end $$
delimiter ;

call whileProc();
select * from gugutbl;

drop procedure if exists errorProc;
delimiter $$
create procedure errorProc()
begin
	declare i int;
    declare hap int;
    declare saveHap int;
	
    declare exit handler for 1264
    begin
		select concat('int 오버플로 직전의 합계 -->', saveHap);
        select concat('1+2+3+4+...+', i , '=오버플로');
	end;
	set i = 1;
	set hap = 0;

	while(true) do
		set saveHap = hap;
		set hap = hap + i;
		set i = i + 1;
	end while;
end $$
delimiter ;

call errorProc();

drop procedure if exists nameProc;
delimiter $$
create procedure nameProc(
	in tblName varchar(20)
)
begin
	select * from tblName;
end $$
delimiter ;

call nameProc('usertbl');

drop procedure if exists nameProc;
delimiter $$
create procedure nameProc(
	in tblName varchar(20)
)
begin
	set @sqlQuery = concat('select * from', tblName);
	prepare myQuery from @sqlQuery;
    execute myQuery;
    deallocate prepare myQuery;
end$$
delimiter ;

call nameProc ('usertbl');

use sqldb;

set global log_bin_trust_function_creators = 1;
show global variables like 'log_bin_trust_fuction_creators';
set global log_bin_trust_function_creators = on;

drop function if exists userFunc;
delimiter $$
create function userFunc(value1 int, value2 int)
	returns int
begin
	return value1 + value2;
end $$
delimiter ;
select userFunc(100, 200);

drop function if exists getAgeFunc;
delimiter $$
create function getAgeFunc(bYear int)
	returns int
begin
	declare age int;
    set age = YEAR(CURDATE()) - bYear;
    return age;
end $$
delimiter ;

select getAgeFunc(1979);

select getAgeFunc(1979) into @age1979;
select getAgeFunc(1997) into @age1989;
select concat('1997년과 1979년의 나이차 ==>' , (@age1979 - @age1989));
select userID, name, getAgeFunc(birthYear) as '만 나이' from usertbl;

show create function getAgeFunc;
drop function getAgeFunc;

