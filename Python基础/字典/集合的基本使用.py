'''
'''
'''
集合是一个不重复的无序，可以使用{}或者set来表示
{}有两种意思，字典，集合
{}里如果放的是键值对，它就是一个字典，如果放的是单个值，就是一个集合
'''
person = {'name':'zhangsan','age':18} #字典
x = {'hello',1,'good'} #集合

names = {'zhangsan','lisi','jack','tony','jack','lisi'}
print(names) #{'jack', 'zhangsan', 'tony', 'lisi'} 但是位置和数据是无序不固定的

#set不能进行增删查改
names.add('jesus')
print(names)

names.remove('jack')
print(names)