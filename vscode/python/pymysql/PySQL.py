import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')

cur = conn.cursor()

cur.execute("create table if not exists userTable(id char(4), userBane char(15), email char(20), birthYear int)")

cur.execute("insert into userTable values('john', 'Hohn Bann', 'john@naver.com', 1990)")
cur.execute("insert into userTable values('kim', 'Kim Chi', 'kim@daum.nt', 1992)")
cur.execute("insert into userTable values('lee', 'Lee Pal', 'lee@paran.com', 1988)")
cur.execute("insert into userTable values('park', 'Park Su', 'park@gmail.com', 1980)")

conn.commit()

conn.close();