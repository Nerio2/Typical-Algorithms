"""
Algorithm specification:
digital alignment of a natural number n>=10,
depends on reducing differences between next digits of a given number.
In the following way:
- the digit of unity remains unchanged,
- if the digit of ten is bigger than digit of unity, we reduce it by one,
On the other hand, if the digit of ten i lower than digit of unity, we increase it by one,
if they are equal we don't change anything
-we analogically compare the next digits until we reach the end of the number

!!! Algorithm have to be created with operations on numbers not on characters !!!
"""

while True:
    number = input("give me the number bigger than 9:\n")
    if int(number) >= 10:
        break
result = 0
reszta = number % 10
result += reszta
i = 1
while number > 9:
    number /= 10
    if number % 10 > reszta:
        number -= 1
    else:
        if number % 10 < reszta:
            number += 1
    i *= 10
    reszta = number % 10
    result += reszta * i
print result
