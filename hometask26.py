# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)             A = 2; B = 3 -> 8

def my_pow(number, power_number): # число, степень числа
    if power_number == 1: # условие выхода из рекурсии
        return number
    return my_pow(number, power_number - 1) * number # рекурсивно умножаем число пока степень не станет 1

a, b = 3, 5 # int(input('type A: ')), int(input('type B: '))
print(my_pow(a, b))