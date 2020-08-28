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
查找数据，字典的数据在保存时是无序的，不能通过下标来查询
'''
print(person['name']) #使用key获取到对应的value

'''
需求，获取一个不存在的key时，不报错，如果这个key不存在，使用默认值
使用get方法，如果key不存在，会默认返回None，而不报错
'''
print(person.get('length')) #返回None
print(person.get('length',888)) #获取不到，给定默认值888,如果key存在，不会改变值


