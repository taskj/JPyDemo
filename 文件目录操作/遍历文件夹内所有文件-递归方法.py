import os

#获取示例递归文件夹路径
recPath = os.path.abspath('recursion')

allFile = []
allPath = []
def getAllFiles(path):
    #遍历该目录下的所有文件夹和文件
    for file in os.listdir(path):
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            allPath.append(filepath)
            getAllFiles(filepath)
        else:
            allFile.append(filepath)

if __name__ == '__main__':
    getAllFiles(recPath)
    #输出文件夹的内所有文件
    for file in allFile:
        print(file)