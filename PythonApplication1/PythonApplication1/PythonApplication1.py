#-*- coding: cp949 -*-

class MyClass:
    age=17
    job='student'
    
    @classmethod
    def t(cls):
        print(cls.age)
   
    def __init__(self, M, D):
        self.birthday=(M, D)
        
    def app(self, a):
        self.p=a
        
    def __repr__(self):
        return 'toilet'
        
K=MyClass(3, 14)
print(f"K's age is {K.age}, and K's job is {K.job}")
print(f"K's birthday is {K.birthday[0]}.{K.birthday[1]}")
K.app(K)
print(K.p)
#When there is a function, bracket necessarily!!
K.t()