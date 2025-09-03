# A
while (count := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")


# B
count = 0
while (sentence := input()) != "Приехали!":
    if "зайка" in sentence:
        count += 1 
print(count)


# C
start = int(input())
end = int(input())

for i in range(start, end + 1):
    print(i, end=" ")


# D
start = int(input())
end = int(input())
step = 1

if end < start:
    step = -1
    end -= 1
else:
    end += 1

for i in range(start, end, step):
    print(i, end=" ")


# E
total = 0.0
while (thing := float(input())) != 0:
    if thing >= 500:
        total += 0.9 * thing
    else:
        total += thing
print(total)


# F
num1 = int(input())
num2 = int(input())

while num1 != 0 and num2 != 0:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1

print(num1 + num2)


# G
num1 = int(input())
num2 = int(input())
a = num1
b = num2

while num1 != 0 and num2 != 0:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1

nod = num1 + num2

print(a * b // nod)


# H
sentence = input()
n = int(input())

for i in range(n):
    print(sentence)


# I
num = int(input())
res = 1

for i in range(2, num + 1):
    res *= i

print(res)


# J
x, y = 0, 0

while (sentence := input()) != "СТОП":
    if sentence == "СЕВЕР":
        y += int(input())
    if sentence == "ЮГ":
        y -= int(input())
    if sentence == "ЗАПАД":
        x -= int(input())
    if sentence == "ВОСТОК":
        x += int(input())

print(y, x, sep='\n')


# K
num = input()
total = 0

for i in num:
    total += int(i)

print(total)


# L
num = input()
mx = 0

for i in num:
    if int(i) > mx:
        mx = int(i)

print(mx)


# M
n = int(input())
first = input()

for i in range(n - 1):
    name = input()
    if name < first:
        first = name

print(first)


# N
num = int(input())
res = "YES"

for i in range(2, int(num**0.5 + 1), 2):
    if num % i == 0:
        res = "NO"

if num == 1:
    res = "NO"

print(res)


# O
n = int(input())
res = 0

for i in range(n):
    if "зайка" in input():
        res += 1

print(res)


# P
num = input()

length = len(num)
num = int(num)
i_start = 0
i_end = length - 1 

start = num // 10**(i_end) % 10 
end = num // 10**(i_start) % 10 

while i_start < i_end and start == end:
    i_start += 1
    i_end -= 1
    start = num // 10**(i_end) % 10 
    end = num // 10**(i_start) % 10 

if i_start < i_end:
    print("NO")
else:
    print("YES")


# Q
num = input()
length = len(num)
num = int(num)

i_start = 0
i_end = length - 1 

while i_start < length:
    start = num // 10**(i_end) % 10 

    if int(start) % 2 != 0:
        print(start, end='')

    i_start += 1
    i_end -= 1


# R
num = int(input())
initial_num = num

if initial_num == 1:
    print("1")
else:
    first = 1
    for i in range(2, int(num**0.5 + 1)):
        while num % i == 0:
            if first:
                print(str(i), end=' ')
                first = 0
            else:
                print("*", str(i), end=' ')
            num //= i
    if num != 1 and first:
        print(num)
    elif num != 1 and not first:
        print("*", num)


# S
num = 500
num_div = 500
print(num)
while (sentence := input()) != 'Угадал!':
    if sentence == 'Больше':
        if num_div % 2 == 0:
            num_div = num_div // 2
        else:
            num_div = num_div // 2 + 1
        num += num_div
        print(num)
    else:
        if num_div % 2 == 0:
            num_div = num_div // 2
        else:
            num_div = num_div // 2 + 1
        num -= num_div
        print(num)


# T
n = int(input())
h_prev = 0
number = 0

while number < n:
    b = int(input())
    m = b // 256**2
    r = (b - m * 256**2) // 256
    h_by_e = (37 * (m + r + h_prev)) % 256
    h = b - m * 256**2 - r * 256
    if h >= 100 or h_by_e != h:
        print(number)
        number = n + 1
    else:
        number += 1
    h_prev = h_by_e

if number == n:
    print("-1")
