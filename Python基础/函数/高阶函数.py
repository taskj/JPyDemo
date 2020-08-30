'''
一个函数作为另外一个函数的返回值
一个函数作为另外一个函数的参数
函数内部再定义一个函数
'''


def foo():
    print("我是foo，我被调用了")
    return 'foo'

def bar():
    print("我是bar，我被调用了")
    return 'bar'

x = bar()
print('x的值是{}'.format(x))

def outer():
    m = 100
    def inner():
        n = 90
        print('我是inner函数')
    print('我是outer函数')
    return inner

outer()() #我是outer函数,我是inner函数
