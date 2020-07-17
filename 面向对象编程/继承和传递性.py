#Person基类
class Person:
    def __init__(self,name,gender,height,age,mobile,email):
        self.name = name
        self.gender = gender
        self.height = height
        self.age = age
        self.mobile = mobile
        self.email = email

    def run(self):
        print("--走路--")

    def eat(self):
        print("--吃饭--")

    def sleep(self):
        print("--睡觉--")

#中国人
class Chinese(Person):
    def __init__(self,name,gender,height,age,mobile,email):
        Person.__init__(self,name,gender,height,age,mobile,email)
    def say(self):
        print("欢迎来到中国")

#由中国人类派生出中国学生类
class ChineseStudent(Chinese):
    def __init__(self,name,gender,height,age,mobile,email):
        Chinese.__init__(self,name,gender,height,age,mobile,email)


if __name__ == '__main__':
    student = ChineseStudent("阿强","女",160,30,"123123131","e131@qq.com")
    #访问父类
    student.say()
    #访问父类的父类
    student.run()
    print(student.name)