# A
n = int(input())
res = "YES"

for i in range(n):
    word = input()
    if word[0] not in "абв":
        res = "NO"

print(res)


# B
words = input()

for i in words:
    print(i)


# C
length = int(input())
num = int(input())

for i in range(num):
    sentence = input()
    if len(sentence) > length:
        print(sentence[:(length - 3)], end="...\n")
    else:
        print(sentence)


# D
while (sentence := input()) != "":
    if sentence.endswith("@@@"):
        continue
    elif sentence.startswith("##"):
        print(sentence[2:])
    else:
        print(sentence)


# E
sentence = input()
res = "YES"

for i, symbol in enumerate(sentence):
    if symbol != sentence[-i - 1]:
        res = "NO" 
        break

print(res)


# F
n = int(input())
res = 0

for i in range(n):
    sentence = input()
    res += sentence.count("зайка")

print(res)


# G
a, b = (int(i) for i in input().split())
print(a + b)


# H
n = int(input())

for i in range(n):
    sentence = input()
    res = sentence.find("зайка")
    if res != -1:
        print(res + 1)
    else:
        print("Заек нет =(")


# I
while (sentence := input()) != "":
    index = sentence.find("#")
    if index == -1:
        print(sentence)
    elif index == 0:
        continue
    else:
        print(sentence[:index])


# J
text = ""
while (word := input()) != "ФИНИШ":
    text += word.lower()

mx_count = 0
symbol = ""

for i in range(97, 1103):
    count = text.count(chr(i))
    if count > mx_count:
        symbol = chr(i)
        mx_count = count

print(symbol)


# K
n = int(input())
lst = []

for i in range(n):
    sentence = input()
    lst += [sentence]

word = input()

for i in lst:
    if i.lower().find(word.lower()) != -1:
        print(i)


# L
lst = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

n = int(input())

for i in range(n):
    print(lst[i % 5])


# M
n = int(input())
lst = []

for i in range(n):
    lst += [int(input())]

power = int(input())

for i in lst:
    print(i**power)


# N
lst = input().split()
power = int(input())

for i in lst:
    print(int(i)**power, end=' ')


# O
lst = input().split()
prev = int(lst[0])
nod = ""

for i in lst:
    num1 = prev
    num2 = int(i)
    
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    
    nod = num1 + num2
    prev = nod

print(nod)


# P
fix_l = int(input())
n = int(input())

for i in range(n):
    string = input()
    length = len(string)

    if length <= fix_l:
        if (fix_l - length) > 3 or (fix_l - length) == 0:
            fix_l -= length
            print(string)
        else:
            print(string[:fix_l - 3], end="...")
            fix_l = 0
    elif fix_l != 0:
        print(string[:fix_l - 3], end="...")
        fix_l = 0


# Q
string = input()
lst = string.lower().split()
sentence = []

for i in lst:
    for j in i:
        sentence += j

res = "YES"
for i, symbol in enumerate(sentence):
    if symbol != sentence[-i - 1]:
        res = "NO" 
        break

print(res)


# R
chars = input()
count = 0
for i in chars:
    if count == 0:
        print(i, end=" ")
        count += 1
        prev_char = i
    elif prev_char == i:
        count += 1
    else:
        print(count)
        print(i, end=" ")
        prev_char = i
        count = 1
        prev_char = i
print(count)


# S
lst = input().split()
stek = []

for i in lst:
    if i.isdigit():
        stek += [int(i)]
    elif i == "+":
        res = stek[-1] + stek[-2]
        stek.pop()
        stek.pop()
        stek += [res]
    elif i == "-":
        res = stek[-2] - stek[-1]
        stek.pop()
        stek.pop()
        stek += [res]
    elif i == "*":
        res = stek[-1] * stek[-2]
        stek.pop()
        stek.pop()
        stek += [res]

print(stek[-1])


# T
lst = input().split()
stek = []

for i in lst:
    if i.isdigit():
        stek += [int(i)]
    elif i == "+":
        res = stek[-1] + stek[-2]
        stek.pop()
        stek.pop()
        stek += [res]
    elif i == "-":
        res = stek[-2] - stek[-1]
        stek.pop()
        stek.pop()
        stek += [res]
    elif i == "*":
        res = stek[-1] * stek[-2]
        stek.pop()
        stek.pop()
        stek += [res]
    elif i == "/":
        res = stek[-2] // stek[-1]
        stek.pop()
        stek.pop()
        stek += [res]
    elif i == "~":
        res = -stek[-1]
        stek.pop()
        stek += [res]
    elif i == "!":
        res = stek[-1]
        stek.pop()
        res_f = 1
        for i in range(2, res + 1):
            res_f *= i 
        stek += [res_f]
    elif i == "#":
        res = stek[-1]
        stek += [res]
    elif i == "@":
        res = [stek[-2], stek[-1], stek[-3]]
        stek.pop()
        stek.pop()
        stek.pop()
        stek += res

print(stek[-1])
