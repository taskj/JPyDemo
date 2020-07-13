import requests

def init():
    pass

#基本http请求，post请求同理

#无参数的get请求
def no_args_get():
    url = "https://www.baidu.com"
    r = requests.get(url=url)
    print(r.content)

#带参数的get请求
def args_get():
    url = "https://www.taskj.cn"
    payload = {'s':'ubuntu'}
    r = requests.get(url=url,params=payload)
    print(r.content)

#http响应
def res():
    url = "https://www.baidu.com"
    r = requests.get(url=url)
    print(r.status_code) #获取http响应状态码
    print(r.headers) #获取http响应头
    print(r.text) #获取http响应文本
    print(r.request.headers) #获取http请求头
    print(r.url) #获取http url

#使用代理服务器请求
def proxy():
    url = "https://www.baidu.com"
    proxise = {'http':'http://192.168.100.9:8080',
               'https':'https://192.168.9:8080'
    }
    r = requests.get(url=url,proxise=proxy(),verify=False)
    print(r.status_code)


#session会话
def session():
    url = "https://www.baidu.com"
    s = requests.Session()
    r = s.get(url)
    print(r.cookies)
    print(r.request.headers)

if __name__ == '__main__':
    init()