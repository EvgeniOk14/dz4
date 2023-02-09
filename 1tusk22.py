# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


# Решение1: через ручной ввод чисел:

n = int(input('введите первое положительное целое число n: ')) # ввели первое число n
i = 0
list1 = []
while (i < n): # заполняем первую последовательность n чисел
    list1.insert(i, int(input('введите число последовательности n: ')))
    i+=1
print('печать списка: ', list1, ': ') # печать списка list1
m = int(input('введите второе положительное целое число: ')) # ввели второе число m
list2 = []
j = 0 
while (j < m): # заполняем вторую последовательность m чисел   
    list2.insert(j, int(input('введите число последовательности m: '))) 
    j+=1
print('печать списка: ', list2, ':') # печать списка list2
s1 =set(list1) # пустое множество s1 заполняем списком list1
s2 =set(list2) # пустое множество s2 запоняем списком list2
print('первое множество: ', s1) # печатаем первое множество s1 для наглядности       
print('второе множество: ', s2) # печатаем второе множество s2 для наглядности
cross = s1.intersection(s2) # создаём пересечение двух множеств cross
                             #с целью нахождения повторяющихся элементов
print('пересечение двух множеств: ', cross) # печатаем пересечение двух множеств
                                            # для наглядности
listAfterCross = list(set(cross)) # делаем из множества список listAfterCross
print(sorted(listAfterCross)) # сортируем по возрастанию и выводим на экран элементы списка listAfterCross
