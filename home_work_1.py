import math



def formula(x, y):
    z = (x - y) / 1 + (x * y)
    print(z)


# вычеслить полупериод маятника длины l
def lengh(l):
    t = 2 * math.pi / l * 2
    print(t)

# вычеслить углы треугольника
def triengl(a, b, c):
    v = math.acosh((a * 2) * (b * 2) * (c ** 2))/ 2 * (a * b)
    m = math.degrees(v)
    print(m)

# а возвести в 5 и 19 степень используя только *
def a(a):
    a_5 = a * a * a * a * a
    print(a_5)
    a_19 = a ** 19
    print(a_19)

# Написать цикл который будет число которое больше 0 возводить в квадрат и печатать
def squer(a, b, c):
    if a > 0:
        a = a ** 2
        print(a)
    else:
        print('less 0')

    if b > 0:
        b = b ** 2
        print(b)
    else:
        print('less 0')

    if c > 0:
        c = c ** 2
        print(c)
    else:
        print('less 0')

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