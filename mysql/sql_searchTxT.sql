show variables like 'innodb_ft_min_token_size';

create database if not exists FulltextDB;
use FulltextDB;
drop table if exists Fulltexttbl;
create table Fulltexttbl(
	id int auto_increment primary key,
    title varchar(15) not null,
    description varchar(1000)
);

insert into FulltextTbl Values
	(null, '광해, 왕이 된 남자', '왕윙르르 둘러싼 권력 다툼과 당쟁응로 혼란이 극에 달한 광해군 8년'),
    (null, '간첩', '남한 내에 고장산첩 5만 명이 암약하고 있으며 특히 권력 핵심부에도 침투해있다.'),
    (null, '남자가 사랑할 때', '대책 없는 한 남자이야기. 형 집에 얹혀 살며 조카한테 무시당하는 남자'),
    (null, '레지던트 이블 5', '인류 구원의 마지막 퍼즐, 이 여자가 모든 것을 끝낸다.'),
    (null, '파괴자들', '사랑은 모든 것을 파괴한다! 한 여자를 구하기 위한, 두 남자의 잔인한 액션 본능!'),
    (null, '킹콩을 들다', '역도에 목숨을 건 시골소녀들이 만드는 기적 같은 신화.'),
    (null, '테드', '지상최대 황금찾기 프로젝트! 500년 전 사라진 황금도시를 찾아라!'),
    (null, '타이타닉', '비극 속에 침몰한 세기의 사랑, 스크린에 되살아날 영원한 감동'),
    (null, '8월의 크리스마스', '시한부 인생 사진사와 여자 주차 단속원과의 미묘한 사랑'),
    (null, '늑대와 춤을', '늑대와 친해져 모닥불 아래서 함께 춤을 추는 전쟁 영웅 이야기'),
    (null, '국가대표', '동계올림픽 유치를 위해 정식 종목인 스키점프 국가대표팀이 급조된다.'),
    (null, '쇼생크 탈출', '그는 누명을 쓰고 쇼생크 감옥에 감금된다. 그리고 역사적인 탈출.'),
    (null, '인생을 아름다워', '귀도는 삼촌의 호텔에서 웨이터로 일하면서 또 다시 도라를 만난다.'),
    (null, '사운드 오브 뮤직', '수녀 지망생 마리아는 명문 트랩가의 가정교사로 들어간다'),
    (null, '매트릭스', '2199년.인공 두뇌를 가진 컴퓨터가 지배하는 세계.');
    
select * from FulltextTbl where description like '%남자%';

create FULLTEXT index idx_description on FulltextTbl(description);
show index from FulltextTbl;

select * from FulltextTbl where match(description) against('남자*' in boolean mode);

select *, match(description) against('남자* 여자*' in boolean mode) as 점수 from FulltextTbl where match(description) against('남자* 여자*' in boolean mode);

select * from FulltextTbl where match(description) against('+남자* +여자*' in boolean mode);
select * from FulltextTbl where match(description) against('남자* -여자*' in boolean mode);

set global innodb_ft_aux_table = 'fulltextdb/fulltexttbl';
select word, doc_count, doc_id, position from information_schema.innodb_ft_index_table;

drop index idx_description on FulltextTbl;

create table user_stopword (value varchar(30));
insert into user_stopword values('그는'),('그리고'),('극에');

set global innodb_ft_server_stopword_table = 'fulltextdb/user_stopword';
show global variables like 'innodb_ft_server_stopword_table';

create fulltext index idx_description on FulltextTbl(description);

select word, doc_count, doc_id, position from information_schema.innodb_ft_index_table;

create database if not exists partDB;
use partDB;
drop table if exists partTBL;
create table partTBL(
	userID char(8) not null,
    name varchar(10) not null,
    birthYear int not null,
    addr char(2) not null)
partition by range(birthYear) (
	partition part1 values less than (1971),
    partition part2 values less than (1979),
    partition part3 values less than maxvalue
);

insert into partTBL select userID, name, birthYear, addr from sqlDB.userTbl;
select * from partTBL;

select table_schema, table_name, partition_name, partition_ordinal_position, table_rows from information_schema.partitions where table_name = 'parttbl';

select * from partTBL where birthYear <= 1965;

explain select * from partTBL where birthYear <= 1965;

alter table partTBL	reorganize partition part3 into(partition part3 values less than (1986), partition part4 values less than maxvalue);
optimize table partTBL;

alter table partTBL reorganize partition part1, part2 into (partition part12 values less than (1979));
optimize table partTBL;

alter table partTBL drop partition part12;
optimize table partTBL;
select * from partTBL;

drop table if exists partTBL;
create table partTBL(
	userID char(8) not null,
    name varchar(10) not null,
    birthYear int not null,
    addr char(2) not null)
partition by list columns(addr) (partition part1 values in ('서울', '경기'), partition part2 values in ('충북', '충남'), partition part3 values in ('경북', '경남'),  
partition part4 values in ('전북', '전남'), partition part5 values in ('강원', '제주'));

insert into partTBL select userID, name, birthYear, addr from sqldb.usertbl;
select * from partTBL;

select * from partTBL where birthYear <= 1965;

explain select * from partTBL where birthYear <= 1965;

alter table partTBL reorganize partition part3 into(partition part3 values less than (1986), partition part4 values less than maxvalue);
optimize table partTBL;

alter table partTBL	reorganize partition part1, part2 into ( partition part12 values less than(1979));
optimize table partTBL;

alter table partTBL drop partition part12;
optimize table partTBL;

select * from partTBL;