#1
# ar1 = float(input('Введите числитель'))
# ar2 = float(input('Введите знаменатель'))
# if ar2 == 0:
#     print('Ошибка: Недопустимый аргумент')
# else:
#     def div(ar1, ar2):
#         return ar1 / ar2
#     print(div(ar1, ar2))
#2

# def my_func (name, surname, year, city, email, telephone):
#     return [name, surname, year, city, email, telephone]
# print(my_func(surname = input('enter surname'), name = input('enter name'),
# year = input('enter year'), city = input('enter city'), email = input('enter mail'),
# telephone = input('enter tel')))
#3
# def my_func(x, y, z):
#     sequence = [x, y, z]
#     total = []
#     max_1 = max(sequence)
#     total.append(max_1)
#     sequence.remove(max_1)
#     max_2 = max(sequence)
#     total.append(max_2)
#     print(sum(total))
# my_func(5, 6, 7)
#4
# x = float(input('Введите основание'))
# y = float(input('Введите степень'))
# if y > 0:
#     print('Ошибка: Недопустимый аргумент')
# else:
#     def my_func(x, y):
#         return x ** y
#     print(my_func(x,y))
# def power(a, n):
#     res = 1
#     for i in range(abs(n)):
#         res *= a
#     if n >= 0:
#         return res
#     else:
#         return 1 / res
#5
# def my_sum ():
#     sum_res = 0
#     ex = False
#     while ex == False:
#         number = input('Ввод числа, при выходе ввести stop - ').split()
#         res = 0
#         for el in range(len(number)):
#             if number[el] == 'n' or number[el] == 'stop':
#                 ex = True
#                 break
#             else:
#                 res = res + int(number[el])
#         sum_res = sum_res + res
#         print(f'Текущее значение {sum_res}')
#     print(f'Конечное число {sum_res}')
# my_sum()

# def int_func (*args):
#     word = input("введите строку ")
#     print(word.title())
#     return
# int_func()

