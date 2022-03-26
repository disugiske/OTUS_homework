"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    return list(map(lambda x: x ** 2, numbers))



# filter types
def is_prime(num):
    if num==0 or num==1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(number,func):
    if func == PRIME:
        return list(filter(is_prime, number))
    if func == ODD:
        return list(filter(lambda x: x%2!=0, number))
    if func == EVEN:
        return list(filter(lambda x: x%2==0, number))
