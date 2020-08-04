'''
在考虑H（Hypothsis）和D（Data）情况下，贝叶斯定理的表达式可以写成：
P(H|D)=P(H)P(D|H)/P(D)
'''
class Bayes:
    '''
    prob 概率
    hypothis 猜想
    '''
    def __init__(self):
        self._container = dict()

    def Set(self,hypothsis,prob):
        self._container[hypothsis] = prob

    def Mult(self,hypothsis,prob):
        old_prob = self._container[hypothsis]
        self._container[hypothsis] = old_prob * prob

    def Normalize(self):
        count = 0
        for hypothsis in self._container.values():
            count = count + hypothsis
        for hypothsis,prob in self._container.items():
            self._container[hypothsis] = self._container[hypothsis]/count

    def Prob(self,hypothsis):
        Prob = self._container[hypothsis]
        return Prob


'''
曲奇饼案例
假设有两碗曲奇饼，碗A包含30个香草曲奇饼和10个巧克力曲奇饼，碗B这两种曲奇饼各20个。 
现在假设你在不看的情况下随机地挑一个碗拿一块饼，得到了一块香草曲奇饼。
问题：从碗A渠道香草曲奇饼的概率是多少
'''
def cookieCal():
    bayes = Bayes()
    #先验概率
    bayes.Set('Bow_A',0.5) #P(碗A) = 1/2
    bayes.Set('Bow_B',0.5) #P(碗B) = 1/2
    #后验概率
    bayes.Mult('Bow_A',0.75) #P(香草饼|碗A) = 3/4
    bayes.Mult('Bow_B',0.5) #(香草饼|碗B) = 1/2
    bayes.Normalize()
    prob = bayes.Prob('Bow_A')
    print('从碗A渠道香草饼曲奇的概率:{}'.format(prob))

if __name__ == '__main__':
    cookieCal()

