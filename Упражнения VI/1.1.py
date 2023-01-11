class Adder:
    def __init__(self, data = 0):
        self.data = data
    def add(self, x, y):        
        print('Not Implement')

class ListAdder(Adder):
    def add(self, x, y):
        print(f'{x} + {y} = ', end = '')
        return list(x)+list(y)

class DictAdder(Adder):
    def add(self, x, y):
        print(f'{x} + {y} = ', end = '')
        for key in y:
            if key in x.keys():
                new_one = []
                new_one.append(x[key])
                new_one.append(y[key])
                x[key] = new_one
            else: x[key] = y[key]
        return x


def selftest():
    print('\t**** Start SELFTEST ****\n')
    print('*** Adder ***')
    z = Adder()
    s1 =1
    s2 =2
    z.add(s1, s2)
    print()
    
    print('*** ListAdder ***')
    y = ListAdder()
    l1 = [1,2,3,4]
    l2 = [5,6,7]
    print(y.add(l1,l2))
    print()
    
    print('*** DictAdder ***')    
    x = DictAdder()
    d1 = {'a':1, 'b':2}
    d2 = {'b':3, 'c':4}
    print(x.add(d1,d2))
    
if __name__ == '__main__':
    selftest()
    
