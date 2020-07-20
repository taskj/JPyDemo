import abc

#抽象类，不能被实例化
class Person(metaclass=abc.ABCMeta):

    @abc.abstractmethod #表明下面方法是抽象类
    def eat(self):
        pass

    @abc.abstractmethod
    def sleep(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

if __name__ == '__main__':
    #抽象类不能被实例化
    lisi = Person()
    lisi.run()
