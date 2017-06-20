import pymysql
from config import conn_cnf
import random
conn = pymysql.connect(**conn_cnf)
cur = conn.cursor()

batch_size = 100
total_size = 10000

db = "db"
tb = "tb1"

sql = ""
tmpsql = ""

conn.begin()

for idx in range(0, total_size+1):
	tmpsql = "update {}.{}  set num = {} where id = {};".format(db, tb, random.randint(5000,6000), idx)
	sql += tmpsql
	if not idx % batch_size:
		cur.execute(sql)
		conn.commit()
		conn.begin()
		sql = ""

conn.commit()

if sql:
	conn.begin()
	cur.execute(sql)
	conn.commit()
cur.close()
conn.close()