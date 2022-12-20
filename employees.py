class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
    def giveRise(self, percent):
        self.salary *= (1+percent)
    def work(self):
        print(self.name, 'does stuff')
    def __repr__(self):
        return '<Employee: name = %s, salary = %s>'%(self.name, self.salary)

class Cheff(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, 'make food')

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, 'interfaces with customer')

class PizzaRobot(Cheff):
    def __init__(self, name):
        Cheff.__init__(self, name)
    def work(self):
        print(self.name, 'makes pizza')

# selftesting
if __name__ == '__main__':
    bob =PizzaRobot('Bob')
    print(bob)
    bob.work()
    bob.giveRise(.2)
    print(bob); print()
    for klass in Employee, Cheff, Server, PizzaRobot:
        obj = klass(klass.__name__.upper())
        obj.work()
    
    
        
        
        
        
        
