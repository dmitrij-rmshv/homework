"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = input("Введите число 'n': ")
nnn = int(n + n + n)
nn = int(n + n)
n = int(n)
print(f"{n} + {nn} + {nnn} = {n + nn + nnn}")