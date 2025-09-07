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
        dct[j] = dct.get(j, []) + [text[0]]

porridge = input()
if porridge not in dct:
    print("Таких нет")
else:
    print("\n".join(sorted(dct.get(porridge))))


# I
dct = {}

while (text := input()) != "":
    lst = text.split()
    for j in lst:
        dct[j] = dct.get(j, 0) + 1

for i in dct:
    print(i, dct[i])


# J
dct = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "Kh",
    "Ц": "Tc",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ъ": "",
    "Ы": "Y",
    "Ь": "",
    "Э": "E",
    "Ю": "Iu",
    "Я": "Ia",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "tc",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "iu",
    "я": "ia"
}

text = input()

for i in text:
    if i in dct:
        print(dct[i], end="")
    else:
        print(i, end="")


# K
n = int(input())
surnames = set()
repeat = []

for i in range(n):
    text = input()

    if text in surnames:
        repeat += [text]

    surnames.add(text)

print(len(repeat) + len(set(repeat)))


# L
n = int(input())
surnames = {}

for i in range(n):
    text = input()
    
    surnames[text] = surnames.get(text, 0) + 1 

not_presence = True
for i in sorted(surnames.keys()):
    if surnames[i] > 1:
        print(i, '-', surnames[i])
        not_presence = False

if not_presence:
    print("Однофамильцев нет")


# M
n = int(input())
meals = set()

for i in range(n):
    meal = input()
    meals.add(meal)

m = int(input())

for i in range(m):
    count = int(input())
    for j in range(count):
        meal = input()
        meals.discard(meal)

lst = sorted(list(meals))
if len(lst) != 0:
    for i in lst:
        print(i)
else:
    print("Готовить нечего")


# N
n = int(input())
ingredients = set()

for i in range(n):
    ingredient = input()
    ingredients.add(ingredient)

m = int(input())
meals = []

for i in range(m):
    meal = input()
    count = int(input())
    m_ingredients = set()
    for j in range(count):
        ingredient = input()
        m_ingredients.add(ingredient)
    if m_ingredients <= ingredients:
        meals += [meal]

meals.sort()
if len(meals) != 0:
    for i in meals:
        print(i)
else:
    print("Готовить нечего")


# O
lst = input().split()
res = []

for i in lst:
    number = int(i)
    b_num = bin(number)[2:]

    b_dict = {
        "digits": len(b_num),
        "units": 0,
        "zeros": 0
    }

    for symbol in b_num:
        if symbol == "1":
            b_dict["units"] += 1
        else:
            b_dict["zeros"] += 1

    res += [b_dict]

print(res)


# P
res = set()

while (sentence := input()) != "":
    words = sentence.split()

    while "зайка" in words:
        ind = words.index("зайка")

        if 0 <= ind + 1 < len(words):
            res.add(words[ind + 1])

        if 0 <= ind - 1 < len(words):
            res.add(words[ind - 1])

        words = words[ind + 1:]

res = sorted(list(res))
print("\n".join(res))


# Q
pairs = {}

while (sentence := input()) != "":
    names = sentence.split()

    pairs[names[0]] = pairs.get(names[0], set())
    pairs[names[0]].add(names[1])
    pairs[names[1]] = pairs.get(names[1], set())
    pairs[names[1]].add(names[0])

for name in sorted(pairs):
    print(f"{name}: ", end="")
    res = set()

    for name2 in sorted(pairs[name]):
        res = res | pairs[name2]

    res.discard(name)
    res = res - pairs[name]
    res = sorted(list(res))

    print(", ".join(res))


# R
n = int(input())
coordinates = {}

for i in range(n):
    x, y = input().split()
    x, y = f"{x:0>9}", f"{y:0>9}"
    key = f"{x[:-1]} {y[:-1]}"

    coordinates[key] = coordinates.get(key, 0) + 1

print(max(coordinates.values()))


# S
n = int(input())
res = set()
repeat = set()

for i in range(n):
    text = (input() + ',').split()[1:]

    text_single = set(text)

    for j in text_single:
        if j[:-1] in res:
            repeat.add(j[:-1])
        res.add(j[:-1])

print('\n'.join(sorted(list(res - repeat))))


# T
nums = sorted(list(set([int(i) for i in input().split('; ')])))
dct = {}

for num in nums:
    p = True
    for j in range(2, num + 1):
        if num % j == 0:
            dct[j] = dct.get(j, set())
            dct[j].add(num)
            p = False
    if p:
        dct[num] = dct.get(num, set())
        dct[num].add(num)

for num in nums:
    single_res = set()
    single_not_res = set()
    for j in dct:
        if num not in sorted(dct[j]):
            single_res = single_res | dct[j]
        else:
            single_not_res = single_not_res | dct[j]
    res = [str(i) for i in sorted(list(single_res - single_not_res))]
    if len(res) != 0:
        print(num, '-', ', '.join(res))
