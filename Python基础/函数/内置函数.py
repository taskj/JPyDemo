
'''
可迭代对象的方法
'''
'''
any,只要有一个元素转换成布尔值都是True,结果都是True,否则是False
all,如果所有的元素转换成布尔值都是True,结果是True,否则是False
'''
print(any(['hello','','yes']))
print(any(['',0]))


nums = [1,2,3]
print(dir(nums)) #列出对象所有的属性和方法


shang,yushu = divmod(15,2)
print(str(shang)+"&"+str(yushu))