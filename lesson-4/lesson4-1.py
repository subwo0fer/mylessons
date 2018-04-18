"""
Функции
Как объявить функцию?
функция это блок кода
Функцию можно вызывать многократно

"""

def hello():  #объявление функции
    print('hello')

print(type(hello))
hello() # вызов функции
hello()

say_hello = hello #присвоить ссылку на функцию переменной
say_hello() #скобки когда вызов функции


def hello_username(name):
    print('Hello,', name)


hello_username('Python')
hello_username('JavaScript')
hello_username('Вася')

def summa(a, b):
    print(a + b)

summa(1, 3)
summa(5) # ошибка, нужны все обязательные аргументы

"""
Передача значений аргументов по ссылке
"""
def parse(src, output):
    src = src.strip('.')

    for i in src.split(): #Метод split позволяет разбить строчку по разделителю, стандартно это пробел
        output.append(i)

src = 'Python is programming language.' 
output = []

print(src, output)
parse(src, output)
print(src, output)

"""
Как задать значение аргумента по умолчанию
"""
def poww(x, p=2): #аргумент p теперь необязательный, если не объявлять то он останется двойкой
    print(x ** p) #аргументв по умолчанию всегда должны быть в конце, иначе ошибка
                  #аргументов должно быть 1-3, максимум 4
poww(5)           #необязательные аргументы всегда должны быть неизменяемым типом данных
poww(2, 3)



def f(i, l=None): #Так можно задать изменяемый тип данных аргументом функции
    l = l or []   #В л записывается первый аргумент который True

"""
Как вернуть значение из функции?
"""

def minus(a, b):
    return a - b  #как только в функции встречается ретурн выполнение функции останавливается
    a = a * b #никогда не выполнится!!!



def f2():
    return 1, 2, 3 #Возвращается в виде кортежа, если нужен явно кортеж то лучше скобки ставить

a, b, c = f2()     #Распаковка кортежа




"""
Переменное количество аргументов в описании функции
"""

def demo_func(i, *args, **kwargs):  #*args должен быть в конце
    """
    args - кортеж
    """
    print(args, type(args))
    print(kwargs, type(kwargs))


demo_func(1, 2, 3, j=4)
demo_func(10, 20, k=True, e=456)

def f3(i, *args, j=1, **kwargs): #именованные попадают в кварг а позиционные в аргс
    print(i, j, args)

f3(2, 5, 5, j=2)

"""
Переменное количество аргументов при вызове функции
"""

def f4(i, j, k, a =None, b=None, c=None):
    print(i, j, k)
    print(a, b, c)

args = [1, 2, 3]
kwargs = {
    'a':10,
    'b':20,
    'c":30,
}

f4(*args)   #звездочка в момент вызова функции разворачивает переменную в значение аргументов, две звездочки разворачивают словарь в значение именованных   аргументов


"""
Анонимная функция - функция без имени (лямбда функция, обычно работает быстрее)
"""

sqrt = lambda x: x ** 0.5  #икс без скобочек, обычно анонимная функция пишется в одну строчку
#lambda: pass
#lambda x, y: pass
print(sqrt(9))

def f5(x, cb):
    return cb(x)
    
print(f5(25, sqrt))


"""
Замыкания - когда внутри одной функции описывается другая фнукция
"""
#aeyrwbz rfhhbhjdfybz
def trim(chars=None):
    #Локальная область видимости функции trim
    #Замкнутая область
    def f(s):
        #Локальная область видимости функции f
        return s.strip(chars)
    return f
    #return lambda s: s.strip(chars) - краткая записб функции f

spaces_trim = trim()
print(spaces_trim('     Hello    '))

slashes_trim = trim('/\\')
print(spaces_trim('asdsad////\\\sad\\\///')

"""
Рекурсивная функция
"""
#5! = 1 * 2 * 3 * 4 * 5
def factorial(x):
    #Прямая рекурсия
    return 1 if x == 0 else x * factorial(x - 1)

print(factorial(5))



#Косвенная рекурсия
#def a():
#   b()
#                эта очень опасная штука
#    
#def b():
#    a()          


#nonlocal (переменная)  функция видит такую переменную в верхних уровнях других функция 
