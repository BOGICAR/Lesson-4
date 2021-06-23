# Задание №2 - сделано
def task_2_1():
    entered_number = 1
    number_of_attempts = -1
    list_1 = []
    while entered_number != 0:
        entered_number = int(input('Please enter an integer number: '))
        list_1.append(entered_number)
        number_of_attempts += 1
    return number_of_attempts
# print('Number of attempts: ',task_2_1())


def task_2_2():
    entered_number = 1
    list_1 = []
    sum_list_1 = 0
    while entered_number != 0:
        entered_number = int(input('Please enter an integer number: '))
        list_1.append(entered_number)
        sum_list_1 = sum(list_1)
    return sum_list_1
# print('Sum: ',task_2_2())


def task_2_3():
    entered_number = 1
    list_1 = []
    multiply_list_1 = 1
    while entered_number != 0:
        entered_number = int(input('Please enter an integer number: '))
        list_1.append(entered_number)
        if entered_number == 0:
            list_1.pop(-1)
    for i in list_1:
        multiply_list_1 = multiply_list_1 * i
    return multiply_list_1
# print('Multiply list: ',task_2_3())


def task_2_4():
    entered_number = 1
    number_of_attempts = -1
    list_1 = []
    sum_list_1 = 0
    while entered_number != 0:
        entered_number = int(input('Please enter an integer number: '))
        list_1.append(entered_number)
        number_of_attempts += 1
        sum_list_1 = sum(list_1)
    average_value = sum_list_1/number_of_attempts
    return average_value
# print('Average value: ',task_2_4())


def task_2_5():
    entered_number = 1
    list_1 = []
    max_value = 1
    index_max_value = 1
    while entered_number != 0:
        entered_number = int(input('Please enter an integer number: '))
        list_1.append(entered_number)
        max_value = max(list_1)
        index_max_value = list_1.index(max_value)
    return max_value, index_max_value
# print('Max value and index: ',task_2_5())


def task_2_6():
    entered_number = 1
    list_1 = []
    list_even = []
    list_odd = []
    while entered_number != 0:
        entered_number = int(input('Please enter an integer number: '))
        list_1.append(entered_number)
        if entered_number % 2 == 0:
            list_even.append(entered_number)
            len_list_even = len(list_even)
        else:
            list_odd.append(entered_number)
            len_list_odd = len(list_odd)
    return len_list_even, len_list_odd
# print('Total of even numbers and total of odd numbers: ',task_2_6())


def task_2_7():
    entered_number = 1
    list_1 = []
    while entered_number != 0:
        entered_number = int(input('Please enter an integer number: '))
        list_1.append(entered_number)
    max_value = max(list_1)
    index_max_value = list_1.index(max_value)
    list_1.pop(index_max_value)
    second_largest_element = max(list_1)
    return second_largest_element
# print('Second largest element: ',task_2_7())


def task_2_8():
    entered_number = 1
    list_1 = []
    amount_max_value = 0
    while entered_number != 0:
        entered_number = int(input('Please enter an integer number: '))
        list_1.append(entered_number)
    max_value = max(list_1)
    index_max_value = list_1.index(max_value)
    for i in list_1:
        if i == max_value:
            amount_max_value +=1
    return amount_max_value
# print('Amount of max value: ',task_2_8())
