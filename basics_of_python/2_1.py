# A
print("Привет, Яндекс!")


# B
print("Как Вас зовут?")

name = input()

print(f"Привет, {name}")


# C
string = input()

print(f"{string}\n" * 3)


# D
nominal = int(input())

print(int(nominal - 2.5 * 38))


# E
price = int(input())
weight = int(input())
money = int(input())

print(money - price * weight)


# F
name = input()
price = int(input())
weight = int(input())
money = int(input())

print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {weight*price}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money-weight*price}руб")


# G
n = int(input())

print("Купи слона!\n" * n)


# H
n = int(input())
string = input()

print(f"Я больше никогда не буду писать \"{string}\"!\n" * n)


# I
n = int(input())
m = int(input())

print(int(m / 2 * n))


# J
name = input()
number = int(input())

print(f"Группа №{number // 100}.")
print(f"{number % 10}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: {number % 100 // 10}.")


# K
number = int(input())
a = number // 1000
b = number // 100 % 10
c = number // 10 % 10
d = number % 10

print(f"{b}{a}{d}{c}")


# L
number1 = int(input())
number2 = int(input())

res1 = (number1 // 1000 + number2 // 1000) % 10
res2 = (number1 // 100 % 10 + number2 // 100 % 10) % 10
res3 = (number1 // 10 % 10 + number2 // 10 % 10) % 10
res4 = (number1 % 10 + number2 % 10) % 10
res = int(f"{res1}{res2}{res3}{res4}")

print(res)


# M
n = int(input())
m = int(input())

print(m // n)
print(m % n)


# N
red = int(input())
green = int(input())
blue = int(input())

print(red + blue + 1)


# O
n = int(input())
m = int(input())
t = int(input())

h = (n + (m + t) // 60) % 24
m = (m + t) % 60

print(f"{h:0>2}:{m:0>2}")


# P
a = int(input())
b = int(input())
c = int(input())

print(f"{(b - a) / c:.2f}")


# Q
total = int(input())
last = input()

print(total + int(last, 2))


# R
total = input()
nominal = int(input())

print(nominal - int(total, 2))


# S
name = input()
price = int(input())
weight = int(input())
money = int(input())

print(f"{'Чек':=^35}")
print(f"Товар:{name: >29}")
print(f"Цена:{f'{weight}кг * {price}': >24}руб/кг")
print(f"Итого:{weight*price: >26}руб")
print(f"Внесено:{money: >24}руб")
print(f"Сдача:{money-weight*price: >26}руб")
print("=" * 35)


# T
n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

w1 = int((n * k2 - n * m)/(k2 - k1))

print(w1, n - w1)
