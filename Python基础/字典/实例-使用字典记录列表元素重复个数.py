chars = ['a','c','x','d','p','a','p','a','c']
#{'a':3,'c':2,'x':1,'d':1,'p':2}
char_count = {}

for char in chars:
    if char in char_count:
        print('字典里面已经有这个字符%s' % char)
        char_count[char] += 1
    else:
        print('字典里面没有这个字符%s' % char)
        char_count[char] = 1

print(char_count)