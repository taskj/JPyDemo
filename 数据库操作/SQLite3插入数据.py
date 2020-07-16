import sqlite3

#创建连接
con = sqlite3.connect('sqlite3.db')

#创建游标对象
cur = con.cursor()

sql = '''
    insert into t_person(pname,age) values (?,?)
'''

try:
    # 执行sql
    cur.execute(sql,("张三",24))
    #提交事务
    con.commit()
    print("插入数据成功")
except Exception as e:
    print(e)
    con.rollback()
    print("插入数据表失败")
finally:
    #关闭游标
    cur.close()
    #关闭数据库
    con.close()