person = {'name':'zhangsan','age':14}

'''
直接使用key可修改对应的value
如果key存在，是修改key对应的value
如果key在字典里面不存在，会往字典写入一个新的key-value
'''
person['name'] = 'lisi'
person['gender'] = 'female'
print(person)
