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
[финальная версия person.py](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/person2.py)

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

Помни, классы это поиск атрибутов в дереве объектов с учетом иерархии. Ну и особый первй аргумент, конечно же, но сейчас не о нем.
``` python
>>>class A:     # создаём класс
    a1 = 'spam' # с атрибутом
>>>class B(A):  # подкласс
    b1 = 'eggs' # со своим атрибутом
 >>>b=B()       # экземпляр подкласса
 >>>b.a1        # наследует атрибут суперкласса
'spam'
>>> A.c1 = 'ham' # тепрь присваиваем новый атрибут суперклассу 
>>> b.c1         # экземпляр подкласса без проблем находит его в дереве объектов
'ham'
>>> b.d1 = 'prum' # тепрь присваиваем новый атрибут экземпляру подкласса
>>> A.d1 = 123    # и новый атрибут суперклассу с тем же именем
>>> b.d1         # по иерархии присвоенный экземпляру атрибут находится раньше чем то что присвоенно в суперклассе
'prum'
>>> B.d1        # а от подкласс будет наследовать от суперкласса, ибо присвоение атрибуту случилось за его пределами
123
```
**Методики связывания классов**
```python
class Super:
    def method(self):
        print('in Super.method')
    def deligate(self):
        self.action()

class Inheritor(Super): pass

class Replacer(Super):
    def method(self): # полностью переопределяем метод суперкласса
        print('in Replaicer.method')

class Extender(Super):
    def method(self): # дополняем метод суперкласса
        print('Original Extender.method start')
        Super.method(self) # с явным вызовом
        print('Original Extender.method end')

class Provider(Super):
    def action(self): # почти круто!!!
        print('in Provider.action')

# Самотест
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n'+'*'*5, klass.__name__,'*'*5,)
        klass().method() # после класса (), почему не понял, но без них не работает
    print('\n'+'*'*5, 'Provider')
    x = Provider()
    x.deligate() #а вот теперь true круто!!!
```
Super - *асбтрактный суперкласс* для Provider. Т.е. он ожидает от своих подклассов предоставления частей своего поведения.

