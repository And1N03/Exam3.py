#1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

# def card_hide(card):
#     return '*' * len(card[:-4]) + card[-4:]
#
# print(card_hide((input('Введите номер карты:'))))



# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

# def palindrome(data):
#     data = data.replace(' ','').lower()
#     return 'Палиндром' if data == data[::-1] else 'Не палиндром'
#
# print(palindrome((input('Введите слово:'))))