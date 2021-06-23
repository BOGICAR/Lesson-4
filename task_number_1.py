# Задание №1 - сделано
def task_1():
    x = int(input('Аmount of kilometers for the first day: '))
    y = int(input('Аmount of kilometers: '))
    day = 1
    while x < y:
        x *= 1.1
        day += 1
    return day
print(task_1())
