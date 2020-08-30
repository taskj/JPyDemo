# + : 可以用来拼接，用于字符串、元组、列表
print('hello' + 'world') #helloworld
print(('good','yes') + ('hi','ok')) #('good', 'yes', 'hi', 'ok')
print([1,2,3] + [4,5,6]) #[1, 2, 3, 4, 5, 6]

# - : 只能用于集合，求差集
print({1,2,3} - {3}) #{1, 2}

# * : 用于字符串、元组、列表，表示重复多次，不能用于字典和集合
print('hello'*3) #hellohellohello
print([1,2,3]*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
print((1,2,3)*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)

# in: 成员预算符号
print('a' in 'abc') #True
print(1 in [1,2,3]) #True
print(4 in (6,4,5)) #True

#in 用于字典是判断key是否存在的
print('zhangsan' in {'name':'zhangsan','age':14,'score':98}) #False
print('name' in {'name':'zhangsan','age':14,'score':98}) #True
print(3 in {3,4,5}) #True

nums = [19,82,39,12,34,58]
#带下标的遍历
en = enumerate(nums)
for i,e in en:
    print(i,e)
'''
0 19
1 82
2 39
3 12
4 34
5 58
'''

