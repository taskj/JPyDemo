import time

def cal_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时',end-start)
    return inner()

@cal_time #第一事件调用cal_time，第二事件把被装饰的函数传递给fn
def demo():
    x = 0
    for i in range(1,1000000):
        x += i
    print(x)

@cal_time
def foo():
    print('hello')
    time.sleep(3)
    print('world')


#第三件事：当再次调用demo函数时，demo函数已经不是上面的demo了，现在的demo已经指向了cal_time()中的inner()
print('装饰后的demo={}'.format(demo))
