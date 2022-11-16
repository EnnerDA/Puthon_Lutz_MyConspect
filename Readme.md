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

```
>>> import script1
```
привелет к выполнению сценария script1.py , но только однократно. Считается, что импорт затратная операция, дальнейщие вызовы import script1 ничего не делают.
если требуется вызвать модуль заново, то
```
from imp import reload
reload(module1)
```
Операции импорта обязаны искать файлы, компилировать их в байт-код и выполнять код.

*Модуль* - пакет имен переменным, известный под названием пространство имен, и имена внутри такого пакета называются - *атрибутами*. Т.е. *атрибут* - это имя переменной, которая прикрепляется к специфическому объекту (вроде модуля).

Формально `from` копирует атрибуты модуля, так что они становятся просто переменными на принимающей стороне.

Функция `dir` вызывается с именем импортированного модуля в круглых скобках, она возвращает все атрибуты внутри 	
модуля. Имена с ведущими и завершающими двойными подчеркиваниями (__ X__) являются встроенными именами.
```
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
 
**Функция dir просто выдает имена методов. Чтобы выяснить, что делает тот или иной метод, его имя можно передать функции help:**	
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
* + сложение (конкатенация)
* * повторение
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
```
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
Проверка навхождение ключа в словарь:
```
if 'name' in rec:
    print('good')
```
Интересный синтаксис:
```python
>>> value = rec['x'] if 'x' in rec else 1 #проверка на вхождение ключа 'x' в словарь rec и ветвление в одной строке
>>> value
1
```
Если требуется наязать порядок в последовательности элементов словаря, то вот вариант:

1. Получаем список ключей методом keys()
2. сортируем этот список методом sort
3. теперь моем пройти все клчи в нужном порялке циклом for
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
```
>>> t = (1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> t[0] # индексацияб нарезание и т.д.
1
 >>> t.index(4) # возвращает индекс элемента со значением 4
3
>>> t.count(4) # считает количество элементов со значением 4
1
>>> t[0] = 2 # выдаст ошибку, т.к. кортеди не изменяемы!
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

Для кодирования и декодирования используем encode / decode:
```
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

*Множество* - неупорядоченная последовательность уникальных элементов. Задаются функцией set.
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

