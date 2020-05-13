"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км
"""

print("Спортсмен занимается ежедневными пробежками.")
a = int(input("В первый день его результат составил, километров: "))
print("Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего")
b = int(input("Введите конечный результат, километров: "))
day = 1  # текущий день, проинициализирован первым днём
result = a  # текущий результат; проинициализирован начальным результатом
while result < b:
    day += 1
    result *= 1.1
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.")