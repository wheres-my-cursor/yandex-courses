# A
print("Как Вас зовут?")
print(f"Здравствуйте, {input()}!")
print("Как дела?")
mood = input()
if mood == "хорошо":
    print("Я за Вас рада!")
elif mood == "плохо":
    print("Всё наладится!")


# B
petya = int(input())
vasya = int(input())

if petya > vasya:
    print("Петя")
else:
    print("Вася")


# C
petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print("Петя")
elif vasya > petya and vasya > tolya:
    print("Вася")
else:
    print("Толя")


# D
petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print("1. Петя")
    if vasya > tolya:
        print("2. Вася\n3. Толя")
    else:
        print("2. Толя\n3. Вася")
elif vasya > petya and vasya > tolya:
    print("1. Вася")
    if petya > tolya:
        print("2. Петя\n3. Толя")
    else:
        print("2. Толя\n3. Петя")
else:
    print("1. Толя")
    if vasya > petya:
        print("2. Вася\n3. Петя")
    else:
        print("2. Петя\n3. Вася")



# E
n = int(input())
m = int(input())

if (6 + n) > (12 + m):
    print("Петя")
else:
    print("Вася")


# F
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES")
else:
    print("NO")


# G
num = int(input())

if (num % 10 == num // 1000) and (num % 100 // 10 == num // 100 % 10):
    print("YES")
else:
    print("NO")


# H
sentence = input()

if "зайка" in sentence:
    print("YES")
else:
    print("NO")


# I
name1 = input()
name2 = input()
name3 = input()

print(min(name1, name2, name3))


# J
password = int(input())

a = password % 10 + password // 10 % 10
b = password // 10 % 10 + password // 100

if a > b:
    print(f"{a}{b}")
else:
    print(f"{b}{a}")


# K
num = int(input())

num1 = num % 10
num2 = num // 10 % 10
num3 = num // 100

if num2 > num3:
    num3, num2 = num2, num3
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2


if (num1 + num3) == num2 * 2:
    print("YES")
else:
    print("NO")


# L
a = int(input())
b = int(input())
c = int(input())

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("YES")
else:
    print("NO")

# M
e = int(input())
g = int(input())
h = int(input())

if e // 10 == g // 10 == h // 10:
    print(f"{e // 10}")
elif e % 10 == g % 10 == h % 10:
    print(f"{e % 10}")


# N
num = int(input())

num1 = num % 10
num2 = num // 10 % 10
num3 = num // 100

if num2 > num3:
    num3, num2 = num2, num3
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2

mx = f"{num3}{num2}"
mn = f"{num1}{num2}"

if num1 == 0:
    mn = f"{num2}{num1}"
if num2 == 0:
    mn = f"{num3}{num3}"

print(mn, mx)


# O
num1 = int(input())
num2 = int(input())


res1 = max(num1 // 10, num1 % 10, num2 // 10, num2 % 10)
res3 = min(num1 // 10, num1 % 10, num2 // 10, num2 % 10)

res2 = (num1 // 10 + num1 % 10 + num2 // 10 + num2 % 10 - res1 - res3) % 10

print(res1, res2, res3, sep="")

# P
num1 = int(input()) 
name1 = "Петя"
num2 = int(input())
name2 = "Вася"
num3 = int(input())
name3 = "Толя"

if num2 > num3:
    num3, num2 = num2, num3
    name3, name2 = name2, name3
if num1 > num2:
    num1, num2 = num2, num1
    name1, name2 = name2, name1
if num2 > num3:
    num2, num3 = num3, num2
    name2, name3 = name3, name2

print(f"{f'  {name3}  ': ^24}")
print(f"{f'  {name2}  ': <24}")
print(f"{f'  {name1}  ': >24}")
print(f"   II      I      III   ")


# Q
a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0:
    print("No solution")
elif a == 0:
    x1 = - c / b
    print(f"{x1:.2f}")
elif d < 0:
    print("No solution")
elif d == 0:
    x1 = - b / 2 / a 
    print(f"{x1:.2f}")
else:
    x1 = (d**0.5 - b) / 2 / a 
    x2 = (- d**0.5 - b) / 2 / a
    if x1 < x2:
        print(f"{x1:.2f} {x2:.2f}")
    else:
        print(f"{x2:.2f} {x1:.2f}")


# R
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num2 > num3:
    num3, num2 = num2, num3
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2

if num3**2 == num2**2 + num1**2:
    print("100%")
elif num3**2 < num2**2 + num1**2:
    print("крайне мала")
elif num3**2 > num2**2 + num1**2:
    print("велика")


# S
x = float(input())
y = float(input())

if y < 0 and (y >= (0.25 * x**2 + 0.5 * x - 8.75)):
    print("Опасность! Покиньте зону как можно скорее!")
elif y >= 0 and ((x <= -4 and y <= (5 / 3 * x + 35 / 3)) or (y <= 5 and -4 <= x <= 0)):
    print("Опасность! Покиньте зону как можно скорее!")
elif y >= 0 and (x >= 0 and (x**2 + y**2) <= 25):
    print("Опасность! Покиньте зону как можно скорее!")
elif (x**2 + y**2) >= 100:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
else:
    print("Зона безопасна. Продолжайте работу.")


# T
sentence2 = input()
sentence1 = input()
sentence3 = input()

if sentence2 > sentence3:
    sentence3, sentence2 = sentence2, sentence3
if sentence1 > sentence2:
    sentence1, sentence2 = sentence2, sentence1
if sentence2 > sentence3:
    sentence2, sentence3 = sentence3, sentence2


if "зайка" in sentence1:
    print(sentence1, len(sentence1))
elif "зайка" in sentence2:
    print(sentence2, len(sentence2))
elif "зайка" in sentence3:
    print(sentence3, len(sentence3))
