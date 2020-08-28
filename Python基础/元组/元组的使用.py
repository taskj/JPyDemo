'''
元组和列表很像，都是用来保存多个数据
使用小括号()可以表示元组
元组与列表不同的是，列表是可变的，元组则不可变
'''

words = ['hello','words','go','hi']
nums = (9,4,3,1,7,6,8,6,4,32,4,9)


print(nums.index(1))
print(nums.count(9))

#tuple内置类
print(tuple('hello')) #输出结果('h', 'e', 'l', 'l', 'o')，拆分成了元组

'''
列表转换成元素
'''
print(tuple(words))
'''
元组转换成列表
'''
print(list(nums))

'''
连接元组内数据
'''
height = ("189","174","170")
print('*'.join(height))

'''
元组也可以遍历
'''
for i in nums:
    print(i)