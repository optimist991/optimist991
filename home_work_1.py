# import math
#
#
#
# def formula(x, y):
#     z = (x - y) / 1 + (x * y)
#     print(z)
#
#
# # вычеслить полупериод маятника длины l
# def lengh(l):
#     t = 2 * math.pi / l * 2
#     print(t)
#
# # вычеслить углы треугольника
# def triengl(a, b, c):
#     v = math.acosh((a * 2) * (b * 2) * (c ** 2))/ 2 * (a * b)
#     m = math.degrees(v)
#     print(m)
#
# # а возвести в 5 и 19 степень используя только *
# def a(a):
#     a_5 = a * a * a * a * a
#     print(a_5)
#     a_19 = a ** 19
#     print(a_19)
#
# # Написать цикл который будет число которое больше 0 возводить в квадрат и печатать
# def squer(a, b, c):
#     if a > 0:
#         a = a ** 2
#         print(a)
#     else:
#         print('less 0')
#
#     if b > 0:
#         b = b ** 2
#         print(b)
#     else:
#         print('less 0')
#
#     if c > 0:
#         c = c ** 2
#         print(c)
#     else:
#         print('less 0')

# Высокостный год
# year = int(input())
# if year % 4 != 0:
#     print("usual year")
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print("intercalary year")
#     else:
#         print("usual year")
# else:
#     print("intercalary year")

# a = int(input())
# b = int(input())
# # if a > b:
# #     c = f'{a} more {b}'
# # else:
# #     c = f'{b} more {a}'
# # print(c)
# c = 5
# # while c < 5:
# #     print(a+b)
# #     c += 1
# for i in range(0, 5):
#     print(a + b)


# m = int(input())
#
# if m <= 2 or m == 12:
#     print('Winter')
# elif 2 < m <= 5:
#     print('Spring')
# elif 5 < m <= 8:
#     print('Summer')
# elif 8 < m <= 11:
#     print('Outam')
# else:
#     print("not in range 1 - 12")

# deposit = 10000
# pers = 0.75
# years = 0
# i = 0
# while True:
#     i += 1
#     deposit = deposit * pers + deposit
#     if years == i:
#         print(deposit)
#         break

# def per(deposit, pers, years):
#     i = 0
#     while True:
#         i += 1
#         deposit = deposit * pers + deposit
#         if years == i:
#             print(deposit)
#             break
#
# per(10000, 0.75, 2)

# a = [10, 20, 30, 40, 50, 60]
# a.append(10)
# print(a)
# b = [10]
# c = a + b
# print(c)

# dict
#
# a = {'key': 10}
# # print(type(a['key']))
# a.get('key2', 5)
# b = {}
# c = dict(key = 10, key2 = 'Hi')
# # print(c)
#
# a = {'key': 10,
#      'key2': 20}
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a.copy())
# print(a.pop('key'))
# print(a)

# def main():
#     lan = ['php', 'java', 'py']
# for _ in range(5):
#     print('Hi')



# a = '%'
# if a.isdigit():
#     print('Number')
#
# a = 'aAAAAAASSSDDDDDD'
# print(a.find('f'))
# print(a[-2: :-1])
# print(a.strip())
# print(a.lower())


import math


# import shlex
# from collections import Counter
#
# text = """Шасси такой модульной системы, как предполагается, будет представлять собой корпус с блоком питания,
# охлаждением и пассивной объединительной платой со слотами PCIe Express, в которую будет устанавливаться основной модуль
# ПК и, возможно, дополнительные платы расширения. Отличие от классической конструкции системного блока при этом
# заключается в том, что роль материнской платы здесь исполняет простейшая объединительная плата со слотами, а основные
# части компьютера, включая процессор, чипсет и память, заключены в заменяемый модуль, похожий по своему внешнему
# исполнению на крупногабаритную карту расширения для слота PCI Express.
#
# В стенах Intel над данным проектом работает команда инженеров, занимающаяся системами семейства NUC. И именно поэтому
#  этот проект выглядит похоже на представленную на Computex 2019 идею Intel NUC Compute Element — миниатюрных заменяемых
#   вычислительных элементов для мобильных компьютеров. Новый, большой «Элемент» — это, фактически, десктопное и
#   полноразмерное воплощение той же идеи, позволяющее пользователям получить в своё распоряжение более мощные и более
#   гибкие модульные компьютеры класса NUC.
# "Эле мент" "Эле мент" "Эле мент" "Эле мент"
# На мероприятии представители Intel продемонстрировали пример такого основного модуля ПК. Показанный "Эле мент" выглядел
#  подобно закрытой кожухом со встроенной системой охлаждения крупной двухслотовой видеокарте. Прототип базировался на
#  процессоре Xeon в BGA-исполнении и содержал внутри себя два слота SO-DIMM LPDDR4, два слота M.2, а также набор
#   дополнительных контроллеров, отвечающих за работу портов, выведенных наружу платы: USB, Ethernet,
#   Thunderbolt и проч."""
#
# words = shlex.split(text)
# words = [word for word in words if len(word) > 3]
# Counter(words).most_common(3)
# print(Counter(words).most_common(3))

# lst = ['a', 10, 'abc', 10]
# lst2 = []
# print(lst.count(10))
# lst.extend([10, 20, 30])
# print(lst * 2)
# lst.insert(0, 'A')
# print(lst)
# del lst[0]
# print(lst)
# lst.remove(10)
# print(lst)

# lst = [1, 2, 2, 3, 4, 4, 5]
# print(lst)
# print(set(lst))
# a, b = (10, 20)
# print(a)
# print(b)

# user, created = get_or_creat(id=3)

# def to_set(lst):
#     return set(lst)
#
# lang = (['php', 'php', 'C++', 'php', 'py', 'py'])
# long_set = set(lang)
# res = dict()
# for i in long_set:
#     res[i] = lang.count(i)
#     print(res)



