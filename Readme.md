**ТОМ 2**
# Часть VI. Классы и объектно-ориентированное програмирование.


**!!! Поиск атрибута в дереве объектов и к специальный первый аргументу в функциях !!!**


## Глава 26. Объектно-ориентированное програмирование общая картина. 

*Классы* - фабрики экземпляров. Атрибуты классов (данные и функции) обеспечивают поведение, которое наследуется всеми экземплярами .
*Экземпляры* - конкретные элементы в предметной области программы. 

![Дерево наследования классов](https://user-images.githubusercontent.com/116806816/207288621-7e372368-d9cd-4485-a3f2-35200fd6596c.png)
```python
class C2: ...         # Создание объектов классов
class C3: ...         # Создание объектов классов
class C1(С2, С3):     # Связывание с его суперклассами (порядок важен!)
    def __init__(self, who):
        self.name = who

I1 = C1('bob')             # Создание объектов эксземпляров
I2 = C1('sue')             # Связывание с его классом
```
Каждый раз когда экземпляр генерируется из класса, Python автоматически вызвает метод `__init__`. Новый экземпляр передается в аргументе `self` метода `__init__`, а значеия перечисленные в круглых скобка при обращении к классу передаються второму и последующим аргументам. 

*Фреимворки* - наборы суперклассов.

## Глава 27. Основы написания классов.

*Метод* - функция внутри класса.

```python
>>> class FirstClass:          # создали класс
	def setdata(self, value):  #создали методы 
		self.data = value
	def display(self):
		print(self.data)

>>> x = FirstClass()      # создали экземпляр
>>> y = FirstClass()
>>> x.setdata('King')     #применили наследованый метод для создания атрибута
>>> y.setdata(3.14159)
>>> x.display()
King
>>> y.display()
3.14159
>>> x.newdata = 'Artur'  # создали атрибут вручную
# Наследование. Подклассы Суперклассы. 
>>> class SecondClass(FirstClass): # создали подкласс из супер класса
	def display(self):             # переопределили (перегрузили) наследованный метод для подкласса 
		print('Current value="%s"'%self.data)

>>> z = SecondClass() # создали экземпляр
>>> z.setdata(42)     # применили метод наследованный от суперкласса
>>> z.display()       # применили свой перегруженый метод
Current value="42"

# Перегрузка и __init__
>>> class ThirdClass(SecondClass): # создаём новый подкласс
	def __init__(self, value):     # конструктор вызывается при создании нового экземпляра
		self.data = value
	def __add__(self, other):      # перегружает операцию "+"
		return ThirdClass(self.data + other) # за счет вызова ThirdClass(...) создаёт новый 
                                             # экземпляр а не меняет текущий
	def __str__(self):             # перегружает оперцию str(), print()
		return '[ThirdClass: %s'%self.data
	def mul(self, other):          # изменение на месте
		self.data *= other
		
>>> a = ThirdClass('abc')
>>> a.display()
Current value="abc"
>>> print(a)
[ThirdClass: abc
>>> b = a + 'xyz'   # __add__ создаёт новый экземплляр, а не меняет текущий на месте
>>> b.display()     # имеет все методы класса ThirdClass 
Current value="abcxyz"
>>> a.mul(3)        # меняет текущий на месте в отличае от __add__
>>> print(a)
[ThirdClass: abcabcabc
```
Если опустить метод перегрузки операции и не наследовать его от суперкласса, тогда соответствующая операция для экземпляров поддерживаться не будет.

Метод `.__bases__` для определения суперкласса
```python
ThirdClass.__bases__
(<class '__main__.SecondClass'>,)
```
Метод `__dict__` для получения перечня атрибутов
```python
[name for name in FirstClass.__dict__ if name[:2]!='__']
['setdata', 'display']
```
Метод `__class__` для определения к какому классу принадлежит экземпляр
```python
x.__class__
<class '__main__.FirstClass'>
```
Присваиваем стороннюю функцию как атрибут модуля
```python
>>> class A: pass
>>> A.name = 'aaa'
>>> b = A()
>>> b.name
'aaa'
>>> def nameupper(obj): return obj.name.upper()
>>> nameupper(b)
'AAA'
>>> b.name
'aaa'
>>> A.nameupper = nameupper
>>> b.nameupper()
'AAA'
```
## Глава 28. Более реалистичный пример.

Итак, мы планируем реализовать два класса:
* Person — класс, который создает и обрабатывает сведения о людях;
* Manager — настроенная версия класса Person, которая модифицирует унаследованное поведение.

[person.py](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/person.py)

Название классов принято писать с большой буквы а модулей и функций с маленькой. Это Важно!

Вывод объекта (`print`) отображает то, что возвращается методом `__ str__` или `__герг__`. Перегрузим их:
```python
def __repr__(self):
    return '[Person: %s, %s]'%(self.name, self.pay)
```
Разница между `__repr__` и `__str__`: 
```python
def __repr__(self):
    return '[Person: %s, %s$]'%(self.name, self.pay)
def __str__(self):
    return '*'*20 + f'\nName: {self.name.split()[0]} \nLast name: {self.name.split()[1]}\n' + '*'*20
# перехожим в интерактивный режим
>>> print(bob) # вызывает __str__
********************
Name: Bob 
Last name: Smith 
********************
>>> bob       # вызывает __repr__
[Person: Bob Smith, 0$]
```
**Расширение методов**
Создаём подкласс `Manager` класса `Person` что бы переобпределить метод `giveRise`
```python
class Manager(Person):
    def giveRise(self, percent, bonus = .1):
        self.pay = int(self.pay * (1 + percent + bonus)) # скопировали вставили из Person
                                                         # плохой метод не копируйте это хуево
    def giveRise(self, percent, bonus = .1):
        Person.giveRise(self, percent + bonus) # сослались на родительский метод и дополнили его
                                               # хороший метод
```
Тут работает схема **`экземпляр.метод(аргументы) = класс.метод(экземпляр, аргументы)`**

А теперь то же но через `__getattr__` называют делегированием
[person-composite.py](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/person-composite.py)

Более явное и осязаемое внедрение. Применяется и наследование и композиция.
[person-department.py](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/person-department.py)

А какие атрибуты у класса на основе которого получен экземпляр `z`
```python
[key for key in z.__class__.__base__.__dict__ if key[:2] != '__']
```
ну или так:
```
>>> tom.__dict__.keys() # атрибуты только экземпляра
dict_keys(['name', 'job', 'pay'])
>>> dir(tom) # плюс унаследованные атрибуты в классах
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'giveRaise', 'job', 'lastName', 'name', 'pay']
```
Чуть побаловался с выводом
```python
def __repr__(self):
    res = ''
    for key in self.__dict__.keys():
        res += key + ' = ' + str(self.__dict__[key]) + ', '            
    return '[%s: %s]'%(self.__class__.__name__, res[:-2]) 
```

**Модули `pickle`, `dbm` и `shelve`**

Создаём базу данных на `shelve`
```python
from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 100000)
tom = Manager('Tom Jones', 50000)

import shelve

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()
```
Просмотр сохраненного
```python
>>> import glob
>>> glob.glob('person*')
['person-composite.py', 'person-department.py', 'person.py', 'person2.py', 'persondb.bak', 'persondb.dat', 'persondb.dir']
>>> print(open('persondb.dir').read())
'Bob Smith', (0, 81)
'Sue Jones', (512, 93)
'Tom Jones', (1024, 92)
```
```python
>>> db = shelve.open('persondb')
>>> len(db)
3
>>> list(db)
['Bob Smith', 'Sue Jones', 'Tom Jones']
>>> bob = db['Bob Smith']
>>> bob.lastName()
'Smith'
>>> for key in db:
	print(key, '=>', db[key])
	
Bob Smith => [Person: job = None, name = Bob Smith, pay = 0]
Sue Jones => [Person: job = dev, name = Sue Jones, pay = 100000]
Tom Jones => [Manager: job = mgr, name = Tom Jones, pay = 50000]
```
**Обновление объектов в хранилище `shelve`**
```python
import shelve

db = shelve.open('persondb')
for key in sorted(db):
    print(key, '=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.1)
db['Sue Jones'] = sue
db.close()
```
И хоть из командной строки меняй

![изображение](https://user-images.githubusercontent.com/116806816/207864466-56ec5d84-96c7-444a-b6ec-44408900a32a.png)

## Глава 29. Детали реализации классов.