Для определения дерева классов
```pyhon
class C(A,B): pass
>>> C.__base__
<class '__main__.A'>
>>> C.__bases__
(<class '__main__.A'>, <class '__main__.B'>)
>>> b = B()
>>> b.__class__
<class '__main__.B'>
>>> b.__class__.__name__
'B'
```
## Глава 30. Перегрузка операций.
 Специфическая возможность при создании класса заменить или определить поведение стандарнтых инструметов типа сложения, выитания, индексации и итераций.
 
 ![изображение](https://user-images.githubusercontent.com/116806816/208588711-6cd9a4da-79eb-4454-81a5-f24432bffc9c.png)
 
## Глава 31. Проектирование с использованием классов.

**Композиция в ООП**

[employees.py](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/employees.py)
[pizzashop.py](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/pizzashop.py)

Классы могут представлять почти любые объекты и отношения, которые удастся выразить с помощью предложения; просто замените имена существительные классами (скажем, Oven), а глаголы методами (например, bake), и вы получите первое приближение к проектному решению.	

Применение `pickle` для сохранения экземпляров 
```python
from pizzashop import PizzaShop
shop = PizzaShop()

import pickle
pickle.dump(shop, open('shopfile.pkl', 'wb'))
```
Сохранили объект!
```python
import pickle
obj = pickle.load(open('shopfile.pkl', 'rb'))
print(obj.server, obj.chef)
```
Выгрузили объект. Шик! Всё работает!

Просто дополнили целевой интерфейс объекта
```python
class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)
```
Если снабдить имя атрибута двумя подчеркиваниями, то имена автоматически расширяться именем класса.
```python
>>> class A:
	__a = 11
>>> a = A()
>>> a._A__a
11
```
Такой метод позволяет избежать конфликта имен в объемных проектах.

Можно так же псевдозакрыть и методы.
```python
>>> class A:
	def __meth1(self):
		self.a = 11
>>> a = A()
>>> a._A__meth1()
>>> a.a
11
```
**Фабрики объектов**
```python
def fabric(aClass, *pargs, **kargs):
    return aClass(*pargs, **kargs)

class A:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def __str__(self):
        for k, v in globals().items():
            if v is self:
                break
        return f'{k} from {self.__class__.__name__} class: {self.name} {self.lastname}'

class B: pass

a = fabric(A, 'tom', 'york')
b = fabric(B)
c = fabric(str, 123)
print(f'{a}\n{b}\n{c}')
# вывод
a from A class: tom york
<__main__.B object at 0x0000000002F81040>
123
```
**Подмешивание классов** удобно если какую-то функцию нужно распространить в большом объеме. Например мы желаем расширить вывод `__str__` ну и напишем отдельный класс, в котором эта функция выглядит так, как нам надо. А далее наследуем его в нужные нам классы. Теперь все выводят `print` как нам хочеться, вот мы и подмешали класс. Класс!

**MRO**
`__mro__` - возвращает кортеж, порядок поиска в дереве классов. 
```python
>>> A.__mro__
(<class '__main__.A'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```
Используй `dir`, чтобы получить список всех атрибутов — физически присутствующих и унаследованных и затем надо применять либо `getattr` для извлечения их значений из экземпляра. Т.к. `__dict__` не отразить наследованые атрибуты ну и соответсвенно `экземпляр.__dict__[key]` не сработает. Посему `dir` и `getattr`.


**Python, а представляют собой предмет, который лучше всего усваивается с опытом.**

## Глава 32. Расширенные возможности классов.

Типы и классы стали одним целым. В Питухогн 2 было не так. Все классы унаследованы от суперкласса `object`.

Путь поиска при наследовании в ромбовидных схемах выполняется больше в манере сначала в ширину - Python сначала ищет в любых суперклассах справа от только что просмотренного и только потом поднимается к общему суперклассу вверху. Это называется - Method Resolution Order. Уместно вспомнить опять про метод `__mro__`.
```python
class A(): attr =1
class B(A): pass
class C(A): attr = 2
class D(B,C): pass
x = D()
x.attr
2
``` 
Порядок поиска в данном случае x,D,B,C,A цепочка прервется при первой встрече с присвоением `attr`.

Так как `object` суперкласс всего и вся и всё на свете наследует от него, то вот перечень основнымх методов - `dir(object)`. Но по правилам mro object всегда посещается последним, именно по этому образуется ромб.

[mapattrs.py](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/mapattrs.py) Для прослеживания наследования атрибутов.

**`__slots__`**

`__slots__` позволяет ограничить количество атрибутов у экземпляров класса. 
```python 
class A:
    __slots__ = ['age', 'name', 'job']

a = A()
```
тепреь мы экземплярам `А` можем присваивать только атриьуты перечисленные в `__slots__`.
```python
>>> a.age
AttributeError: age
>>> a.age= 40
>>> a.age
40
>>> a.ppp = 12
AttributeError: 'A' object has no attribute 'ppp'
```
____
* **` .__dict__` вернет собственные атрибуты экземпляра, но не `__slots__`**

* **`dir()` вернет также все унаследованные атрибуты и `__slots__`**

*  **` .__slots__` вернет переменные из `__slots__`**

*  **`getattr(obj, name)` извлечет и dict и slot**
____
Слоты наследуются:
```python
>>> class A: __slots__ = ['a']
>>> class B(A): __slots__ = ['b']
>>> b = B()
>>> [atr for atr in dir(b) if atr[:2] != '__']
['a', 'b']
```
В итоге слоты работают чуть быстрее, и вроде полезны для оптимизации памяти, могут ограничить количество атрибутов в экземплярах, но мешают созданию `__dict__`. Лучтц рекомендует их использовать только в крайних случаях.

**Свойства**

Так мы можем изолировать изменение какого-либо атрибута не прибегаю к общей изоляции функциями `__setatrr__` и `__getattr__`.
```python
class A:
	def getage(self):return 40
	def setage(self,value):
		print('set age: %s'%value)
		self._age = value
	age = property(getage, setage, None, None)
>>> x = A()
>>> x.age
40
>>> x.age =42
set age: 42
>>> x.age
40
>>> x._age
42
```
Все присвоения `x.age` уходят в переменную `x._age`. Остальные атрибуты работают как обычно. 

Тоже самое через `getattr` `setattr`:
```python
class B:
	def __getattr__(self, name):
		if name == 'age': return 40
		else: raise AttributeError(name)
	def __setattr__(self, name, value):
		if name == 'age':
			print('set age:', value)
			self.__dict__['_age'] = value
		else: self.__dict__[name] = value
```
**Дескрипторы**

Только пример написан без пояснений как-будто б не понятно
```python
>>> class A:
	def __get__(self, instance, owner): return 40
	def __set__(self, instance, value): instance._age= value
>>> class B: age = A()
	
>>> x = B()
>>> x.age
40
>>> x.age = 42
>>> x._age
42
```
**Статические методы** 

если определить в классе метод как статический то затем его можно вызывать и из экземпляра и из метода не передавая собственно экземпляр или класс.
```python
class A:
    i = 0
    def __init__(self):
        A.i += 1
    def print_i(): print(A.i)
    print_i = staticmethod(print_i)

if __name__ == '__main__':
    a = A()
    b = A()
    a.print_i() # выведет 2
    A.print_i() # выведет 2
```
**Методы класса**

Внимание обратить что в функцию `count` попадает не `self` а класс!
```python
class A:
    i = 0
    def count(cls):
        cls.i += 1
    def __init__(self):
        self.count()
    def print_i(cls, e= '\n'):
        print(cls.i, end = e)
    count = classmethod(count)

class B(A):
    i = 0
    def __init__(self):
        A.__init__(self)

class C(A):
    i = 0
        
if __name__ == '__main__':
    a1, a2 = A(), A()
    b1, b2, b3 = B(), B(), B()
    c1 = C()
    a1.print_i(', '), b1.print_i(', '), c1.print_i()
 
 # вывод
2, 3, 1
```

**Декараторы и метаклассы**

Декоратор записывается в собственной строке перед оператором `def`.Он состоит из `@` и метафункции, т.е. функции которая управляет другой функцией.
```
class C:
	@staticmethod
	def meth():
```
Равносильно:
```python
class C:
	def meth():
	...
	meth = staticmethod
```
Вот такой у нас теперь счетчик
```python
class A:
    i = 0
    def __init__(self):
        A.i += 1
    @staticmethod
    def print_i(e= '\n'):
        print(A.i, end = e)
class B(A):
    i = 0
    def __init__(self):
        B.i += 1
    @staticmethod
    def print_i(e= '\n'):
        print(B.i, end = e)
class C(A):
    i = 0
    @staticmethod
    def print_i(e= '\n'):
        print(C.i, end = e)
        
if __name__ == '__main__':
    a1, a2, a3 = A(), A(), A()
    b1, b2, b3 = B(), B(), B()
    c1 = C()
    a1.print_i(', '), b1.print_i(', '), c1.print_i()
    A.print_i(', '), B.print_i(', '), C.print_i()
# вывод
4, 3, 0
4, 3, 0
```
Напишем декоратор функций, который считает количество обращений к ним
```python
class tracer:
    """декоратор функций, считает сколько раз обращались к функции"""
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args)

@tracer # то же, что и spam = tracer(spam)
def spam(a,b,c):
    return a+b+c
print(spam(1,2,3))
print(spam(4,5,6))  

# вывод
call 1 to spam
6
call 2 to spam
15
```
[**??? вопрос №1**](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/questions.md)

**Функция `super`**

Автор ругается, семантика и вообще вся моторика Python нарушаются от этой вашей `super`. 
Её, говорит, лучше не использовать. Но если уж сильно хочется то лучше это делать если:
1. В случае изменения суперкласса во время выполнения (крайне неявная штука):
```python
class A:
    def a(self): print('A')
class B:
    def a(self): print('B')
class C(A):
    def a(self): super().a()

c = C()
# вывод
>>> c.a()
A
>>> C.__bases__ = (B,) # смена суперкласса прям походу выполнения
>>> c.a()
B
```
Но и в этом случае можно без `super` обойтись.
```python
class C(A):
    def a(self): C.__bases__[0].m(self)
```
2. Кооперативная координация вызовов методов при множественном наследовании.
В случае длинной цепочик наследования, обращение к классам от которых наследуется несколько предков может дублироваться. Если во всейх классах по всей цепочке использовать `super` то все действия пойдут по списку MRO. Без дублирований. 

**Трудности классов**

* Классы, экземпляры, их атрибуты и методы изменяемы, как словари или списки. Будь аккуратен с этим.
* Помни, что при множественом наследовании порядок перечисления суперклассов имеет зеначение, первым атрибуты смотрятся в классах слева. Что бы изолировать атрибут и потомки его не наследовали, в суперклассе его имя можно начать с `__`. Это псевдозакрытие атрибутов.
* Simple is better than complex.

[Упражнение 1](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20VI/1.md)

[Упражнение 2](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20VI/2.py)

[Упражнение 3](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20VI/3.py)

[Упражнение 4](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20VI/4.py)

[Упражнение 7](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20VI/7.py)

[упражнение 9](https://github.com/EnnerDA/Puthon_Lutz_MyConspect/blob/main/%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20VI/9.py)

# Часть VII. исключения и инструменты.
## Глава 33. Основы Исключений

* **`try/except/else`** прерывает и производит востановление после исколючений, инициируемых Python.
* **`try/finaly`** выполняет действие по очистке независимо от того произошло исключение ли нет.
* **`raise`** генерирует исключение вручную в коде.
* **`assert`** генерирует исключение условно в коде.
* **`with/as`** реализует диспетчеры контекстов, что бы это не значило.

Для формирования собственных исключений воспользуемся наследованием от класса *Exception*.
```python
class PidorError(Exception): pass # Пользовательское исключение
raise PidorError
```
Можем расширить:
```python
class PidorError(Exception): # Пользовательское исключение
    def __str__(self): return "I don't have no time for no monkey business"

raise PidorError
```
За это расширение спасибо группе Qween и их песне "Living on My Own"

## Глава 34. Детали обработки исключений.

**`try/except/else/finaly`**
```python
try:
	операторы # Главное действие выполняемое в первую очередь
except ИМЯ_1: 
	операторы # Выполняются если в течение блока try возникло
		  # исключение ИМЯ_1 
except (ИМЯ_2, ИМЯ_3):
	операторы # Выполняются если в течение блока try возникло
		  # любое изх перечисленных исключений (ИМЯ_2 или ИМЯ_3) 
except ИМЯ_4 as переменная:
	операторы # Выполняются если сгенерировалось исключение ИМЯ_4
		  # экземпляр исключения присваивается переменной
except:
	операторы # Выполняются если были сгенерированы все остальные исключения

else:
	операторы # Выполняются если в течение блока try не возникло исключений
```
Например:
```python
try:
    print(1)
    raise PidorError
    print(2)
except PidorError: print(3)
else: print(4)
finally: print(5)
# вывод
1
3
5
```
а если так:
```python
try:
    print(1)
    #raise PidorError
    print(2)
except PidorError: print(3)
else: print(4)
finally: print(5)
# вывод
1
2
4
5
```
Если оставить пустое `except` то оно перехватит вообще все исключения, в том числе и системные по типу ctrl+C для выхода. Это небезопастно лучше писать `except Exeption` так будут перехвачены все исклбчения но выход останеться вохзможным. 

Сообщения об ошибках могут содержать более одного исключения:
```python
try:
    try:
        1/0
    except: badname
except: open('ggggg')
```
Выдаст три исключения: `FileNotFoundError`, `NameError`, `ZeroDivisionError`.

**`assert`** 

`assert test, data` `data` - необязательная часть. Если в результате вычислений `test` получится `False`, тогда Python  генерирует исключение `AssertionError`, с аргументом `data` если она предоставленна.

Если запускать файл из командной строки с флагом -O, то операторы `assert` не учитываются. Например `%py -O proba.py`. Это называется *оптимизированный режим*.

**`with/as`**
```python
with выражение as переменная # as необязательная часть:
    блок-with
```
*выражение* - возвращает объект, поддерживающий протокол управления контекстами.
Например отлично подходит для файлов: не зависимо от о=того сгенерировалось ли исключение в блоке with файл будет закрыт по завершению этого блока.
```python
with open(r'c:\data\proba') as myfile:
    for line in myfile:
        print(line)
```
*Протокол управления контекстами можно формировать самому, для этого при реализации класса надо перегрузить операции `__enter__` и `__exit__`. Об этом лучше в других местах почитать если уж совсем невтерпёж.*

Допускается указывать любое количество диспетчеров контекстов.
```python
with A() as a, B() as b:
    ...some code
```
## Глава 35. Объекты исключений.

Так как исключения основаны на классах, `except` будет отлавливать не только  класс указанный в нем но и все его подклассы. Суперклассы становятся названием категорий, а подклассы специфическими видами исключений.
```python
class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0(): raise General()
def raiser1(): raise Specific1()
def raiser2(): raise Specific2()

import sys
for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:
        print(f'caught: {sys.exc_info()[0:2]}')
```
**Дерево исключений**

`BaseException` самый верхний класс -> 

-> `Exception` суперкласс для большинства исключений кроме событий выхода в систему. Именно от него надо строить пользовательские исключения. 

-> `ArithmeticError` суперкласс для всех численных ошибок. Содержит подклассы: `OvertlowError`, `ZeroDivisionError` и `FloatingPointError` и пр.

-> `LookupError:` суперкласс для ошибок индексирования в последовательностях `IndexError` и `KeyError`.
  
-> и т.д.

## Глава 36. Проектирование с использованием исключений.

Дерево дейсвтий в случае многократного вложения `try` в `try`
```python
try:
    print('Start 1...')
    try:
        print('Start 2...')
        try:
            print('Start 3...')
            print('spam'[6])
        finally: print('Finally 3')
    finally: print('Finally 2')
finally: print('Finally 1')
# вывод
Start 1...
Start 2...
Start 3...
Finally 3
Finally 2
Finally 1
IndexError: string index out of range
```
Опреаторы `finally` выполняться в любом случае, в порядке обратном от их вызова и только после них будет сообщение об исключении.

Типичный подход к тестированию програм:
```python
import sys
log = open('testlog', 'a')
from testapi import moreTests, runNextTests, testName
def testdriver():
    while moreTests():
        try: runNextTest()
	except Exception: 
	    print('FAILED', testName(), sys.exc_info()[:2], file = log)
	else:
	    print('PASSED', testName(), file = log)
testdriver()
```
**sys.exc_info()** - кортеж с тремя значениями (type, value, traceback) текущего исключения:
1. type - класс обрабатываемого исключения
2. value - экземпляр класса исключенияб который был сгенерирован
3. tracerback - объект трассировки.

**Тут многоувжаемый Лутц изволил советов по проектированию с использованием `try` нам напихать**
* Оперции, которые часто терпят неудачу как правило помещают в `try`. Например открытие фалов, обращения к сокетам.
* Дейсвтия по завершению должны быть реализованы в операторах `try/finally` либо `with/as` если поддержиается диспетчер контекста.
* Принимайте решение о степени детализации в операторах `try/except` адекватно. Не стоит помещать каждый чих в `try`. Смелей.
* Избегайте перехвата пустого `except`. Лучше уж `except Exception` взять, а еще лучше быть поконкретнее чем просто `Exception`. 

_______________________________
>*Примите поздравления! На этом ознакомление с основами языка программирования Python завершено.*
>**Марк Лутц Том 2, стр. 391** 	

________________________________

