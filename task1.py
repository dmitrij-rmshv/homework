"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
a = 3
b = 4.5
c = "text"
print("int var a = ", a)
print("float var b = ", b)
print("str var c = ", c)

a = int(input("Введите целое число: "))
b = int(input(" ..и ещё одно число: "))
c = a / b
d = input('введите строку "делить на" : ')
e = input('введите строку "равно" : ')
print(f"{a} {d} {b} {e} {c:0.2f}")