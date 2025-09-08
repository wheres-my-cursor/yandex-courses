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
