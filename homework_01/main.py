"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    return list(map(lambda x: x ** 2, numbers))



# filter types
def is_prime(num):
    f=[]
    for i in num:
        for a in range(2,i):
            if i%a == 0:
                f.append(i)
                break
            break
    return list(filter(lambda x: x not in f, num))
ODD = 1
EVEN = 2
PRIME = 3

def filter_numbers(number,func):
    if func == 3:
        return is_prime(number)
    if func == 1:
        return list(filter(lambda x: x%2, number))
    if func == 2:
        return list(filter(lambda x: x%2!=0, number))
