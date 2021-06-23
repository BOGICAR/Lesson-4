# Задание №4 - сделано
def task_4():
    entered_number_i = int(input('Please enter an integer number <=9: '))
    list_1 = []
    if entered_number_i <= 9:
        for i in list(range(1, entered_number_i+1)):
                list_1.append(str(i))
                list_2 = ''.join(list_1)
                print(list_2)
    else:
        print('Enter number <= 9')

task_4()
