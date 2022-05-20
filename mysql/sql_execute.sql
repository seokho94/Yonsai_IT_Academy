use sqldb;

select userID, SUM(price*amount) AS '총구매액'
	from buytbl
    group by userID
    order by SUM(price*amount) DESC;
    
select B.userID, U.name, SUM(price*amount) AS '총구매액'
	from buytbl B
		Inner join usertbl U
			ON B.userID = U.userID
	Group By B.userID, U.name
    order by SUM(price*amount) DESC;

select B.userID, U.name, SUM(price*amount) AS '총구매액'
	from buytbl B
		right outer join usertbl U
			on B.userID = U.userID
	group by B.userID, U.name
    order by SUM(price*amount) DESC;
    
select U.userID, U.name, SUM(price*amount) AS '총구매액'
	from buytbl B
		right outer join usertbl U
			on B.userID = U.userID
	group by U.userID, U.name
    order by SUM(price*amount) DESC;
    
select U.userID, U.name, SUM(price*amount) AS '총구매액',
		case
			when (SUM(price*amount) >= 1500) then '최우수고객'
			when (SUM(price*amount) >= 1000) then '우수고객'
			when (SUM(price*amount) >= 1) then '일반고객'
			else '유령고객'
		end as '고객등급'
    from buytbl B
		right outer join usertbl U
			on B.userID = U.userID
	group by U.userID, U.name
    order by sum(price*amount) DESC;
    
drop procedure if exists whileProc;
DELIMITER $$
create procedure whileProc()
Begin
		declare i int;
		declare hap int;
	set i =1;
	set hap =0;
		while(i<=100) DO
			set hap = hap+i;
			set i = i+1;
		end while;
            
		select hap;
end $$
DELIMITER ;
call whileProc();

drop procedure if exists whileProc2;
delimiter $$
create procedure whileProc2()
Begin
	declare i int;
    declare hap int;
    set i = 1;
    set hap = 0;
    
    myWhile: while (i <= 100) Do
		IF(i%7 = 0) Then
			set i = i + 1;
            iterate myWhile;
		end if;
			set hap = hap + i;
            if(hap > 1000) then
				leave myWhile;
		end if;
			set i = i + 1;
		end while;
        
        select hap;
end $$
delimiter ;
call whileProc2();

drop procedure if exists errorProc;
delimiter $$
create procedure errorProc()
begin
	declare continue handler for 1146 select '테이블이 없어요ㅠㅠ' as '메시지';
	select * from noTable;
end $$
delimiter ;
Call errorProc();

drop procedure if exists errorProc2;
delimiter $$
create procedure errorProc2()
begin
	declare continue handler for sqlexception
    begin
		show errors;
        select '오류가 발생했네요. 작업은 취소시켰습니다.' as '메시지';
        rollback;
	end;
    insert into usertbl values('LSG', '이상구', 1988, '서울', null, null, 170, current_date());
    end $$
    delimiter ;
    call errorProc2();
    
    use sqldb;
    prepare myQuery from 'select * from usertbl where userID = "EJW"';
    execute myQuery;
    deallocate prepare myQuery;
    
    use sqldb;
    drop table if exists myTable;
    create table myTable (id int auto_increment primary key, mDate datetime);
    
    set @curDate = current_timestamp();
    
    prepare myQuery from 'insert into myTable values(null, ?)';
    execute myQuery using @curDATE;
    deallocate prepare myQuery;
    
    select * from myTable;