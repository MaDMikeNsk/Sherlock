"""
Шерлок считает строку действительной, если все символы строки появляются одинаковое количество раз. Также допустимо,
если он может удалить 1 символ по 1 индексу в строке, а оставшиеся символы будут встречаться столько же раз.
По заданной строке определите, является ли она действительной. Если это так, верните YES, в противном случае верните NO.

Пример: abc -> YES, abcc-> YES(Удаляем c по индексу 2, тогда оставшиеся элементы встречаются 1 раз),
abcсc-> NO(после удаления c по индексу 2, 3 или 4 у нас останется abcc)
"""


def is_real_string(string):
    char_list = list(string)
    char_set = set(char_list)

    list_of_occurence = [string.count(x) for x in char_set]
    count_set = set(list_of_occurence)
    if len(count_set) == 1:
        return True
    else:
        return False


def sherlock(string):
    char_set = set(string)

    if is_real_string(string):
        return print('Original str is real')
    else:
        for char in char_set:
            string_list = list(string)
            string_list.remove(char)
            new_str = list_to_str(string_list)

            if is_real_string(new_str):
                return print('New string is real')

    return print("String can't be real")


def list_to_str(lst):
    res = ''
    for char in lst:
        res += char
    return res


string = 'abccc'
sherlock(string)
