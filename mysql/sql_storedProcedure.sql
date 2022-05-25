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

drop procedure if exists cursorProc;
delimiter $$
create procedure cursorProc()
begin
	declare userHeight int;
    declare cnt int default 0;
    declare totalHeight int default 0;
    
    declare endOfRow boolean default false;
    
    declare userCursor cursor for select height from usertbl;
    
    declare continue handler for not found set endOfRow = true;
    
    open userCursor;
    
    cursor_loop : loop
		fetch userCursor into userHeight;
        
        if endOfRow then leave cursor_loop;
        end if;
        
        set cnt = cnt + 1;
        set totalHeight = totalHeight + userHeight;
	end loop cursor_loop;
    
    select concat('고객 키의 평균 ==> ', (totalHeight/cnt));
    close userCursor;
end $$
delimiter ;

 call cursorProc();
 
 alter table usertbl add grade varchar(5);
 
 drop procedure if exists gradeProc;
 delimiter $$
 create procedure gradeProc()
 begin
	declare id varchar(10);
    declare hap bigint;
    declare userGrade char(5);
	
    declare endOfRow boolean default false;
    
    declare userCursor cursor for
		select U.userid, sum(price * amount)
			from buytbl B
				right outer join usertbl U
                on B.userid = U.userid
			group by U.userid, U.name;
            
	declare continue handler for not found set endOfRow = true;
    open userCursor;
    grade_loop : loop
		fetch userCursor into id, hap;
        if endOfRow then
			leave grade_loop;
		end if;
        
        case
			when(hap >= 1500) then set userGrade = '최우수고객';
            when(hap >= 1000) then set userGrade = '우수고객';
            when(hap >= 1) then set userGrade = '일반고객';
            else set userGrade = '유령고객';
		end case;
		
        update usertbl set grade = userGrade where userID = id;
	end loop grade_loop;
    close userCursor;
end $$
delimiter ;

call gradeProc();
select * from usertbl;

create database if not exists testdb;
use testdb;
create table if not exists testtbl(id int, txt varchar(10));
insert into testtbl values(1, '레드벨벳');
insert into testtbl values(2, '잇지');
insert into testtbl values(3, '블랙핑크');

drop trigger if exists testTrg;
delimiter //
create trigger testTrg
	after delete
	on testtbl
    for each row
begin
	set @msg = '가수 그룹이 삭제됨' ;
end //
delimiter ;

set @msg = '';
insert into testtbl values(4, '마마무');
select @msg;
update testtbl set txt = '블핑' where id = 3;
select @msg;
delete from testtbl where id = 4;
select @msg;

use sqldb;

drop table buytbl;
create table backup_usertbl(
	userID char(8) not null primary key,
    name varchar(10) not null,
    birthYear int not null,
    addr char(2) not null,
    mobile1 char(3),
    mobile2 char(8),
    height smallint,
    mDate date,
    modType char(2),
    modDatae date,
    modUser varchar(256)
);

drop trigger if exists backUserTbl_UpdateTrg;
delimiter //
create trigger backUserTbl_UpdateTrg
	after update
    on usertbl
    for each row
begin
	insert into backup_userTbl values( old.userID, old.name, old.birthYear, old.addr, old.mobile1, old.mobile2, old.height, old.mDate, '수정', curdate(), current_user());
end //
delimiter ;




drop trigger if exists backUserTbl_UpdateTrg;
delimiter //
create trigger backUserTbl_UpdateTrg
	after update
    on usertbl
    for each row
begin
	insert into backup_userTbl values( old.userID, old.name, old.birthYear, old.addr, old.mobile1, old.mobile2, old.height, old.mDate, '삭제', curdate(), current_user());
end //
delimiter ;

update usertbl set addr = '몽고' where userID = 'JKW';
delete from usertbl where height >= 177;
select * from backup_userTbl;

drop trigger if exists userTbl_InsertTrg;
delimiter //
create trigger userTbl_InsertTrg
	After INSERT
    ON userTBL
    FOR EACH ROW
begin
	signal sqlstate '45000'
		set message_text = '데이터의 입력을 시도했습니다. 귀하의 정보가 서버에 기록되었습니다.';
end //
delimiter ;

#insert into usertbl values('ABC', '에비씨', 1977, '서울', '011', '11111111', 181, '2019-12-25');

drop trigger if exists userTbl_BeforeInsertTrg;
delimiter //
create trigger userTbl_BeforeInsertTrg
	before insert
    on usertbl
    for each row
begin
	if new.birthYear < 1900 then
		set new.birthYear = 0;
	elseif new.birthYear > Year(curdate()) then
		set new.birthYear = Year(curdate());
	end if;
end //
delimiter ;

alter table usertbl drop grade;

insert into usertbl values('AAA', '에이', 1877, '서울', '011', '1112222', 181, '2022-12-25');
insert into usertbl values('BBB', '비이', 2977, '경기', '011', '1113333', 171, '2019-3-25');

select * from usertbl;

show triggers from sqldb;

drop database if exists triggerDB;
create database if not exists triggerDB;
use triggerDB;
create table orderTbl(
	orderNo int auto_increment primary key,
    userID varchar(5),
    prodName varchar(5),
    ordermount int);

create table prodTbl(prodName varchar(5), account int);
create table deliverTbl(
	deliverNo int auto_increment primary key,
    prodName varchar(5),
    account int );

insert into prodTbl values('사과', 100);
insert into prodTbl values('배', 100);
insert into prodTbl values('귤', 100);

drop trigger if exists orderTrg;
delimiter //
create trigger orderTrg
	after insert
    on orderTbl
    for each row
begin
	update prodTbl set account = account - new.ordermount
		where prodName = new.prodName;
end //
delimiter ;

drop trigger if exists prodTrg;
delimiter //
create trigger prodTrg
	after update
    on prodTBL
    for each row
begin
	declare orderAmount int;
    set orderAmount = old.account - new.account;
    insert into deliverTbl(prodName, account)
		values(new.prodName, orderAmount);
end //
delimiter ;

insert into orderTbl values (null, 'JOHN', '배', 5);

select * from orderTbl;
select * from prodTbl;
select * from deliverTbl;

alter table deliverTBL change prodName productName varchar(5);

insert into orderTbl values (null, 'DANG', '사과', 9);
select * from orderTbl;
select * from prodTbl;
select * from deliverTbl;