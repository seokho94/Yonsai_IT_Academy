use tabledb;

create view v_usertbl as select userid, name, addr from usertbl;
select * from v_usertbl;

select U.userid, U.name, B.prodName, U.addr, concat(U.mobile1, U.mobile2) as '연락처' from usertbl U inner join buytbl B on U.userid = B.userid;

create View v_userbuytbl as select U.userid, U.name, B.prodName, U.addr, concat(U.mobile1, U.mobile2) as '연락처' from usertbl U inner join buytbl B on U.userid = B.userid;

select * from v_userbuytbl where name = '김범수';

use sqldb;
create view v_userbuytbl as select U.userid as 'USER ID', U.name as 'USER NAME', B.prodNAme as 'PRODUCT NAME', U.addr, concat(U.mobile1, U.mobile2) as 'MOBILE PHONE' 
	from usertbl U inner join buytbl B on U.userid = B.userid;
select `USER ID`, `USER NAME` from v_userbuytbl;

alter view v_userbuytbl as select U.userid as '사용자 아이디', U.name as '이름', B.prodName as '제품 이름', U.addr, concat(U.mobile1, U.mobile2) as '전화 번호' from usertbl U inner join buytbl B
	on U.userid = B.userid;

select `이름`,`전화 번호` from v_userbuytbl;
drop view v_userbuytbl;

create or replace view v_usertbl as select userid, name, addr from usertbl;
describe v_usertbl;

show create view v_usertbl;

update v_usertbl set addr = '부산' where userid = 'JKW';

##insert into v_usertbl(userid, name, addr) values('KBM','김병만','충북');

create view v_sum as select userid as 'userid', sum(price*amount) as 'total' from buytbl group by userid;
select * from v_sum;

select * from information_schema.views where table_schema = 'sqldb' and table_name = 'v_sum';

create view v_height177 as select * from usertbl where height >= 177;
select * from v_height177;

delete from v_height177 where height < 177;
insert into v_height177 values('KBM', '김병만', 1977, '경기', '010', '55555555', 158, '2023-01-01');
alter view v_height177 as select * from usertbl where height >=177 with check option;

##insert into v_height177 values('SJH', '서장훈', 2006, '서울', '010', '33333333', 155, '2023-3-3');

create view v_userbuytbl as select U.userid, U.name, B.prodName, U.addr, concat(U.mobile1, U.mobile2) as mobile from usertbl U inner join buytbl B on U.userid = B.userid;

#2개의 테이블 뷰는 업데이트 불가능
#insert into v_userbuytbl values('PKL', '박겅림', '운동화', '경기', '00000000', '2023-2-2');

drop table if exists buytbl, usertbl;
##테이블 삭제이 뷰도 함께 삭제
##select * from v_userbuytbl;
check table v_userbuytbl;