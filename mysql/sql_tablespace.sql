show variables like 'innodb_data_file_path';
show variables like 'innodb_file_per_table';


create tablespace ts_a add datafile 'ts_a.ibd';
create tablespace ts_b add datafile 'ts_b.ibd';
create tablespace ts_c add datafile 'ts_c.ibd';

use sqldb;
create table table_a (id int) tablespace ts_a;
create table table_b (id int);
alter table table_b tablespace ts_b;
create table table_c (select * from employees.salaries);
alter table table_c tablespace ts_c;