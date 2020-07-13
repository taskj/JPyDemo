import getopt
import sys

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
    if(len(sys.argv) == 7):
        opts, args = getopt.getopt(sys.argv[1:], "u:t:d:")
        for k,v in opts:
            if k == "-u":
                url = v
            elif k == "-t":
                threads = v
            elif k == "-d":
                dic = v
        print("url:" + url)
        print("threads:" + threads)
        print("dic:" + dic)
    else:
        print("Error Argument !")
        sys.exit()

if __name__ == '__main__':
    init()