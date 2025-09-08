# A
[i ** 2 for i in range(a, b + 1)]


# B
[i ** 2 for i in range(a, b + (1 if a < b else -1), 1 if a < b else -1)]


# C
[i for i in range(a, b + (1 if a < b else -1), 1 if a < b else -1) if i % d == 0]


# D
set(i for i in numbers if i % 2 != 0)


# F
[len(i) for i in sentence.split()]


# G
"".join([i for i in text if i.isdigit()])


# H
"".join([i[0].upper() for i in string.split()])


# I
" - ".join([str(i) for i in sorted(set(numbers))])


# J
[i for i in words.split() if len([j for j in i.lower() if j in "аяуюоёэеиыaeiouy"]) >= 3]


# K
set(i for i in numbers if numbers.count(i) == 1)


# L
max([j * i for i in numbers for j in numbers if i != j])


# M
min([(sum(data[i]), i) for i in data])[1]


# N
{i for i in data if len(set(data[i])) < len(data[i])}


# O
{i: (text.lower().count(i)) for i in sorted(set(text.lower())) if i.isalpha()}


# P
"".join(i[0] * i[1] for i in rle)


# Q
[[i*j + j for j in range(1, n + 1)] for i in range(n)]


# R
{i: [j for j in range(1, i + 1) if i % j == 0] for i in sorted(numbers)}


# S
{i for i in numbers if [j for j in range(2, i) if i % j == 0] == [] and i != 1}


# T
set(sorted(set((word1, word2) for i, word1 in enumerate(sorted(set(text.split())))
    for j, word2 in enumerate(sorted(set(text.split()))[i:]) 
    if word1 != word2 and len(set(word1) & set(word2)) > 2)))
