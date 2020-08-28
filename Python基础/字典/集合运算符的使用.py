first = {'李白','白居易','李清照','杜甫','王昌龄','王维','孟浩然','王安石'}
second = {'李商隐','杜甫','李白','白居易','岑参','王昌龄'}
third = {'李清照','刘禹锡','岑参','王昌龄','苏轼','王维','李白'}

'''
set 支持多数运算符
'''
print(first - second) #求 a-b 的差集
print(first & second) #求 a和b 的交集
print(first | second) #求 a和b 的并集
print(first ^ second) #求 a和b差集的并集