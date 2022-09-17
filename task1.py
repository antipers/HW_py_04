# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

import math


def trunker(num_float):
    print (num_float)
    trunked = str(num_float)
    return (trunked[0:trunk+2])

num_float = float(input("введите число, которое требуется усечь: "))
trunk = int(input("введите желаемое количество цифр после запятой у искомого числа: "))
print(trunker(num_float))
