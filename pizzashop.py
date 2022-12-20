from employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, 'orders from', server.name)
    def pay(self, server):
        print(self.name, 'pays for item to', server.name)
        print('\t'+'*'*10 )

class Oven:
    def bake(self):
        print('oven bakes')
        
class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

#selftesting
if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    scene.order('Shaggy')
    
        
