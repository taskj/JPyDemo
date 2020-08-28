person = {'name':'zhangsan',
          'age':18,
          'math':96,
          'chinese':100,
          'english':88,
          'height':180,
          'weight':150,
          'age':28, #会替换上一个age的值
          'isPass':True, #可以是布尔值
          'hobbies':['唱','跳','篮球','rap'], #可以是列表
          4:'good',
          ('yes','hello'):100 #['yes','no'] 如果是列表类型这种可变的就不行
          }

'''
特殊在列表和元组是一个单一的数据，但是字典是键值对的形式
'''

'''
第一种遍历方式
直接for...in循环字典
'''
for x in person: #for..in循环获取的是key
    print(x,"=",person[x])

'''
第二种遍历方式
获取所有的key，然后再遍历key，根据key获取value
'''
print(person.keys()) #输出dict_keys(['name', 'age', 'math', 'chinese', 'english', 'height', 'weight', 'isPass', 'hobbies', 4, ('yes', 'hello')])
for k in person.keys():
    print(k,"=",person[k])
    
'''
第三种方式，获取所有value
只拿value不拿key
'''
for v in person.values():
    print(v)

'''
第四种方式
'''
print(person.items()) #dict_items([('name', 'zhangsan'), ('age', 28), ('math', 96), ('chinese', 100), ('english', 88), ('height', 180), ('weight', 150), ('isPass', True), ('hobbies', ['唱', '跳', '篮球', 'rap']), (4, 'good'), (('yes', 'hello'), 100)])
for item in person.items(): #列表里的元素是元组，把元组当作整体进行遍历
    print(item[0],"=",item[1])
'''
上下两者等价
'''
for v,k in person.items():
    print(v,"=","k")
