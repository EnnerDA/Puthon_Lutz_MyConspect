class Scene:
    @classmethod
    def action(cls):
        customer = Customer()
        clerk = Clerk()
        parrot = Parrot()
        customer.line()
        clerk.line()
        parrot.line()        

class Customer:
    def line(self):
        print('I am Customer')

class Clerk:
    def line(self):
        print('I am Clerk')

class Parrot:
    def line(self):
        print('I am Parrot')

Scene().action()
