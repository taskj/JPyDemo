'''
遍历 将所有的数据都访问一遍，针对的是可迭代对象
'''
'''
while 循环遍历
for...in 循环遍历
'''
names = ['吕布','周瑜','诸葛亮','张飞','关羽']

'''
for...in 循环的本质就是不断调用迭代器next方法查找下一个数据
'''
for name in names:
    print(name)


i = 0
while i < len(names):
    print(names[i])
    i += 1
