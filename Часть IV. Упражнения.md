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
```def factor(y):
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
    print(f'{y} has factor {res}')
 ```
 
