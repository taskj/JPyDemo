import re

def main():
    html_str =  "<h1>这是一个标题</h1>"
    ret = re.match(r"<\w*>.*</\w*>",html_str)
    ret = re.match(r"<(\w*)>.*</\1>", html_str)

    html_str = "<body><h1>测试分组</h1></body>"
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", html_str)
    #分组起名 起名 ?P<p1> 取名 (?P=p1)
    ret = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", html_str)
    print(ret.group())
if __name__ == '__main__':
    main()
