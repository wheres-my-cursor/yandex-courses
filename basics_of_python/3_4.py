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
lst = [i for i in range(1, n + 1)]

res = list(product(lst, lst))

for i, j in res:
    print(i * j, end = ' ') 
    if j == n:
        print()


# J
