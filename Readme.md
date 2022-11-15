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
 
 


 



 


 
