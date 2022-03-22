"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    return list(map(lambda x: x ** 2, numbers))
power_numbers(1, 2, 5, 7)


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
ODD = lambda x: x%2
EVEN = lambda x: x%2!=0
PRIME = 1

def filter_numbers(number,func):
    if func == 1:
        return is_prime(number)
    else:
        return list(filter(func, number))
print(filter_numbers([2, 3, 4, 56, 53, 7, 9, 5, 97, 6], PRIME))
