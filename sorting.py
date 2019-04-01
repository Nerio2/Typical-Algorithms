import random


def swap(a, b):
    temp = b
    b = a
    a = temp


tab = range(100)
for i in range(100):
    tab[i] = random.randint(1, 100)
    print tab[i],

""" bubble sort: """
for i in range(99):
    for j in range(99):
        if tab[j] > tab[j + 1]:
            temp = tab[j]
            tab[j] = tab[j + 1]
            tab[j + 1] = temp
print "Bubble sort:"
for i in tab:
    print i,
random.shuffle(tab)
print ""
for i in tab:
    print i,
