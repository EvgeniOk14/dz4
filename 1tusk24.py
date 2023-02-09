# Задача 24:
#  В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#  Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
#  собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
#  которое может собрать за один заход собирающий модуль,
#  находясь перед некоторым кустом заданной во входном файле грядки.
# ввод: 4 -> 1 2 3 4
# вывод: 9

# решение 1: ручной ввод

i = 0
n = int(input('В ведите количество кустов n в диапазоне от 3 до 1000: '))
while (n <= 3 or n >= 1000):
    print('Вы ввели число вне заданного диапазона! Введите заного!\n ')
    n = int(input('В ведите количество кустов n в диапазоне от 3 до 1000: '))
    i+=1  
print('Вы ввели количество кустов равное: ', n)    
maxSum = 0
bushBerry = []
j = 0
while (j < n):
    bushBerry.insert(j, int(input('Введите количество ягод на кусте в диапазоне от 3 до 11: ')))
    j+=1 
print('Вы ввели количество ягод на кусте равное: ', bushBerry)  
maxSum = 0
pos = 0
for i in range(n-1):
    
    if((bushBerry[i-1] + bushBerry[i]+ bushBerry[i+1]) >= maxSum):
        maxSum = bushBerry[i-1] + bushBerry[i]+ bushBerry[i+1] 
        pos = i+1
        print(i+1, ' заход модуля. Максимальный урожай равен: ', bushBerry[i-1], ' + ', bushBerry[i], ' + ', bushBerry[i+1], ' = ', maxSum)
    
    else:
        sum = bushBerry[i-1] + bushBerry[i]+ bushBerry[i+1]
        print(i+1, ' заход модуля. Максимальный урожай равен: ', bushBerry[i-1], ' + ', bushBerry[i], ' + ', bushBerry[i+1], ' = ', sum)

    if ((bushBerry[i-2] + bushBerry[i-1]+ bushBerry[i]) >= maxSum):
        maxSum = bushBerry[i-2] + bushBerry[i-1]+ bushBerry[i]
        print(n, ' заход модуля. Максимальный урожай равен: ', bushBerry[i-2], ' + ', bushBerry[i-1], ' + ', bushBerry[i], ' = ', maxSum)    
    
print('самый максимальный урожай на ', pos, ' заходе модуля и равен: ', maxSum) 