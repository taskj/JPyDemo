import random

#一个学校，有三个办公室，现在有10位老师等待工位的分配，请编写程序，完成随机分配
teachers = ['A','B','C','D','E','F','G','H','I','J']
rooms = [[],[],[]]

for teacher in teachers:
    room = random.choice(rooms) #choice从列表里面选择一个数据
    room.append(teacher)

print(rooms)