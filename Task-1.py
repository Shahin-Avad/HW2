"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def summ(first_num, second_num):
    a = first_num + second_num

    return a


def subt(first_num, second_num):
    a = first_num - second_num

    return a


def mult(first_num, second_num):
    a = first_num * second_num

    return a


def divi(firs_num, second_num):
    a = firs_num / second_num
    if second_num == 0:
        print('Деление на 0 нельзя')
    else:
        return a


def calc():
    sign = input('Введите операцию (+, -, *, / или 0 для выхода): ')

    if sign == '0':

        return 'Вы вышли'

    else:
        b = int(input("Введите первое число: "))
        c = int(input("Введите второе число: "))

        if sign == '+':
            print('Ваш результат: ', summ(b, c))

        elif sign == '-':
            print('Ваш результат: ', subt(b, c))

        elif sign == '*':
            print('Ваш результат: ', mult(b, c))

        elif sign == '/' and c != 0:
            print('Ваш результат: ', divi(b, c))

        elif sign == '/' and c == 0:
            print('Errdivbyzero')

        else:
            print('Короче, я тебя спас и в благородство играть не буду: я выполню для тебя прогу заново — и мы в расчете.\n\
Заодно посмотрим, как быстро у тебя башка после этого прояснится. А по твоей теме постараюсь разузнать. \nХрен его знает, \
на кой ляд тебе этот ', sign, ' сдался, но я в чужие дела не лезу, хочешь в ', sign, ' значит есть за что...')
        return calc()


calc()
