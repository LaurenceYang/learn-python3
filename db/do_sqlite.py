import  sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('create table if not EXISTS user (id VARCHAR(20) PRIMARY key, name VARCHAR(20))')

cursor.execute('insert into user (id, name) VALUES (\'3\', \'xiaoxiao\')')

print('rowcount =', cursor.rowcount)

cursor.close()

conn.commit()
conn.close()

# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
# cursor.execute('select * from user where id=?', '1')
cursor.execute('select * from user')
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()