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
