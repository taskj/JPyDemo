#去重排序
nums = [5,8,7,6,4,1,3,5,1,8,4]

x = set(nums)
print(x) #转换成集合去重
y = list(x)
y.sort(reverse=True) #[8, 7, 6, 5, 4, 3, 1]
print(y)

z = list({'name':'zhangsan','age':14,'score':98})
print(z)

#Python有一个内置函数 eval(),可以执行字符串里面的代码
a = 'input("请输入您的用户名：")'
b = '1+1'
print(eval(b))


import json
'''
json的使用，把列表，元组，字典等转换成JSON字符串
'''
person = {'name':'zhangsan','age':14,'gender':'female'}
'''
字典如果想把它传给前端页面或者把字典写入到一个文件里面
'{"name":"zhangsan","age":14,"gender":"female"}'
'''
m = json.dumps(person) #dumps 将字典，元组，集合转换成JSON字符串
print(m) #{"name": "zhangsan", "age": 14, "gender": "female"}
print(type(m)) #<class 'str'>
#print(m['name']) #不能这样使用，因为m是一个字符串

n = '{"name":"lisi","age":17,"gender":"male"}'
p = eval(n) #eval可以将JSON字符串转换成python里面的字典
print(type(p)) #<class 'dict'>
s = json.loads(n) #json.loads 方法也可以将JSON字符串转换成python里面的字典
print(s) #{'name': 'lisi', 'age': 17, 'gender': 'male'}
print(type(s)) #<class 'dict'>



