use sqldb;
select U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
	from usertbl U
		LEFT OUTER JOIN buytbl B
			on U.userID = B.userID
	where B.prodName is NULL
    order by U.userID;
    
    use employees;
    select count(*) as '데이터개수'
		from employees
			cross join titles;

select if (100>200, '참이다', '거짓이다');
select ifnull(null, '널이군요'), ifnull(100, '널이군요');
select nullif(100, 100), nullif(200, 100);
select case 10
		when 1 then '일'
        when 5 then '오'
        when 10 then '십'
        else '모름'
        
	end as 'case연습';

select ascii('A'), char(65);
select bit_length('abc'), char_length('abc'), length('abc');
select bit_length('가나다'), char_length('가나다'), length('가나다');

select concat_ws('/', '2025', '01', '01');
select elt(2, '하나', '둘', '셋'), field('둘', '하나', '둘', '셋'), find_in_set('둘', '하나, 둘, 셋'), instr('하나둘셋', '둘'), locate('둘', '하나둘셋');

select format(123456.12345, 4);
select bin(31), hex(31), oct(31);

select insert ('abcdefghi', 3, 4, '@@@@'), insert('abcdefghi', 3, 2,'@@@@@');

select left('abcdefghi', 3), right('abcdefghi', 3);
select LOWER('abcdEFGH'), UPPER('abcdEFGH');
select lpad('이것이', 5, '##'), rpad('이것이', 5, '##');

select ltrim('      이것이'), rtrim('이것이     ');
select trim('       이것이      '), trim(both 'ㅋ' from 'ㅋㅋㅋ재밌어요.ㅋㅋㅋ');

select repeat('이것이', 3);
select replace('이것이 MySQL이다', '이것이', 'This is');