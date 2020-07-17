#Person基类
class Person:
    def __init__(self,name,gender,height,age,mobile,email):
        self.name = name
        self.gender = gender
        self.height = height
        self.age = age
        self.mobile = mobile
        self.email = email

#中国人
class Chinese(Person):
    def __init__(self,name,gender,height,age,mobile,email):
        Person.__init__(self,name,gender,height,age,mobile,email)
    def say(self):
        print("欢迎来到中国")

#日本人
class Japanese(Person):
    def __init__(self,name,gender,height,age,mobile,email):
        Person.__init__(self,name,gender,height,age,mobile,email)
    def say(self):
        print("欢迎来到日本")

#美国人
class American(Person):
    def __init__(self,name,gender,height,age,mobile,email):
        Person.__init__(self,name,gender,height,age,mobile,email)
    def say(self):
        print("欢迎来到美国")


if __name__ == '__main__':
    a = Chinese("张三","男",175,24,"1231314314","888@qq.com")
    a.say()

    b = Japanese("木村拓哉","男",180,44,"3131432","gogogo@qq.com")
    b.say()

    c = American("Trump","男",180,70,"4323424","asdad@gmail.com")
    c.say()