drop database moviedb;

create database moviedb;

use moviedb;
create table movietbl
(
	movie_id int,
    movie_title varchar(30),
    movie_director varchar(20),
    movie_star varchar(20),
    movie_script longtext,
    movie_film longblob
)default charset = utf8mb4;

insert into movietbl values(1, '쉰들러 리스트', '스필버그', '리암 니슨', load_file("C:/Users/YONSAI/Desktop/MySQL8_Code/Movies/Schindler.txt"), load_file("C:/Users/YONSAI/Desktop/MySQL8_Code/Movies/Schindler.mp4"));
insert into movietbl values(1, '쉰들러 리스트', '스필버그', '리암 니슨', load_file("C:/Program Files/MySQL/MySQL Server 8.0/Uploads/Schindler.txt"), load_file("C:/Program Files/MySQL/MySQL Server 8.0/Uploads/Schindler.mp4"));

select * from movietbl;