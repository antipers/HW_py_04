# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


def sorting(list):
    copy_listt = []
    for i in range(len(list)):
        count = 0
        for k in range(len(list)):
            if i != k and list[i] == list[k]:
                count += 1
        if count == 0:
            copy_listt.append(list[i])
    print(f"Не повторяющиеся элементы: {copy_listt}")


listt= list(map(int, input("Введите числа через пробел: ").split()))
print(listt)
sorting(listt)
