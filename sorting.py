import random


def swap(a, b):
    temp = b
    b = a
    a = temp


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
            temp = tab[j]
            tab[j] = tab[j + 1]
            tab[j + 1] = temp
    length -= 1
print ""
print "Bubble sort:"
for i in tab:
    print i,
    plik.write(str(i) + ", ")
random.shuffle(tab)
print ""
print "Shuffle:"
for i in tab:
    print i,
