# A
text = input().split()

for i, word in enumerate(text, 1):
    print(f"{i}. {word}")


# B
lst1 = input().split(', ')
lst2 = input().split(', ')

for (i, j) in zip(lst1, lst2):
    print(f"{i} - {j}")


# C
from itertools import count


a, b, step = (float(i) for i in input().split())

for i in count(a, step):
    if i > b:
        break
    print(i)


# D
from itertools import accumulate

text = [i + " " for i in input().split()]

for i in accumulate(text):
    print(i)


# E
from itertools import chain 


mom_list = input().split(", ")
dad_list = input().split(", ")
d_list = input().split(", ")

for i, word in enumerate(sorted(chain(mom_list, dad_list, d_list)), 1):
    print(f"{i}. {word}")


# F
from itertools import product


nominal = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
           'валет', 'дама', 'король', 'туз']
mast = ['пик', 'треф', 'бубен', 'червей']

wth = input()
mast.remove(wth)

res = list(product(nominal, mast))

for i, j in res:
    print(i, j)


# G
from itertools import combinations
n = int(input())

names = []

for i in range(n):
    names += [input()]

res = combinations(names, 2)

for i, j in res:
    print(f"{i} - {j}")


# H
from itertools import cycle

m = int(input())

porridge = []

for i in range(m):
    porridge += [input()]

n = int(input())

for i, j in enumerate(cycle(porridge)):
    if i == n:
        break
    print(j)


# I
from itertools import product


n = int(input())

res = list(product(range(1, n + 1), repeat=2))

for i, j in res:
    print(i * j, end=' ') 
    if j == n:
        print()


# J
from itertools import product


n = int(input())

print("А Б В")
for i, j in list(product(range(1, n + 1) repeat = 2)):
    if n - i - j > 0:
        print(i, j, n - i - j)


# K
from itertools import product


n = int(input())
m = int(input())

res = product(range(n), range(1, m + 1))
width = len(str(n * m))

for i, j in res:
    print(f"{i * m + j: >{width}}", end=' ')
    if j % m == 0:
        print()


# L
n = int(input())

lst = []

for i in range(n):
    lst += input().split(", ")

for i, word in enumerate(sorted(lst), 1):
    print(f"{i}. {word}")


# M
from itertools import permutations 


n = int(input())
names = []

for i in range(n):
    names += [input()]

res = sorted(permutations(names, n))

for i in res:
    print(", ".join(i))


# N
from itertools import permutations 


n = int(input())
names = []

for i in range(n):
    names += [input()]

res = sorted(permutations(names, 3))

for i in res:
    print(", ".join(i))


# O
from itertools import permutations 


n = int(input())

lst = []

for i in range(n):
    lst += input().split(", ")

res = sorted(permutations(lst, 3))

for i in res:
    print(" ".join(i))


# P
from itertools import product, combinations


nominal = ["10", "2", "3", "4", "5", "6", "7", "8", "9",
           "валет", "дама", "король", "туз"]
suit = ["бубен", "пик", "треф", "червей"]
suit_cases = {"буби": "бубен",
              "пики": "пик",
              "трефы": "треф",
              "черви": "червей"
              } 

main_suit = suit_cases[input()]
wtht_nominal = input()
nominal.remove(wtht_nominal)


res = combinations(product(nominal, suit), 3)

res = [i for i in res if main_suit in str(i)][:10]

for ((x1, y1), (x2, y2), (x3, y3)) in res:
    print(f"{x1} {y1}, {x2} {y2}, {x3} {y3}")


# Q
from itertools import product, combinations


nominal = ["10", "2", "3", "4", "5", "6", "7", "8", "9",
           "валет", "дама", "король", "туз"]
suit = ["бубен", "пик", "треф", "червей"]
suit_cases = {"буби": "бубен",
              "пики": "пик",
              "трефы": "треф",
              "черви": "червей"
              } 

main_suit = suit_cases[input()]
wtht_nominal = input()
nominal.remove(wtht_nominal)


comb = combinations(product(nominal, suit), 3)
prev = input()
res = ""
flag = 1

for i in comb:
    if flag and main_suit in str(i):
        maybe_prev = f"{i[0][0]} {i[0][1]}, {i[1][0]} {i[1][1]}, {i[2][0]} {i[2][1]}"
        if maybe_prev == prev:
            flag = 0
    elif not flag and main_suit in str(i):
        res = f"{i[0][0]} {i[0][1]}, {i[1][0]} {i[1][1]}, {i[2][0]} {i[2][1]}"
        break

print(res)


# R
from itertools import product


string = input() + " "
comb = product([0, 1], [0, 1], [0, 1])

print("a b c f")
for (x, y, z) in comb:
    res = string.replace('a ', f"{x} ").replace('b', str(y)).replace('c', str(z))
    print(x, y, z, int(eval(res)))


# S
from itertools import product


string = input()
variables = sorted(set(i for i in string if i.isupper()))
n = len(variables)

comb = product([0, 1], repeat=n)


print(" ".join(variables), end=" F\n")
for i in comb:
    res = string
    for ind, j in enumerate(i):
        print(j, end=" ")
        res = res.replace(variables[ind], str(j))
    res = res.replace("~", "==")
    print(res)

    while "->" in res:
        ind = res.index("->")
        res = list(res)
        res.insert(0, "not ")
        res = "".join(res)
        res = res.replace("->", "or", count=1)
        print(res)

    print(int(eval(res)))
