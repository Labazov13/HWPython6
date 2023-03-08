# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_element=int(input("Введите первый элемент массива: "))
step=int(input("Введите разность между элементами массива: "))
count_element=int(input("Введите количество элементов массива: "))


def arifm_progress(first_el,step,count_el):
    list_result=[None for i in range(count_el)]
    count=0
    for i in range(len(list_result)):
        list_result[i]=first_el+count
        count+=step
        print(list_result[i])

    
arifm_progress(first_element,step,count_element)
