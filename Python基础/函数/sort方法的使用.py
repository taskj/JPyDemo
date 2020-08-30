#有几个内置函数和内置类，用到了匿名函数
nums = [4,8,2,1,7,6]
# nums.sort()
# print(nums)


ints = (5,9,2,1,3,8,7,4)
#sorted内置函数，不会改变原有数据，而是生成一个新的结果
x = sorted(ints)
print(ints)

students = [
    {'name':'zhangsan','age':14,'score':98,'height':198},
    {'name':'lisi','age':13,'score':38,'height':23},
    {'name':'wangwu','age':12,'score':48,'height':131},
    {'name':'zhaoliu','age':8,'score':28,'height':129},
]

#字典与字典之间不能使用比较符运算
#students.sort()



def foo(ele):
    print("ele = {}".format(ele))
    return ele['age'] #通过返回值告诉sort方法，按照元素的属性进行排序
'''
需要传递参数key,指定比较规则
key参数类型是一个函数
在sort内部实现的时候，调用了foo方法，并传入了一个参数，参数就是列表里面的元素
'''
students.sort(key=foo)



