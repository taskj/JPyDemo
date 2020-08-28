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

print(person)

'''
#1 字典里的key不允许重复，如果key重复了，最后一个key对应的值会覆盖前一个
#2 字典里面的value可以是任意数据类型，但是key只能使用不可变数据类型，一般是字符串
'''