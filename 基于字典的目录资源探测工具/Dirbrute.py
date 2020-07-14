import getopt
import sys
import math

def init():
    start()

def banner():
    print("*"*50)
    print("taskj字典暴力破解器 V1.0"+"")
    print("*"*50)
    print("本工具仅供测试学习！！！")

def usage():
    print("这是工具的使用方法")
    print("python Dirbrute.py -u -url -t -thread -d dictionary")

def start():
    #接收传递过来的参数
    if(len(sys.argv) == 7):
        opts, args = getopt.getopt(sys.argv[1:], "u:t:d:")
        for k,v in opts:
            if k == "-u":
                url = v
            elif k == "-t":
                threads = v
            elif k == "-d":
                dic = v
        multi_scan(url,threads,dic)
    else:
        print("Error Argument !")
        sys.exit()

'''
@url
@threads
@dic 字典文件路径
'''
def multi_scan(url,threads,dic):
    #第一步读取字典文件
    #第二部确定读取的行数
    #第三部制作每一个线程读取的字典列表[[t1],[t2],[t3]]
    with open("dic.txt","r") as f:
        dic_lists = f.readlines()
        thread_line_num = math.ceil(len(dic_lists) / int(threads)) #向上取整线程数
        i = 0
        for line in dic_lists:
            i = i + 1
            




if __name__ == '__main__':
    init()