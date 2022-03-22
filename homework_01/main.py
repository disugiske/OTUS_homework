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
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(number,func):
    if func == PRIME:
        return is_prime(number)
    if func == ODD:
        return list(filter(lambda x: x%2, number))
    if func == EVEN:
        return list(filter(lambda x: x%2!=0, number))
print(filter_numbers([1,2,3,4,5,99,6,7,8],ODD))
