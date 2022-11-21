# Часть I. Начало работы.
## Глава 1. Python в вопросах и ответах.

Питухон - великолепный язык, мы 60 страниц это доказываем.

## Глава 2. Как Python выполняет программы.

Исходный код компилируется в байт-код, который запускается на виртуальной машине Python.

Есть способы ускорить Python разными моделями реализации языка. IronPython, PyPy etc. М
ожно с помощью сторонних средств получить фиксированный двоичный файл.

## Глава 3. Как пользователь выполняет программы.

Вы обязаны инициализировать счетчики нулями, прежде чем сможете увеличивать их, инициализировать списки до их расширения и т.д.; вы не объявляете переменные, но им должны быть присвоены значения до того, как их можно будет извлекать.

*Программа - последовательность готовых операторов, сохраненных в файле для многократного выполнения.*

```
 % py scriptl.py > saveit.txt	
```
если ввести такое в командной строке, то результат выполнения скрипта сохранится в saveit.txt

Перва я строка в файле .py может быть *запускающим модулем.* В первой строке пишется #! подробнее в приложении В тома 2.

```python
>>> import script1
```
привелет к выполнению сценария script1.py , но только однократно. Считается, что импорт затратная операция, дальнейщие вызовы import script1 ничего не делают.
если требуется вызвать модуль заново, то
```python
from imp import reload
reload(module1)
```
Операции импорта обязаны искать файлы, компилировать их в байт-код и выполнять код.

*Модуль* - пакет имен переменным, известный под названием пространство имен, и имена внутри такого пакета называются - *атрибутами*. Т.е. *атрибут* - это имя переменной, которая прикрепляется к специфическому объекту (вроде модуля).

Формально `from` копирует атрибуты модуля, так что они становятся просто переменными на принимающей стороне.

Функция `dir` вызывается с именем импортированного модуля в круглых скобках, она возвращает все атрибуты внутри 	
модуля. Имена с ведущими и завершающими двойными подчеркиваниями (__ X__) являются встроенными именами.
```python
>>> dir(treenames) 
[’__builtins__	', '__ doc__	’_____ file__ ', '__ name__	', '__ package__', ’a’, ’b’, 'c']
```

Вызов встроенной функции `exec(open('module.ру').read())` является приемом запуска файлов без импортирования и последующей перезагрузки.

**!**  `ехес` работает, как если бы вы поместили код на его место, потенциально он способен молча переписать переменные, которые используются в текущий момент.	

*IDLE* - интегрированная среда разработки (integrated development environment — IDE в общеам случае и IDLE в случае стандартной питоновской среды, названой спциально с ошибкой). Графический пользовательский интерфейс, который позволяет редактировать, выполнять, просматривать и отлаживать программы Python, используя единый интерфейс.
IDLE можно запустить из консоли `% py -m idlelib.idle`
 
Для прокрутки ранее написанных команд можно использовать <Alt+P>/<Alt+N>. 

Повторять команды можно также путем перемещения на них курсора с последующим щелчком и нажатием <Enter> для вставки их текста в строку с приглашением.
 
Применяйте отладчик командной строки pdb.

Применяйте аргумент -i команды python	(например, python -i m.py). Когда сценарий закончит работу, либо успешно дойдя до конца, либо из-за возникновения ошибки вы сможете вывести финальные значения переменных, чтобы получить больше деталей.

# Часть II. Типы и операции.
 
## Глава 4. Введение в типы объектов Python.

Концептуальная иерархия Python:
1. Программы состоят из модулей.
2. Модули содержат операторы.
3. Операторы содержат выражения.
4. Выражения создают и обрабатывают объекты.

Обзор встроенных типов объектов:

