person = {'name':'zhangsan','age':14,'addr':'usa','gender':'male'}


'''
把name对应的键值对删除了，执行结果是被删除的value
'''
x = person.pop('name')
print(x) #('gender', 'male')
print(person)

'''
popitem 删除一个元素，结果是被删除这个元素的元素组成的键值对
'''
result = person.popitem()
print(result)
print(person)

'''
删除一个的key
'''
del person['addr']
print(person)

'''
清空字典所有内容
'''
person.clear()
print(person)
