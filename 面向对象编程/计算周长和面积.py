from abc import *
import math

class Graph(metaclass=ABCMeta):

    #抽象方法求周长
    @abstractmethod
    def get_perimeter(self,len):
        pass
    @abstractmethod
    def get_area(self):
        pass


#派生出等边三角形类
class EquT(Graph):
    def __init__(self,len):
        self.len = len

    #实现抽象方法-周长
    def get_perimeter(self):
        return 3 * self.len

    def get_area(self):
        return 0.5 * self.len * math.sqrt(3) / 2

#派生出等边三角形类
class Square(Graph):
    def __init__(self,len):
        self.len = len

    def get_perimeter(self):
        return 4 * self.len

    def get_area(self):
        return self.len * self.len

#派生出园类
class Cricular(Graph):
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.1415926

    def get_perimeter(self):
        return 4 * self.pi * self.radius

    def get_area(self):
        return 2 * self.pi * self.radius * self.radius

if __name__ == '__main__':
    print("===等边三角形===")
    a = EquT(10)
    print("等边三角形周长为: %2.f" % a.get_perimeter())
    print("等边三角形面积为: %2.f" % a.get_area())
    print("===圆形===")
    b = Cricular(10)
    print("圆形的周长为: %2.f" % b.get_perimeter())
    print("圆形的面积为: %2.f" % b.get_area())
    print("===正方形===")
    c = Square(10)
    print("正方形的周长为: %2.f" % c.get_perimeter())
    print("正方形的面积为: %2.f" % c.get_area())
