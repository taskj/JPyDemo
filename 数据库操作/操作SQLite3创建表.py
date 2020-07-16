import sqlite3

#创建连接
con = sqlite3.connect('sqlite3.db')
#创建游标对象
cur = con.cursor()
#编写创建表的sql语句
sql = '''
    create table t_person
    (
    pno INTEGER PRIMARY key autoincrement,
    pname VARCHAR not null,
    age INTEGER
    )'''


try:
    # 执行sql语句
    cur.execute(sql)
    print("")
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    #关闭游标
    cur.close()
    #关闭连接
    con.close()
