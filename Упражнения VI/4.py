class Attrs:
    a1 = 1
    a2 = 'spam'
    
    def __init__(self, num):        
        self.a3 = num
        self.name = 'self'
    def __getattr__(self, attr):
        
        print(f'Какой нахуй {attr}? Нет такого атрибута в {self.name} . Иди на хуй!')                

    def __setattr__(self, attr, val):        
        if attr == 'a3':
            print(f'ok a3 = {val}')
            self.__dict__['a3'] = val
        elif attr == 'name':
            self.__dict__['name'] = val            
        else:
            print(f'Do you wand to do {self.name}.{attr} = {val}?')
            print(f'{self.name}.{attr} = ИДИ НА ХУЙ')            
    def __str__(self):
        return f'''
The {self.name} is the {self.__class__.__name__} instance:
a1 = {self.a1}
a2 = {self.a2}
num = {self.a3}
'''
    def my_name(self):
        for k,v in globals().items():
            if v == self:
                self.name = k

        
if __name__ == '__main__':
    x = Attrs(21)
    x.my_name()
    print(x)
    print(x.a1)
    x.a1 = 123123
    x.b =123123
    print(x)
    
