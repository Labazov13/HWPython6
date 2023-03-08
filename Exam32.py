import random
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

count=int(input("Введите количество элементов: "))
list_input=[random.randint(-5,20) for i in range(count)]
print(list_input)

def find_index(list_in):
    list_index=[]
    start_value=int(input("Ищем числа от: "))   #5
    end_value=int(input("... до: "))            #10
    for i in range(start_value,end_value):
        for j in range(len(list_in)):
            if list_in[j]==i:
                list_index.append(list_in[j])
    print(list_index)

find_index(list_input)
