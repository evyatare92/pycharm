import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', passwd='Aa123456',
                       db='dogs', autocommit=True)

# 2
cursor = conn.cursor()
cursor.execute("insert into dogs values ('Rexi',10,'Rotwiler');")
cursor.execute("insert into dogs values ('Melodi',12,'Golden');")
cursor.execute("insert into dogs values ('Lyla',8,'Puddle');")
cursor.close()

# 3
cursor = conn.cursor()
cursor.execute("update dogs set age = 5 where name='Melodi'")
cursor.close()

# 4
cursor = conn.cursor()
cursor.execute("delete from dogs where name='Lyla'")
cursor.close()

# 5
cursor = conn.cursor()
cursor.execute('select * from dogs')
for row in cursor:
    print(row[0])
cursor.close()