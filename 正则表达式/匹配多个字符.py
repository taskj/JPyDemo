import re

# \d{1,3}匹配1-3位的数字
ret = re.match(r"速度与激情\d{1,3}","速度与激情34")

#\d{11}匹配必须11位数字
ret = re.match(r"\d{11}","13888888888")

# ? 前面的字符可有可无，02112345678 一样可以匹配成功
ret = re.match(r"021-?\d{8}","021-12345678")

# 验证电话号码，区号3或4位，电话号码，7或8位
ret = re.match(r"\d{3,4}-?\d{7,8}","0898-3230212")

html_content = "asdsadasds\nasdasd"

# .匹配任意一个字符 \n除外
ret = re.match(r".*",html_content)

# re.s 匹配 \n
ret = re.match(r".*",html_content,re.S)

# +必须出现一次，如为空则报错
ret = re.match(r".+","")


print(ret.group())
