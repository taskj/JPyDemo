#列表可以存储任意数据类型，但是一般情况下，我们都存储单一的数据类型
names = ['zhangsan','lisi','wangwu']
scores = [100,99,88,60,2]

'''
列表里面的每一个元素代表什么呢？
列表只能储存的值，但无法对值进行描述
'''
person = ['zhangsan',18,98,97,93,180,150]

'''
字典不仅可以保存值，还能对值进行描述
使用大括号{}来表示一个字典，不仅有值value,还有值的描述key
字典里面的数据都是以键值对key-value的形式保留的
key和value之间使用冒号:连接
多个键值之间使用逗号,分开
'''
person = {'name':'zhangsan',
          'age':18,
          'math':96,
          'chinese':100,
          'english':88,
          'height':180,
          'weight':150
          }
