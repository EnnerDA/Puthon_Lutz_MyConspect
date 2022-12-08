**Упражнение 1** 
 элементарно

**Упражнение 2**`def adder(x,y): return x+y`

**Упражнение 3** 
```python
def adder(*args):
    res = 0
    for arg in args:
        if not res: res = arg
        else: res += arg
    return res
```
**Упражнение 4**
```python
def adder(good = 1, bad = 10, ugly = 100, **args):
    res = good + bad + ugly
    for val in args:
        res += args[val]
    return res
 
 adder(pep = 1000, kek = 10000)
 ```
 **Упражнение 5**
  ```python
 def copyDict(**args):
    return {key:val for key,val in args.items()}    
  ```
Проверка
  ```python
>>> y = {'a':1, 'b':2}
>>> x = copyDict(**y)
>>> x
{'a': 1, 'b': 2}
>>> y['a']=3
>>> y
{'a': 3, 'b': 2}
>>> x
{'a': 1, 'b': 2}
```
 Номер с `y = x[:]` не пройдет, ведь словари не поддерживают нарезание.
 
 **Упражнение 6**
 ```python
 def addDict(*dicts):
    res = {}
    for user_dict in dicts:
        if not res: res = copyDict(**user_dict)
        else:
            for key in user_dict:
                if key in res: pass
                else: res[key] = user_dict[key]
    return res
 ```
 Проверка
```python
>>> x ={'a': 1, 'b': 2, 'c':3}
>>> y = {'a': 3, 'b': 2, 'd':4}
>>> addDict(x,y)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
**Упражнение 7**
```python
def f1(a, b): print(a, b)
def f2(a, *b): print(a, b)
def f3(a, **b): print(a, b,)
def f4(a, *b, **c): print(a, b, c)
def f5(a, b=2, c=3): print(a, b, c)
def f6(a, b=2, *c): print(a, b, c)

f1(1, 2)
f1(b=2, a =1)
f2(1, 2, 3)
f3(1, x=2, y=3)
f4(1, 2, 3, x=2, y=3)
f5(1)
f5(1, 4)
f6(1)
f6(1, 3, 4)
```
**Упражнение 8**
```python
def factor(y):
    x = y//2
    while x>1:
        if not y%x:
            print(y, 'has factor', x)
            break
        x -=1
    else: print(y, 'is prime')
```
Рефакторнём немножко
```python
def factor2(y):
    res = next((x for x in range(y//2,0,-1) if not y%x))
    if res != 1: print(f'{y} has factor {res}')
    else: print(y, 'is prime')
 ```
**Упражнение 9**
```python
import math
>>> list(map(math.sqrt, [2,4,9,16,25]))
[1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
>>> [math.sqrt(x) for x in [2,4,9,16,25]]
[1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
>>> list(math.sqrt(x) for x in [2,4,9,16,25])
[1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
```
**Упражнение 10**
```python
>>> import sys, math
>>> sys.path.append(r'C:\Users\1\Desktop\Проект\Питухон\Марк Лутц')
>>> from timer import *

>>> bestoftotal(10000,10000, (math.sqrt), 100)
	From total in 10000 reps:
besttime = 0.0017007470000862668, 
bedtime = 0.02317085300001054, 
result = 10.0
>>> bestoftotal(10000,10000, (lambda x: x**0.5), 100)
	From total in 10000 reps:
besttime = 0.003287867999915761, 
bedtime = 0.08048238200012747, 
result = 10.0
>>> bestoftotal(10000,10000,pow, 100, 0.5)
	From total in 10000 reps:
besttime = 0.002729627000007895, 
bedtime = 0.34011286499980997, 
result = 10.0
```
Вывод, если нужен кореньквадратный в невероятно большом количестве, то лучше использовать `sqrt` из модуля `math`.

**Упражнение 11**
```python
>>> def contdown(x):
	if x:
		print(x, end = ' ')
		return contdown(x-1)
	else: print('STOP')

>>> contdown(5)
5 4 3 2 1 STOP
```
Если через генератор, то можно так:
```python
>>> f = lambda x:(i if i else 'stop' for i in range(x,-1,-1))
>>> s = f(10)
>>> list(s)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 'stop']
>>> s = f(5)
>>> for i in s: print(i, end = ' ')
5 4 3 2 1 stop 
```
**Упражнение 12**
```python
from timer import *
from functools import reduce
import math

def fact1(n):
    if n: return n*fact1(n-1)
    else: return 1

def fact2(x):
    return reduce(lambda x,y: x*y, list(range(x,0,-1)))

def fact3(x):
    y = 1
    for i in range(x,0,-1):
        y *= i
    return y

def fact4(x): return math.factorial(x)
```
Замерим:
```python
>>> bestoftotal(1000, 10000, fact1, 10)
besttime = 0.01587743199999636, 
result = 3628800

>>> bestoftotal(1000, 10000, fact2, 10)
besttime = 0.02191875100000118, 
result = 3628800

>>> bestoftotal(1000, 10000, fact3, 10)
besttime = 0.010534739000007676, 
result = 3628800

>>> bestoftotal(1000, 10000, fact4, 10)
besttime = 0.00225055800001428, 
result = 3628800
```

