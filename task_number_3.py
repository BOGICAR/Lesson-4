# Задание №3 - сделано
def task_3():
    a = int(input('Please enter an integer number: '))
    b = int(input('Please enter an integer number: '))
    list_1 = []
    if a < b:
        for i in list(range(a, b+1)):
            list_1.append(i)
    else:
        for i in list(range(b, a+1)):
            list_1.append(i)
        list_1.sort(reverse=True)
    return list_1
print('All numbers: ',task_3())
