#列表保存多个数据，是有有序可变。
#操作列表，一般为增加数据，查询数据，修改数据以及查询数据。

names = ['特朗普','奥巴马','布什','克林顿','尼克松','华盛顿','林肯']

#添加元素的方法 append insert extend

'''
append在列表最后面追加一个数据
'''
names.append('肯尼迪')
print(names)


'''
insert 需要两个参数
index 表示下标
object 表示对象，具体插入哪个数据
'''
names.insert(2,'希拉里')
print(names)


x = ['嬴政','李世民','蒋介石']
'''
extend(iterable) 需要的一个可迭代对象
A.extend(B) ==> 将可迭代对象B添加到A里
'''
names.extend(x)
print(names)