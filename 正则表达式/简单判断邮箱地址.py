import re

def main():
    #如果要匹配普通的. ? 的字符，使用\转义
    ret = re.match(r"([a-zA-Z0-9_]{4,20})@(163|126)\.com$","laowang@126.com")
    print(ret.group(1))


if __name__ == '__main__':
    main()