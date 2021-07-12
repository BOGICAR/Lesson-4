# Задание №2 - сделано
def task_2():
    entered_1 = input('Enter some words: ')
    amount_element = len(entered_1)
    amount_words = len(entered_1.split())
    # print(amount_element)
    # print(amount_words)
    return amount_words, amount_element


print('Amount of words, elements: ', task_2())
