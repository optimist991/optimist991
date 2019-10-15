"ДОМАШНЕЕ ЗАДАНИЕ № 2"
"  2    15    28    41    54    7    20    33    46    59" "Shulga Andy"

# "2   Даны две строки. Определите, содержится ли меньшая по длине строка в большей."
# def line_in_line(line_1, line_2):
#     a = len(line_1)
#     if line_1[:a] == line_2[:a]:
#         print("Vxodit")
#     else:
#         print("no vxodit")
#
# line_in_line("Andy", "AndyShulga")

"15  Дана строка. Если в строке больше трех различных символов, то удалить в строке три любых различных " \
"символа, иначе добавить в строку в произвольных местах новые элементы так, чтобы количество различных " \
"элементов было больше трех."

# text = '1, 2'
# mylist = text.split(', ')
# print(len(mylist))
# mylist_new = []
# mylist_new_2 = []
# if len(mylist) >= 3:
#     mylist_new = mylist[3:]
#     print(mylist_new)
# else:
#     mylist_new_2 = mylist
#     mylist_new_2.append('answer for everething is 42')
#     print(mylist_new_2)

"""28 Дано натуральное число. Получить строку, в которой тройки цифр этого числа разделены пробелом, 
начиная с правого конца. Например, число 1234567 преобразуется в 1 234 567."""
# a = list(str(input()))
# res = [ ''.join(a[::-1][i:i+3])[::-1]
#         for i in range(0,len(a),3)]
# print(' '.join(res[::-1]))

"""41 Дана строка. Вставить после каждого символа два случайных символа."""
# from random import randint
#
# def random():
#     while True:
#         a = randint(65, 123)
#         if not 90 < a < 97:
#             return chr(a)
#
# s = input()
# for c in s:
#     print(c, random(), random(), sep='', end='')

"""54 Дан текст. Найдите наибольшее количество идущих подряд цифр."""

# text="Hii`myoandmydaybirthday1988andiwant"
# coun=0
# max_num=0
# for i in text:
#   if (i.isdigit()):
#     coun+=1
#   else:
#     if max_num<coun:
#       max_num=coun
#     counter=0
# print(max_num)


"""7 Дана строка. Вывести первый, последний и средний (если он есть)) символы."""

# def middle(text):
#     if len(text) % 2 == 0:
#         a = "no inside letter"
#     else:
#         a = text[len(text) // 2]
#     print(text[0], a, text[-1])
#
# middle('hell')

"""20 Даны два слова. Найдите только те символы слов, которые встречаются в обоих словах только один раз."""


# def same(word_1, word_2):
#     for letter_1 in word_1:
#         for letter_2 in word_2:
#             if letter_1 == letter_2:
#                 print(letter_1)
#             else:
#                 pass
#
#
# same('andy', 'argi')

"""33 Удалить в строке все лишние пробелы, то есть серии подряд идущих пробелов заменить на одиночные пробелы.
 Крайние пробелы в строке удалить."""


# def del_space(text):
#     text = text.strip()
#     print(text)
#     print(text.replace('      ', ' '))
#
#
# del_space('  ghbdtn      ghjf    ')

"""46 Строка состоит из слов, разделенных одним или несколькими пробелами. Переставьте слова по убыванию их длин."""

# def sort(text):
#
#     text = text.split(' ')
#     text = sorted(text, key=len)
#     print(text)
#
# sort('asdadaasdsadsa re fdfs  sdfsfsd')


"""59 Замените в строке все вхождения 'word' на 'letter'."""

# def change(text):
#     print('Очень интересное задание - нихера не понял)')
#
# change('Chto-to')