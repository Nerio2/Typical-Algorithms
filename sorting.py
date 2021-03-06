import random


def swap(a, b):
    temp = b
    b = a
    a = temp
    return a, b


plik = open('results.txt', 'w')
tab = range(100)
length = len(tab) - 1
plik.write("Shuffled tab:\n")
for i in range(100):
    tab[i] = random.randint(1, 100)
    plik.write(str(tab[i]) + ", ")
    print tab[i],

""" bubble sort: """
plik.write("\nBubble sort:\n")
for i in range(99):
    for j in range(length):
        if tab[j] > tab[j + 1]:
            tab[j], tab[j + 1] = swap(tab[j], tab[j + 1])
    length -= 1
print ""
print "Bubble sort:"
for i in tab:
    print i,
    plik.write(str(i) + ", ")
random.shuffle(tab)
print ""

"""Insertion Sort"""
plik.write("\nInsertion Sort\n")
print "\nInsertion Sort\n"
for i in range(99):
    if tab[i + 1] < tab[i]:
        for j in range(i + 1):
            k = i - j
            if tab[k + 1] < tab[k]:
                tab[k + 1], tab[k] = swap(tab[k + 1], tab[k])
for i in tab:
    plik.write(str(i) + ", ")
    print i,
random.shuffle(tab)

print "\nSelection sort"
for i in range(50):
    max = 99 - i
    min = i
    for j in range(100 - 2 * i):
        k = i + j
        if tab[k] > tab[max]:
            max = k
        if tab[k] < tab[min]:
            min = k
    tab[i], tab[min] = swap(tab[i], tab[min])
    tab[(99 - i)], tab[max] = swap(tab[(99 - i)], tab[max])

for i in tab:
    print i,
