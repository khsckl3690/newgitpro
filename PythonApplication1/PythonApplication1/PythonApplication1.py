class MyClass:
    age=17
    job='student'
    
    def __init__(self, M, D):
        self.birthday=(M, D)
        
    def app(self, a):
        self.p=a
        
    def __repr__(self):
        print(self.p)
        
K=MyClass(3, 14)
print(f"K's age is {K.age}, and K's job is {K.job}")
print(f"K's birthday is {K.birthday[0]}.{K.birthday[1]}")
K.app('app')
print(K)