![Обзор встроенных типов объектов:](https://user-images.githubusercontent.com/116806816/202090225-28e7bae0-31f9-43aa-b9ef-6d8c2479db4f.png)

*Последовательность* - позиционно упорядоченая коллекция других объектов.

Операции эквивалентны:
```python
S = 'spam'
S[-1] == S[len(S)-1]
```
Интересный синтаксис:
```python
>>>S[:-1] #выдать все кроме последнего элемента
'spa'
```
Строка - неизменяемый объект. мы можем построить новый на ее основе но не поменять саму строку:
```python
>>> s = 'spam'
>>> s[0] = z
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s[0] = z
NameError: name 'z' is not defined
>>> s = 'z' + s[1:]
>>> s
'zpam'
```
Кортежи, строки, числа - неизменяемы. Списки, словари, множества - изеняемы.
 
Функция `dir` просто выдает имена методов. Чтобы выяснить, что делает тот или иной метод, его имя можно передать функции `help`:

```python
>>> help(s.index)
Help on built-in function index:

index(...) method of builtins.str instance
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.
```
Можно запрашивать `help` по целым классам, например `help(str)' выдаст описание всех строковых методах.

**Строки**
Операции над строками:
* \+ сложение (конкатенация)
* \* повторение
* [:] нарезание
* [1] индексирование


Для сопоставления с образцом в Python мы используем модуль `re`. Синтаксис его не явный и я нихрена не понял.

**Списки** 

*Списки*  - позиционно упорядоченные коллекции объектов произвольных типов и не имеют фиксированных размеров. Кроме того, они изменяемы — в отличие от строк списки можно модифицировать на месте путем присваивания по смещениям и вызова разнообразных списковых методов.

Операции над списками:
* теже что и для строк +
* добавление объекта в конец списка `spisok.append(new_element)`
* удаление элемента из середины `spisok.pop(2)`, в скобках указан индекс удаляемого элемента.
* del spisok[1], удаляет элемент из списка.
* isnsert, remove, extend и т.д.
* spisok.sort(), spisok.reverse() меняют порядок следования элементов.

Поскольку списки являются зменяемыми, большинство списковых методов также модифицируют объект спискаа месте, а не создают новый такой объект	

Вложения - можно вкладывать в список списки, словари, и любые типы данных на любую глубину.
```python
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
>>> m
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> m[1][0]
4
```
**Списковые включения**
Получать строки легко посредством простой индексации, потому что матрица хранится по строкам, но получить столбец почти так же легко с помощью спискового включения:
```python
>>> col2 = [row[1] for row in m]
>>> col2
[2, 5, 8]
>>> [row[1] + 1 for row in m] # добавить 1 к каждому значению row[1]
[3, 6, 9]
>>> [row[1] for row in m if row[1]%2 == 0] # вернуть только четные значения row[1]
[2, 8]
```
Интересный синтаксис:
```python
>>> list(range(-6,6,2))
[-6, -4, -2, 0, 2, 4]
>>> [[x**2, x**3] for x in range(4)]
[[0, 0], [1, 1], [4, 8], [9, 27]]
>>> [[x, x/2, x*2] for x in range(-6,7,2) if x > 0]
[[2, 1.0, 4], [4, 2.0, 8], [6, 3.0, 12]]
```
```python
>>> list(map(sum, m))
[6, 15, 24]
```
Создание словарей:
```python
{x: ord(x) for x in 'spaam'}
```
функция `ord` возвращает численный код Unicod заданого символа.

**Словари**

*Словари* Python - это *отображения*, коллекции других элемнентов, но объекты храняться по ключам, а не по относительным позициям. Являются изменяемыми.  
```python 
rec = {'name': {'first': 'bob', 'last': 'smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
```
Проверка нахождения ключа в словаре:
```python
if 'name' in rec:
    print('good')
```
Интересный синтаксис:
```python
>>> value = rec['x'] if 'x' in rec else 1 #проверка на вхождение ключа 'x' в словарь rec и ветвление в одной строке
>>> value
1
```
Если требуется навязать порядок в последовательности элементов словаря, то вот вариант:

1. Получаем список ключей методом `keys()`
2. Сортируем этот список методом `sort`
3. Теперь можем пройти все ключи в нужном порядке циклом `for`
```python
>>> ks = list(rec.keys())
>>> ks
['name', 'jobs', 'age']
>>> ks.sort()
>>> ks
['age', 'jobs', 'name']
>>> for key in ks:
        print(key, '=>', rec[key])

age => 40.5
jobs => ['dev', 'mgr']
name => {'first': 'bob', 'last': 'smith'}
```
Тот же результат получим если напишем так:
```python
>>> for key in sorted(rec):
    print(key, '=>', rec[key])
```

**Кортежи**
 
*Кортежи* - неизменяемая последовательность элементов.
```python
>>> t = (1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> t[0] # индексацияб нарезание и т.д.
1
 >>> t.index(4) # возвращает индекс элемента со значением 4
3
>>> t.count(4) # считает количество элементов со значением 4
1
>>> t[0] = 2 # выдаст ошибку, т.к. кортежи не изменяемы!
```

**Файл**
Пример создания
```python
>>> f = open('data.txt', 'w')
>>> f.write('hello\n')
6
>>> f.close()
```
В сценарии содержимое файла всегда будет строкой независимо от типа находящихся в нем данных.
Файлы предлагают итераторы для своего чтения: `for line in open(’data.txt’): print(line)`

Для кодирования и декодирования используем `encode` / `decode`:
```python
>>> text = 'abcdefg'
>>> text.encode('utf-8')
b'abcdefg'
>>> rutext = 'абвгде'
>>> rutext.encode('utf-8')
b'\xd0\xb0\xd0\xb1\xd0\xb2\xd0\xb3\xd0\xb4\xd0\xb5'
>>> crokazyab = b'\xd0\xb0\xd0\xb1\xd0\xb2\xd0\xb3\xd0\xb4\xd0\xb5'
>>> crokazyab.decode('utf-8')
'абвгде'
```

**Прочие типы***

*Множество* - неупорядоченная последовательность уникальных элементов. Задаются функцией `set`.
```python
>>> x = set('spam')
>>> y = {'h', 'a', 'm'}
>>> x,y
({'m', 's', 'a', 'p'}, {'m', 'h', 'a'})
>>> x&y # пересечение
{'m', 'a'}
>>> x|y # объединение
{'h', 'm', 's', 'a', 'p'}
>>> x - y # разность
{'s', 'p'}
>>> x > y # надмножество
False
>>> {n**2 for n in range(4)}
{0, 1, 4, 9}
```

**Классы, определяемые пользователем**

Классы определяют новые типы объектов, которые расширяют основной набор.

## Глава 5. Числовые типы.

![изображение](https://user-images.githubusercontent.com/116806816/202360309-952f14e7-a5a2-4e17-abff-674bb365bf6a.png)

![изображение](https://user-images.githubusercontent.com/116806816/202364052-0a3d73f1-5af9-4b26-a305-eed12b8bab00.png)

Операции, находящиеся ниже в табл. 5.2, имеют более высокий приоритет и потому в смешанных выражениях вычисляются раньше. 	

Операции, расположенные в одной строке табл. 5.2, обычно группируются слева направо, когда они скомбинированы (за исключением возведения в степень, которое группируется справа налево, и сравнений, выстраиваемых в цепочку слева направо).	

Например: x + y * z Python первым выполнит y * z а затем уже сложение.

Применение круглых скобок переопределяет порядок и вообще улучшает читабельность.

```python
>>> 1 == 2 < 3 # тоже, что и 1 == 2 and 2 < 3
False
```
**!!!** Важный пример
```python
>>> 1.1 + 2.2 == 3.3
False
>>> 1.1 + 2.2
3.3000000000000003 # ограниченная точность
```
Причина связана с тем фактом, что числа с плавающей точкой не способны представлять определенные значения точно из-за ограниченного количества битов — фундаментальная проблема в численном программировании, не уникальная для языка Python.	

`//` -  деление с округлением, в меньшую сторону — она усекает результат до ближайшего целого значения, которое меньше подлинного результата. В отрицательных числах результат такой:
```python
>>> -9/4
-2.25
>>> -9//4
-3
```

Если требуется усечение в сторону 0, то лучше прогнать функцию `math.trunc`.
```python
>>> import math
>>> math.trunc(-9/4)
-2
```
**Комплексные числа** записываются 
```python
>>> 2+2j
(2+2j)
```
Отлично обрабатываются стандартным модулем cmath.

Но, надо быть аккуратнее и постараться не называть переменные `j`, мало ли путаницу внесу случайно.

**Не десятичные системы исчисления**
 
* `oct` преобразует десятичное число в восьмеричное 
* `hex` — в шестнадцатеричное
* `bin` — в двоичное	
 
Если вы обнаруживаете, что хотите манипулировать битами в Python, то должны подумать о том, тот ли язык вы используете для реализации программы.
 
 **Дргуие встроенные инструменты**
 
 ```python
>>> import math
>>> math.pi, math.e # классические константы
(3.141592653589793, 2.718281828459045)
>>> math.sin(math.pi/2) # тригонометрические функции
1.0
>>> math.sqrt(144) # квадратный корень
12.0
 >>> abs(-42) # абсолютное значение (модуль)
42
>>> sum((1,8,6,4)) # сумма, работает на последовательности
19
>>> min(3,1,2,4), max(3,1,2,4) # минимум, максимум
(1, 4) 
>>> math.floor(2.567), math.floor(-2.567) # округление в меньшую сторону (до меньшего целого)
(2, -3)
 >>> round(2.467), round(2.567), round(2.567, 2) # нормальное округление
(2, 3, 2.57)
 >>> '%.1f' %2.567, '{0:.2f}'.format(2.567) # округление для отображения
('2.6', '2.57')
```
```python
>>> import random # модуль случайностей
>>> random.random() # случайное число с плавающей точкой от 0 до 1
0.7048912341014086
>>> random.randint(1,10) #  случайное целое число в указаном диапазоне
6
>>> spisok = ['a', 'b', 'c', 'd']
>>> random.choice(spisok) # выбор случайного элемента из списка
'b'
>>> random.shuffle(spisok) # перемещать список
>>> spisok
['b', 'd', 'a', 'c']
 ```
**Другие числовые типы**
 
 **Десятичные**
 
 Из-за вот такой математики могут возникнуть ошибки
 ```python
 >>> 0.1+0.1+0.1-0.3
5.551115123125783e-17
 ```python
>>> from decimal import Decimal
>>> Decimal('0.1') +Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
Decimal('0.0')
 ```
 Однако если использовать float() в качестве аргумента:
 ```python
 Decimal(0.1) +Decimal(0.1)+Decimal(0.1)-Decimal(0.3)
Decimal('2.775557561565156540423631668E-17')
 ```
 Можно установить глобальную точность для десятичных чисел:
```python
>>> import decimal
>>> decimal.getcontext().prec=4
>>> Decimal(0.1) +Decimal(0.1)+Decimal(0.1)-Decimal(0.3)
Decimal('1.110E-17')
```
 не понятно тогда зачем всё это?!

 **Дробный тип**
 
Тип Fraction реализует объект рационального числа. По существу он явно хранит числитель и знаменатель.	
```python
 >>> from fractions import Fraction
>>> x = Fraction(1,3)
>>> x
Fraction(1, 3)
>>> print(x)
1/3
>>> 1 - x
Fraction(2, 3)
```
Можно создавать дробные числа из чисел с плавающей запятой
``` python 
>>> y = Fraction(0.25)
>>> y
Fraction(1, 4)
```
Таким образом можно получить точные математические вычисления, но со снижением скорости и читабельности кода.
 ```python
 >>> 0.1+0.1+0.1-0.3 # стандартная математика
5.551115123125783e-17
>>> 5.551115123125783e-17 == 0
False
# Дробная
>>> Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
Fraction(0, 1)
>>> Fraction(0, 1) == 0
True
# Десятичная
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
>>> Decimal('0.0') == 0
True
```
Еще способ представления в кчестве дроби
 ```python
>>> (4/3).as_integer_ratio()
(6004799503160661, 4503599627370496)
>>> a = Fraction(*(4/3).as_integer_ratio())
>>> a
Fraction(6004799503160661, 4503599627370496)
>>> a.limit_denominator(10)
Fraction(4, 3)
>>> a
Fraction(6004799503160661, 4503599627370496)
``` 
 Иногда для сохранения точности придется преобразовывать данные вручную:
 ```python
 >>> x+1/3
2.666666666666667
>>> x + Fraction(1,3)
Fraction(8, 3)
 ```
 **Множества**
 
 *Множество* - неупорядоченная коллекция уникальных неизменяемых элементов, которая подджерживает операции математической теории множеств. Множества итерируемы, могут увеличиваться, уменьщаться и содержать объекты разнообразных типов. Создаётся функцией `set`.
 ```python
>>> x = set('abcde')
>>> y = set('bdxyz')
# Операции над множествами
 >>> x-y # Разность
{'e', 'c', 'a'}
>>> x|y # Объединение
{'c', 'a', 'z', 'x', 'd', 'y', 'e', 'b'}
>>> x&y # Пересечение
{'b', 'd'}
>>> x^y # Симметрическая разность (исключающее ИЛИ)
{'e', 'x', 'y', 'z', 'c', 'a'}
>>> x > y, x < y # Надмножество, подмножество
(False, False)
>>> 'e' in x # проверка вхождения
True
 ```
 Методы
 ```python
 >>> x.add('SPAM') # Вставка элемента
 {'c', 'a', 'd', 'e', 'b', 'SPAM'}
 >>> x.update(['x','k','z'] # Слияние: объединение на месте
 >>> x.remove('b') # удаление одного элемента
 >>> x
 {'c', 'a', 'z', 'x', 'd', 'e', 'k', 'SPAM'}
 ```
 Множества могут содержать только объекты неизменяемых типов. Следовательно списки, словари не могут встраиваться во множества, но кортежи могут. 
 ```python
 >>> s.add([1,2,3])
 TypeError: unhashable type: 'list'
 >>> s.add({a:1})
 TypeError: unhashable type: 'dict'
 >>> s.add((1,2,3))
>>> s
{1, (1, 2, 3)}
 >>> s|{(4,5,6), (1,2,3)}
{1, (1, 2, 3), (4, 5, 6)}
 ```
Функция `frozenset` работает в точности как `set`, но создает неизменяемое множество, которое не допускает модификацию и потому может быть внедрено в другие множества.

Включения множеств:
 ```python
 >>> {x**2 for x in [1,2,3,2,4]}
{16, 1, 4, 9}
>>> {x for x in 'spramm'}
{'p', 'a', 's', 'm', 'r'}
 ```
 
 **Булевские занчения**
 
 `True == 1` и `False == 0`
 
 **Численные расширения**
 
Если вам необходимо заниматься серьезным перемалыванием чисел, то дополнительное расширение для Python под названием NumPy (Numeric Python) предоставляет расширенные инструменты численного программирования, такие как матричный тип данных, обработка векторов и библиотеки сложных вычислений.

 ## Глава 6. Кратко о динамической типизации.

Порядок действий при ситуации:
```python
a = 3
```
1. Создание объекта для представления значения 3.
2. Создание переменной а, если она не существует.
3. Связываение а с новым объектом 3.

* Объекты - это области выделенной памяти с достаточным пространством для предоставления значений, для которых они предназначены.
* Переменные - это записи в системной таблице, в которых предусмотрены места для связей с объектами.
* Ссылки - это следуемые указатели от переменных к объектам.

Каждый объект содержит два стандартных заголовочных поля: *обозначение типа*, применяемое для пометки типа объекта, и *счетчик сылок*, используемый для определения, когда можно освободить память, которую занимает объект.

---
**Именяемые типы в Python: списки, словари и множества.**
---

 ```python
>>> a = 2 # а - это просто ссылка на объект int со значением 2 
>>> b = a # b - d не ссылается на а, вместо а подставляется ссылка на объект,
          # так что b это ссылка на объект int со значением 2
>>> a, b
(2, 2)
>>> a = 24 # теперь а ссылкается на другой объект
>>> a,b
(24, 2) # но b никто не менял, она по прежднему сслыка на объект int со значением 2
# НО!!!
>>> a = [1,2,3] 
>>> b = a # a и b сслыкаются на один и тот же объект list
>>> a[0]=124 # меняем на ходу один из элементов этого объекта
>>> a,b
([124, 2, 3], [124, 2, 3]) # a и b продолжают ссылкаться на этот list, не смотря на то что он изменен
```
 Если нам не требуется такое поведение то мы можем запросить копию объекта:
 ```python
>>> a = [1,2,3]
>>> b = a[:] # или list(a), copy.copy(a), и т.д.
>>> a,b
([1, 2, 3], [1, 2, 3])
>>> a is b
False
>>> a[0] = 123
>>> a,b
([123, 2, 3], [1, 2, 3])
 ```
 Для словарей и множест нарезка не подходит так как они не являбются последовательностями. Для них нужно использовать модуль `copy`.
 ```python
 import copy
 x = copy.copy(y) # создаёт поверхностную копию верхнего уровня
 x = copy.deepcopy(y) # создаёт глубокую копию, полностью копируя все вложенные части
```
 
 В учебнике сказано, что со строками и числами ссылки будут указывать на один и тот же объект даже в случе копирования из-за того что эти объекты попадают в кэш. Хотя вообще по логике в случае неизменяемых объектов нет смысла создавать копию, я б в логике языка так и оставлял ссылку на объект. 
 ```python
 >>> a = 1.32131
>>> b = a
>>> a is b
True
>>> b = copy.copy(a)
>>> a == b
True
>>> a is b
True
import sys
 >>> sys.getrefcount(1.32131) # указывает количество ссылок на объект
2
 ```
 Существует термин *слабая ссылка* - это такая ссылка, которая не препятствует сборке мусора. Т.е. если последними оставшимися сслыками на объект оказываются слабые сслыки, тогда выдеоенная под объект память освобождается.
 
## Глава 7. Фундаментальные основы строк.

*Строка* - упорядоченная коллекция символов. Является первым представителем более крупного класса *последовательности*.

![image](https://user-images.githubusercontent.com/116806816/202838994-92b820c2-3cf2-41cd-8246-85cccc062822.png)

![image](https://user-images.githubusercontent.com/116806816/202839019-3174f4aa-6a74-4332-97b2-a4b5ec033097.png)

Обратная косая черта используется для введения специальных кодировок символов, известных как *управляющие последовательности*.

![image](https://user-images.githubusercontent.com/116806816/202840965-1930d939-4091-4f74-b23b-a2d5a3d81906.png)

 Если перед кавычкой поставить `r`, то это будет неформатированная строка. Неформатированные строки подавляют управляющие последовательности. Их удобно использовать для написания адресов, дабы обратная косая черта не создавала управляющий символ.
 ```python
 b = r'С:\new\text.dat
 ```
 *Блочные строки* - многострочный текст обособленный тремя кавычками, двойнми или одинарными не важно, главное что б какие в начале - такие и в конце.
 Используются, когда нужно вставить многострочный текст, код HTML, XML, JSON, либо для строк документации как большой комментарий к кодуб либо для временного отключения нескольких строк кода.
 
**Базоввые операции**
 
 ```python
>>> a = 'abcdefg'
>>> for c in a: print(c, end = '!')
a!b!c!d!e!f!g!
```
Расширенное нарезание (S [i: j :k] ) принимает шаг (или страйд (большой шаг)) к, который по умолчанию равен +1. Например для смены порядка можно `S[::-1]`, или `S[::2]` для извлечения элементов только с четным индексом. 
 При отрицательном страйде (*страйд* - шаг) смысл первых двух границ по существу изменяется на противоположный. Таким образом, срез S [5:1: -1] извлекает элементы со второго по пятый в обратном порядке (результат содержит элементы по смещениям 5, 4, 3 и 2).
 
 Преобразование символа в его внутренний целочисленный код.
 ```python
 >>> ord(s)
 115
 >>> chr(115)
 's'
 ```
 Преобразование строки двоичных цифр в целоеЖ
 ```python
 >>> int('1101', 2)
 13
 >>> bin(13)
 '0b1101'
 ```
 
 **Изменение строк**
 
 *Извлечение атрибутов*
 
*Объект.Атрибут* означает извлечь атрибут из объекта.
 
 *Выражение вызова* 
 
 *Функция(Аргументы)* означает вызвать код функции передав ему некоторое количество аргументов через запятую и возвратить результирующее значение функции.
 
 Объединение этих двух операций позволяет вызывать *Метод Объекта*.
 
 *Объект.Метод(Аргумент)* это означает Вызвать метод для обработки объекта с аргументами.
 
 43 строковых метода, в квадратных скобках необязательные аргументы.
 
 ![изображение](https://user-images.githubusercontent.com/116806816/202975199-97b22767-d242-4b5b-91d3-aeb9c42d8958.png)

 **Методы:**
  
* Нарезание  `s = s[:10:2] + 'xx' + s[5:]`
* `replace` - замена подстрок, можно использовать необязательный третий аргумент для ограничения количесва замен.
```python
>>> 'aa$bb$cc$dd'.replace('$', 'SPAM', 2)
'aaSPAMbbSPAMcc$dd'
* `find` - поиск подстроки, вернет -1 если не найдет. 
```python
>>> s = 'xxxxSPAMxxxxSPAMxxxx'
>>> where = s.find('SPAM')
>>> where 
4
>>> s = s[:where] + 'EGGS' + s[(where + len('EGGS')):]
>>> s
'xxxxEGGSxxxxSPAMxxxx'
```
* Сборка из частей в строку `list` -> `json`. В обзем случае метод выглядит так: `'Разделителm'.join(Итерируемый объект)`
```python
>>> s = 'spammy'
>>> l = list(s)
>>> l
['s', 'p', 'a', 'm', 'm', 'y']
>>> l[3] = l[4] = 'x'
>>> s = ''.join(l)
>>> s
'spaxxy'
```
* Разбор строки на части `split` разбивает строку на список подстрок согласно строке разделителя, по умолчанию разделитель - пробел.	
```python
>>> line = 'aaa bbb ccc'
>>> line.split()
['aaa', 'bbb', 'ccc']
>>> line = 'aaa,bbb,ccc'
>>> line.split(',')
['aaa', 'bbb', 'ccc']
```



