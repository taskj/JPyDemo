import getopt
import sys
import math
import threading
import requests

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
    result_list = [] #最终结果数组
    temp_list = [] #临时数组
    threads_list = [] #多线程列表
    with open("dic.txt","r") as f:
        dic_list = f.readlines()
        #计算每个线程要读取行数的余数
        remainder = len(dic_list) % int(threads)
        #计算出每个临时数组的长度
        if remainder == 0:
            thread_read_line_num = len(dic_list) / int(threads)
        else:
            thread_read_line_num = math.ceil(len(dic_list) / int(threads))

        #计算最后一个临时数组的长度
        remainArr = int(len(dic_list) % thread_read_line_num)
        i = 1
        if remainArr == 0:
            for line in dic_list:
                if i == thread_read_line_num:
                    temp_list.append(line.strip())
                    result_list.append(temp_list)
                    temp_list = []
                    i = 1
                else:
                    temp_list.append(line.strip())
                    i = i + 1
        else:
            for line in dic_list:
                if i == thread_read_line_num:
                    temp_list.append(line.strip())
                    result_list.append(temp_list)
                    temp_list = []
                    i = 1
                else:
                    temp_list.append(line.strip())
                    i = i + 1
            result_list.append(temp_list)


        for i in result_list:
            threads_list.append(threading.Thread(target=scan, args=(url,i)))

def scan(url,dic):
    for line in dic:
        r = requests.get(url + "/" + line)
        if r.status_code == 200:
            print(r.url + ":" + r.status_code)




if __name__ == '__main__':
    init()