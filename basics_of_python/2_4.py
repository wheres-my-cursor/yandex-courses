# A
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=' ')
    print()


# B
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{j} * {i} = {i * j}")


# C
n = int(input())

i, j, step = 1, 0, 1
while i <= n:
    while j < step and i <= n:
        print(i, end=' ')
        i, j = i + 1, j + 1
    print()
    step, j = step + 1, 0


# D
n = int(input())
total = 0

for i in range(n):
    num = input()
    for j in num: 
        total += int(j)

print(total)


# E
n = int(input())
total = 0

for i in range(n):
    presence = False
    while (sentence := input()) != "ВСЁ":
        if 'зайка' in sentence:
            presence = True
    total += presence

print(total)


# F
n = int(input())
num1 = int(input())

for i in range(n - 1):
    num2 = int(input())
    
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    
    num1 = num1 + num2

print(num1)


# G
n = int(input())
m = 3

for i in range(n):
    for j in range(m, 0, -1):
        print(f"До старта {j} секунд(ы)")
    m += 1
    print(f"Старт {i + 1}!!!")


# H
n = int(input())
mx_winner = ""
mx_num = 0

for i in range(n):
    winner = input()
    num = input()
    num_sum = 0
    for j in num:
        num_sum += int(j)
    if num_sum >= mx_num:
        mx_num = num_sum
        mx_winner = winner
    num_sum = 0

print(mx_winner)


# I
n = int(input())
res = ""

for i in range(n):
    num = input()
    mx = 0
    for j in num:
        if int(j) > mx:
            mx = int(j)
    res += str(mx)

print(int(res))


# J
n = int(input())

print("А Б В")

for x in range(1, n + 1):
    for y in range(1, n):
        for z in range(1, n - 1):
            if (x + y + z) == n:
                print(x, y, z)


# K
n = int(input())
total = 0

for i in range(n):
    num = int(input())
    res = True 
    if num == 1:
        res = False
    else:
        for j in range(2, int(num**0.5 + 1)):
            if num % j == 0:
                res = False
    if res:
        total += 1

print(total)


# L
n = int(input())
m = int(input())

length = len(str(n * m))

for i in range(0, n):
    for j in range(0, m):
        print(f"{(j + i * m + 1): >{length}}", end=' ')
    print()


# M
n = int(input())
m = int(input())

length = len(str(n * m))

for i in range(0, n):
    for j in range(0, m):
        print(f"{(i + j * n + 1): >{length}}", end=' ')
    print()


# N
n = int(input())
m = int(input())

length = len(str(n * m))

for i in range(0, n):
    if i % 2 == 0:
        for j in range(0, m):
            print(f"{(j + i * m + 1): >{length}}", end=' ')
    else:
        for j in range(m - 1, -1, -1):
            print(f"{(j + i * m + 1): >{length}}", end=' ')
    print()


# O
n = int(input())
m = int(input())

length = len(str(n * m))

for i in range(0, n):
    for j in range(0, m):
        if j % 2 == 0:
            print(f"{i + n * j + 1: >{length}}", end=' ')
        else:
            print(f"{n - i + n * j: >{length}}", end=' ')
    print()


# P
n = int(input())
m = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j: ^{m}}", end='')
        if j != n:
            print('|', end='')
    print()
    if i != n:
        print(f"{'':-^{(m + 1) * n - 1}}")


# Q
n = int(input())
total = 0

for i in range(n):
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
    
    if i_start >= i_end:
        total += 1

print(total)



# R
n = int(input())

i, j, step, width = 1, 0, 1, 0

while i <= n:
    width = 0
    while j < step and i <= n:
        width += len(str(i))
        if j != (step - 1) and i != n:
            width += 1
        i, j = i + 1, j + 1
    step, j = step + 1, 0

i, j, step = 1, 0, 1


while i <= n:
    res = ""
    while j < step and i <= n:
        res += str(i)
        if j != (step - 1) and i != n:
            res += " "
        i, j = i + 1, j + 1

    print(f"{res: ^{width}}")
    step, j = step + 1, 0

# S
n = int(input())

mx = n // 2 + n % 2
t = 0
if n % 2 == 0:
    t = 1

width = len(str(mx))

for i in range(1, n + 1):
    if i > mx:
        i = mx - (i - mx) + t
    for j in range(1, n + 1):
        if j > mx:
            j = mx - (j - mx) + t
        print(f"{min(i, j): >{width}}", end=' ')
    print()


# T
n = int(input())

res = 0
mx = 0
num = str(n)
num_sum = 0

for i in range(10, 1, -1):
    temp = n
    num = ""
    while temp != 0:
        num += str(temp % i)
        temp = temp // i

    num_sum = 0
    for j in num:
        num_sum += int(j)
    if num_sum >= mx:
        mx = num_sum
        res = i

print(res)
