class Lunch:
    "Класс контейнера и контролера"
    order_count = 0
    def __init__(self, customer_name, employee_name, foodName):
        "Создаёт экземпляры Customer и Employee"
        Lunch.order_count += 1
        self.order_number = Lunch.order_count
        self.customer = Customer(customer_name, self)
        self.employee = Employee(employee_name, self)
        self.foodName = foodName
        self.order(foodName)
        
    def order(self, foodName):
        "Начинает эмуляцию заказа экземпляром Customer"
        print('*'*23, f'''
\tStart order #{self.order_number}
{self.customer.customer_name} хочет из {self.employee.employee_name}:''')
        for k,v in self.foodName.items():
            print(f' {k.title()} - {v} штук')
        print()
        self.customer.placeOrder(self.employee, foodName)    
    def result(self):
        "Запрашивает у Customer какой экземпляр Food он имеет"
        print(f'Оплата прошла, {self.employee.employee_name}, приступаейте к доставке')
        self.employee.done()
        
class Customer:
    "Покупатель"
    def __init__(self, customer_name, lunch):
        "Инициализирует блюдо значением None"
        self.customer_name = customer_name
        self.lunch = lunch
    def placeOrder(self, employee, foodName,):
        "Размещает заказ с экземпляром Employee"
        employee.takeOrder(foodName)
    def printFood(self):
        "Выводит название блюда"
        pass
    def pay(self, cost):
        print(f' - {self.customer_name}: Ok!  оплатил {cost} $')
        self.lunch.result()
        

class Employee:
    "Продавец"
    def __init__(self, employee_name, lunch):
        self.employee_name = employee_name
        self.lunch = lunch
             
    def takeOrder(self, foodName):
        "Возвращает экземпляр Food с запрошенным названием"
        print(f' - {self.employee_name}: заказ размещен')        
        for k in foodName:
            for i in range(foodName[k]):
                self.food = Food(k)
        self.cost = self.cost_order(self.employee_name, foodName)
        print(f'   с Вас {self.cost} $')
        self.lunch.customer.pay(self.cost)
        
    def cost_order(self, employee_name, foodName):
        if employee_name == 'PizzaHot': menu = {'pizza1' : 15, 'pizza2':20}
        if employee_name == 'HotCat': menu = {'cat1' : 5, 'great_cat':55}
        if employee_name == 'IceCreamBeach': menu = {'ice':7, 'cream':12, 'beach': 24}
        res = 0
        for k,v in foodName.items():
            res += menu[k]*v        
        return res
    def done(self):
        print(f' - {self.employee_name}:')
        print('*'*5, "ВСЁ ГОТОВО!", '*'*5, '\n')
        
class Food:
    "Заказ"
    all_food = {}
    def __init__(self, name):
        "сохраняет название блюда"
        self.name = name
        if name in Food.all_food: Food.all_food[name] += 1
        else: Food.all_food[name] = 1

    @classmethod
    def print_today_food(self):
        print('Всего за сегодня было заказано:')
        for k,v in Food.all_food.items():
            print(f' {k} - {v}шт.')
    

if __name__ == "__main__":
    from random import randint
    employees = ['Bob', 'Albert', 'Mary']
    PizzaHot_menu = {'pizza1' : 15, 'pizza2':20}
    HotCat_menu = {'cat1' : 5, 'great_cat':55}
    IceCreamBeach_menu = {'ice':7, 'cream':12, 'beach': 24}
    customers = {'PizzaHot': PizzaHot_menu, 'HotCat': HotCat_menu , 'IceCreamBeach': IceCreamBeach_menu}
    for i in range(randint(1, 10)):
        e = employees[randint(0, (len(employees) - 1))]
        c = list(customers.keys())[randint(0, (len(customers.keys())-1))]
        o = {}
        for i in range(randint(1,5)):
            o1 = list(customers[c].keys())[randint(0, (len(customers[c].keys())-1))]
            o[o1] = randint(1,3)
        l = Lunch(e,c, o)
    Food.print_today_food()
