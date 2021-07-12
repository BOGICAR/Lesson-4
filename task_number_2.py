# Задание №2 - сделано
def user_input():
    list_1 = []
    u_input = 1
    while u_input != 0:
        u_input = int(input('Enter a number: '))
        list_1.append(u_input)
    list_1.pop(-1)
    return list_1


def amount_numbers(list_1):
    return len(list_1)


def sum_numbers(list_1):
    return sum(list_1)


def multiply_numbers(list_1):
    multiply_list_1 = 1
    for i in list_1:
        multiply_list_1 *= i
    return multiply_list_1


def average_value(list_1):
    average_val = sum(list_1)/len(list_1)
    return average_val


def max_value(list_1):
    max_val = max(list_1)
    index_max_val = list_1.index(max_val)
    return max_val, index_max_val


def even_odd(list_1):
    even_numbers = 0
    odd_numbers = 0
    for i in list_1:
        if i % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    return even_numbers, odd_numbers


def second_largest_element(list_1):
    list_2 = list_1.copy()
    max_list_2 = max(list_2)
    index_max_list_2 = list_2.index(max_list_2)
    list_2.pop(index_max_list_2)
    max_value_list_2 = max(list_2)
    return max_value_list_2


def amount_max(list_1):
    amount_max_value = 0
    for i in list_1:
        if i == max(list_1):
            amount_max_value += 1
    return amount_max_value


def main():
    x = user_input()
    final_list = {'Number of attempts: ': amount_numbers,
                  'Sum: ': sum_numbers,
                  'Multiply list: ': multiply_numbers,
                  'Average value: ': average_value,
                  'Max value and index: ': max_value,
                  'Total of even numbers and total of odd numbers: ': even_odd,
                  'Second largest element: ': second_largest_element,
                  'Amount of max value: ': amount_max}
    for key, funk in final_list.items():
        print(key, funk(x))


main()
