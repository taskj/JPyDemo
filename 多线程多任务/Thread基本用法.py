import time
import threading

def sing():
    for i in range(5):
        print("正在唱：一路向北...")
        time.sleep(1)

def dance():
    for i in range(5):
        print("正在跳舞...")
        time.sleep(1)

#没有使用多任务完成的程序
#def main():
#    sing()
#    dance()

#使用多任务完成程序
def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()