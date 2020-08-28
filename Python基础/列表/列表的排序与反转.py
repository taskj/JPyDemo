nums = [6,5,3,1,8,7,2,4]

'''
调用列表 sort 方法可以直接对列表进行排序
reverse 参数用于反转排序
'''
nums.sort(reverse=True)
print(nums)

'''
内置函数sorted(),不会改变原来的列表数据，会生成一个新的有序数据
'''
x = sorted(nums)
print(nums)
print(x)

'''
reverse() 反转 等同 names[::-1]
'''
names = ['zhangsan','lisi','wangwu']
names.reverse()
print(names)