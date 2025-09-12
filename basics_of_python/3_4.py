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

