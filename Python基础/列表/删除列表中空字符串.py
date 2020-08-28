# 删除列表中的空字符串
words = ['hello','good','','','yes','ok','']


'''
在用for...in遍历列表时，最好不要进行增加和删除操作,删掉元素后会漏掉
for word in words:
    if word == '':
        words.remove(word)
print(words)
'''

i = 0
while i < len(words):
    if words[i] == "":
        words.remove(words[i])
        i -= 1
    i += 1
print(words)
