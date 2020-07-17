import random

class Person():
    def eat(self):
        print("吃什么都行")

class Chinese(Person):
    def eat(self):
        print("我想吃米饭")

class Japanese(Person):
    def eat(self):
        print("我想吃寿司")

class American(Person):
    def eat(self):
        print("我想吃汉堡")

class Lunch:

    def get_one_person(self):
        num01 = random.randint(1,3)
        if num01 == 1: return Chinese()
        if num01 == 2: return Japanese()
        if num01 == 3: return American()


    #===使用多态===
    def goto_lunch(self,person:Person):
        person.eat()

    #===不使用多态===
    def lunch_with_chinese(self,person:Chinese):
        person.eat()

    def lunch_with_janpanese(self,person:Japanese):
        person.eat()

    def lunch_with_american(self,person:American):
        person.eat()


if __name__ == '__main__':
    #随机产生一个人
    lunch = Lunch()
    zhangsan = lunch.get_one_person()

    #使用多态，直接调用
    lunch.goto_lunch(zhangsan)

    #===没有使用多台，判断是什么人===
    # if isinstance(zhangsan,Chinese):
    #     lunch.lunch_with_chinese(zhangsan)
    # if isinstance(zhangsan,Japanese):
    #     lunch.lunch_with_janpanese(zhangsan)
    # if isinstance(zhangsan,American):
    #     lunch.lunch_with_american(zhangsan)
