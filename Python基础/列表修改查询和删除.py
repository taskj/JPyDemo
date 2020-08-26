names = ['特朗普','奥巴马','布什','克林顿','尼克松','华盛顿','林肯']

'''
删除数据有三个相关的方法 pop remove clear
'''

'''
pop方法会默认删除列表里面最后一个数据，并返回这个元素
pop也可以传入传入index参数，用来指定位置上的数据
'''
x = names.pop()
#x = names.pop(3)
print(x)

'''
remove 用来删除指定的元素
'''
names.remove('特朗普')
#names.remove('123321') 如果数据不存在就报错
print(names)

'''
clear 直接清空这个列表
'''

names.clear()
print(names)


'''
查询相关方法
'''
tanks = ['亚瑟','程咬金','盾山','张飞','廉颇','程咬金']
#返回元素的索引
print(tanks.index('盾山')) # 返回2
#print(tanks.index('庄周')) 如果元素不存在，会报错
#返回元素的个数
print(tanks.count('程咬金')) # 返回2
#in 运算符
print('张飞' in tanks) # True
print('苏烈' in tanks) # False

'''
修改元素
'''
tanks[5] = '黄盖'
print(tanks)



