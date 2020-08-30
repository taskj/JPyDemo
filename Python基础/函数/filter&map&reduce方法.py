'''
filter 对可迭代对象进行过滤，得到的是一个filter对象
python2的时候是内置函数，python3修改成一个内置类
'''
ages = [12,23,30,17,16,22,29]
#filter可给定两个参数，第一个是函数，第二个是可迭代对象
x = filter(lambda ele : ele > 18,ages)

adult = list(x)
print(adult)


#求和
from functools import reduce
scores = [100,89,76,87]
print(reduce(lambda ele1,ele2:ele1+ele2,scores))

