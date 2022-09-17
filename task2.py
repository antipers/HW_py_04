# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]


def factors(number):
    base = []
    i = 2
    while i * i <= number:
        while number % i == 0:
            base.append(i)
            number /= i
        i += 1
    if number > 1:
        base.append(number)
    return base


number = int(input("введите число: "))
print(factors(number))
