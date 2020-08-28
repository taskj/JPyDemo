#列表推导式是用一个简单的语法创建一个列表
nums = [i for i in range(10)]
print(nums)

x = [i for i in range(10) if i % 2]
print(x)

#points 是一个列表，这个列表里的数据都是元组
points = [(x,y) for x in range(5,9) for y in range(10,20)]
print(points)