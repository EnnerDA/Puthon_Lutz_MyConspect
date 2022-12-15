class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s$]'%(self.name, self.pay)
    #def __str__(self):
        #return '*'*20 + f'\nName: {self.name.split()[0]} \nLast name: {self.name.split()[1]} \n'+ '*'*20

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay) #job заполняется автоматически
    def giveRaise(self, percent, bonus = .1):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    # Код самотеста
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.1)
    print(sue)
    print(bob)
    # Создаём Manager
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.1)
    print(tom.lastName())
    print(tom)
    print('--All three--')
    for obj in (bob, sue, tom): # Полиморфизм
        obj.giveRaise(0.1)
        print(obj)

    
    
 
    
