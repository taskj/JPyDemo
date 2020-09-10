import pymysql

#打开一个数据库连接
db = pymysql.connect(host='192.168.229.130',
                     user='taskj',
                     password='123456',
                     database='pystudy',
                     port=3306,
                     charset='utf8')

cursor = db.cursor()
cursor.execute('select * from student')
cursor.close()
db.commit()
print(cursor.fetchall())
db.close();


'''
((1, '郭德纲', '男', 1, 134.0, '二人转', datetime.date(1994, 12, 21), '北京'), 
(2, '张学友', '男', 0, 98.0, '歌神', datetime.date(1960, 11, 1), '香港'), 
(3, '赵雅芝', '女', 1, 66.0, '女人的', datetime.date(1994, 12, 28), '香港'), 
(4, '王宝强', '男', 1, 77.0, '绿帽子', datetime.date(1993, 6, 25), '北京'), 
(5, '赵丽颖', '女', 1, 33.0, '女神', datetime.date(1991, 12, 19), '上海'), 
(6, '马蓉', '女', 1, 99.0, '不老女神', datetime.date(1940, 10, 24), '上海'), 
(7, '刘德华', '男', 0, 154.0, '四大天王', datetime.date(1955, 7, 15), '香港'), 
(8, '周杰伦', '男', 1, 222.0, '亚洲歌王', datetime.date(1984, 6, 13), '北京'), 
(9, '马化腾', '男', 0, 123.0, '抄袭王', datetime.date(1973, 11, 16), '北京'), 
(10, '马云', '男', 1, 888.0, '有钱人', datetime.date(1964, 6, 12), '上海'), 
(11, '郭富城', '男', 1, 12.0, '舞王', datetime.date(1955, 7, 15), '香港'), 
(12, '昆凌', '女', 0, 67.0, '天王嫂', datetime.date(1984, 8, 25), '上海'), 
(13, '张柏芝', '女', 1, 90.0, '无', datetime.date(1990, 3, 23), '香港'), 
(14, '杨颖', '女', 1, 87.0, 'baby', datetime.date(1983, 6, 17), '上海'), 
(15, '尼古拉斯', '男', 1, 999.0, '赵四', datetime.date(1995, 1, 1), '北京'), 
(18, '孙红雷', '女', 1, 767.0, '哈哈', datetime.date(1995, 1, 18), '上海'), 
(19, '杨幂', '女', 0, 576.0, 'hello', datetime.date(1994, 8, 29), '上海'), 
(20, '黎明', '男', 1, 76.0, 'nihao', datetime.date(1991, 11, 29), '香港'))
Process finished with exit code 0
'''

