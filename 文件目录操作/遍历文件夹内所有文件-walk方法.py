import os

allFile = []
allPath = []

#获取示例递归文件夹路径
recPath = os.path.abspath('recursion')

for root,dir,file in os.walk(recPath):
    for name in file:
        print(os.path.join(root,name))