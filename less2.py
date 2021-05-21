#1111111111
a = ['a', 'ac', 34, True ,  345, 's']
b=[]
for el in a:
   b.append(type(el))
print(b)
#2

li=[]
while True:
   a=input('Введите число, для выхода нажмите стоп')
   if a.title()=='Stop':
       break
   li.append(a)
   print(li)
for i in range(1,len(li),2):
   li[i], li[i - 1] = li[i- 1], li[i]
print(li)

#3
month = int(input("Введите месяц по номеру "))
season1 = {'winter':1,'spring': 3, 'summer': 6, 'autumn': 9}
season2 = {'winter':2,'spring': 4, 'summer': 7, 'autumn': 10}
season3 = {'winter':12,'spring':5, 'summer': 8, 'autumn': 11}
for element in season1:
    if month == season1[element]:
      print(element)
for element in season2:
    if month == season2[element]:
      print(element)
for element in season3:
    if month == season3[element]:
      print(element)
#Вариант через list
seasons_dict = {1:'winter', 2:'spring', 3:'summer', 4:'autumn'}
month = int(input("Введите месяц по номеру "))
month_list = list(seasons_dict.values())
if month ==1 or month == 12 or month == 2:
     print(month_list[0])
if month == 3 or month == 4 or month ==5:
     print(month_list[1])
if month == 6 or month == 7 or month == 8:
     print(month_list[2])
if month == 9 or month == 10 or month == 11:
    print(month_list[3])
#4

s_str = input("Enter string: ")
a = s_str.split(' ')
print(a)
for i, el in enumerate(a, 1):
    if len(str(s_str)) <= 20:
        print(f"{i} - {el}")
    else:
        print(f"{i} - {s_str [el] [0:20]}")
#5
d_li = [7, 4, 3, 2, 2, 2]
print(d_li)
num = int(input("Введите число "))
while num != 111:
    for el in range(len(d_li)):
        if d_li [el] == num:
            d_li.insert(el + 1, num)
            break
        elif d_li[0] < num:
            d_li.insert(0, num)
        elif d_li[-1] > num:
            d_li.append(num)
        elif d_li[el] > num and d_li[el + 1] < num:
            d_li.insert(el + 1, num)
    print(d_li)
    break


# #6
numstr = int(input("Введите кол-во SKU"))
n = 1
a_dict = []
b_list = []
while n <= numstr:
    a_dict = dict({'Название': input("введите название "),
                    'Цена': input("Введите цену "),
                    'Количество': input('Введите кол-во '),
                    'Ед': input("Введите ед ")})
    b_list.append((n, a_dict))
    n += 1
print(b_list)
