# A
string_set = set(input())

for i in string_set:
    print(i, end="")


# B
string_set_1 = set(input())
string_set_2 = set(input())

print("".join(string_set_1 & string_set_2))


# C
n = int(input())
string_set = set()

for i in range(n):
    lst = input().split()
    string_set = string_set | set(lst)

print("\n".join(string_set))


# D
n = int(input())
m = int(input())
n_set, m_set = set(), set()

for i in range(n):
    n_set.add(input())

for j in range(m):
    m_set.add(input())

count = len(n_set & m_set)

if count == 0:
    print("Таких нет")
else:
    print(count)


# E
n = int(input())
m = int(input())
all_set = set()

for i in range(n + m):
    child = input()
    if child in all_set:
        all_set.remove(child)
    else:
        all_set.add(child)

count = len(all_set)
if count == 0:
    print("Таких нет")
else:
    print(count)


# F
n = int(input())
m = int(input())
all_set = set()

for i in range(n + m):
    child = input()
    if child in all_set:
        all_set.remove(child)
    else:
        all_set.add(child)

count = len(all_set)
if count == 0:
    print("Таких нет")
else:
    lst = "\n".join(sorted(list(all_set)))
    print(lst)


# G
dct = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

text = input().lower()

for i in text:
    if i != " ":
        print(dct[i], end=" ")
    else:
        print()


# H
n = int(input())

dct = {}

for i in range(n):
    text = input().split()

    for j in text[1:]:
        dct[j] = dct.get(text[0], default) + text[0]

porridge = input()

print(dct.get(porridge))
