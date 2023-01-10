# 1. возник в теме декораторов на стр.273 второго тома.
**Никак не могу понять пример:**
```python
def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print(f'call {oncall.calls} to {func.__name__}')
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer #эквивалент spam = tracer(spam)
    def spam(self, a,b,c): return a+b+c

x = C()
print(x.spam(1,2,3))
print(x.spam('a', 'b', 'c'))

#вывод
call 1 to spam
6
call 2 to spam
abc
```
Но я никак не догоняю почему? Во втором случае когда мы вызываем `print(x.spam('a', 'b', 'c'))` мы же запускаем функцию `tracer` в её теле каждый раз должна выполняться строчка `oncall.calls = 0`. То есть она же каждый раз должна обнулять счетчик.

**Возможно ответ**

При первом вызове `tracer` мы просто запоминаем функцию. создаем в ней метод `oncall` затем после создания метода добавляем в него атрибут `oncall.calls = 0`. Важно что эта строчка стоит ниже создания функции. Последующие вызовы вызывают не `tracer` а именно `oncall`.

Вот конструкция без лишнего дерьма:
```python
def f1(func):
    def f2(*args):
        f2.i += 1
        print(f2.i)
        return func(*args)
    f2.i = 0    
    return f2

a = lambda x: x**2 # a - some func
b = f1(a) 
# вывод
>>> b(2)
1
4
>>> b(3)
2
9
>>> b(4)
3
16
```
То есть мы каждый раз вызывая функции через `f1` на самом деле  выполняем всё ту же функцию которую передаём в аргумент `f1` но с дополнительным уровенм логики которая перечислена в теле `f1`.
