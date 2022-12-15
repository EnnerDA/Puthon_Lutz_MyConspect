from classtools import AttrDisplay

class Person(AttrDisplay):
    """Создаёт и обрабатвает записи о людях"""
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
class Manager(Person):
    """Настроенная версия Person со специальными требованиями"""
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
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

    
    
 
    
