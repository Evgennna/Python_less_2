# 1. Напишите программу банкомат.
#   Начальная сумма равна нулю
#   Допустимые действия: пополнить, снять, выйти
#   Сумма пополнения и снятия кратны 50 у.е.
#   Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#   После каждой третей операции пополнения или снятия начисляются проценты - 3%
#   Нельзя снять больше, чем на счёте
#   При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#   Любое действие выводит сумму денег

def calculate_tax(balance):
    if balance >= 5000000:
        # Вычитаем налог на богатство 10%
        tax = balance * 0.1
        balance -= tax
    return balance

def calculate_interest(balance, operations_count):
    if operations_count % 3 == 0 and operations_count != 0:
        # Начисляем проценты 3%
        interest = balance * 0.03
        balance += interest
        print("Начислены проценты:", interest)
    return balance

def deposit(balance):
    amount = int(input("Введите сумму для пополнения (кратную 50): "))
    if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
        return balance

    balance += amount
    return balance

def withdraw(balance):
    amount = int(input("Введите сумму для снятия (кратную 50): "))
    if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
        return balance

    if amount > balance:
        print("Недостаточно средств на счете")
        return balance

    if amount > 600:
        amount = 600
    elif amount < 30:
        amount = 30

    fee = amount * 0.015
    balance -= amount + fee
    return balance

def print_balance(balance):
    print("Остаток на счете:", balance)

def atm():
    balance = 0
    operations_count = 0

    while True:
        balance = calculate_tax(balance)

        print("Текущий баланс:", balance)

        choice = input("Выберите действие:\n"
                       "1. Пополнить\n"
                       "2. Снять\n"
                       "3. Выйти\n"
                       "Введите номер действия: ")

        if choice == "1":
            balance = deposit(balance)
            operations_count += 1
        elif choice == "2":
            balance = withdraw(balance)
            operations_count += 1
        elif choice == "3":
            print("Операция завершена")
            break
        else:
            print("Некорректный выбор")

        balance = calculate_interest(balance, operations_count)
        print_balance(balance)

atm()



# 2. Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def get_hexadecimal_representation(number):
    hexadecimal = ""

    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    while number > 0:
        remainder = str(number % 16)
        hexadecimal = remainder + hexadecimal
        number = number // 16

    if is_negative:
        hexadecimal = "-" + hexadecimal

    return hexadecimal


num = int(input("Введите целое число: "))
result = get_hexadecimal_representation(num)
print("Шестнадцатеричное представление числа:", result)
print("Шестнадцатеричное представление числа через hex: ", hex(num))


# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и
# произведение * дробей. Для проверки своего кода используйте модуль fractions.

def calculate_fraction_operations(fraction1, fraction2):
    num_1, denom_1 = map(int, fraction1.split('/')) # 1/3 -> ["1", "3"] -> [1, 3]
    num_2, denom_2 = map(int, fraction2.split('/'))

    # Вычисляем сумму и произведение числителей
    num_add = num_1 * denom_2 + num_2 * denom_1
    num_mult = num_1 * num_2

    # Вычисляем знаменатель для обеих операций
    denom_common = denom_1 * denom_2

    # Сокращаем полученные дроби
    gcd_add = greatest_common_divisor(num_add, denom_common)
    gcd_mult = greatest_common_divisor(num_mult, denom_common)

    addition = f"{num_add // gcd_add}/{denom_common // gcd_add}"
    multiplication = f"{num_mult // gcd_mult}/{denom_common // gcd_mult}"

    return addition, multiplication


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


f_1 = input("Введите первую дробь в формате a/b: ")
f_2 = input("Введите вторую дробь в формате a/b: ")

add, mult = calculate_fraction_operations(f_1, f_2)

print("Сумма дробей:", add)
print("Произведение дробей:", mult)

# Проверка с использованием модуля fractions
from fractions import Fraction

f1 = Fraction(f_1)
f2 = Fraction(f_2)

print("Проверка с использованием модуля fractions:")
print("Сумма дробей (fractions):", f1 + f2)
print("Произведение дробей (fractions):", f1 * f2)