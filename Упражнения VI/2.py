class Adder:
    def __init__(self, data = 0):
        self.data = data
    def add(self, x):        
        print(f'{self.data} + {x} = ', end = '')
        self.data += x
        return self.data
    def __add__(self, x):
        return self.add(x)

class ListAdder(Adder):
    def __init__(self, data =[]):
        self.data = data
        
    def add(self, y):
        print(f'{self.data} + {y} = ', end = '')
        self.data += (list(y))
        return self.data

class DictAdder(Adder):
    def __init__(self, data ={}):
        self.data = data
    
    def add(self, y):
        print(f'{self.data} + {y} = ', end = '')
        for key in y:
            if key in self.data.keys():
                new_one = []
                new_one.append(self.data[key])
                new_one.append(y[key])
                self.data[key] = new_one
            else: self.data[key] = y[key]
        return self.data


def selftest():
    print('\t**** Start SELFTEST ****\n')
    print('*** Adder ***')
    z1 = Adder()
    z2 = Adder(2)
    s2 = 2
    print(z1.add(s2))
    print(z1 + 22)
    print()
    
    print('*** ListAdder ***')
    y = ListAdder()
    print(y.data)
    l2 = [5,6,7]
    print(y.add(l2))
    print(y + l2)
    print()

    print('*** DictAdder ***')    
    x = DictAdder()
    d1 = {'a':1, 'b':2}
    d2 = {'b':3, 'c':4}
    print(x.add(d1))
    print(x + d2)
    
if __name__ == '__main__':
    selftest()
