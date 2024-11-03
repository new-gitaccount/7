i = 1
while i <= 10:
    print(i, end=", " if i < 10 else "")
    i += 1

son = int(input("Sonni kiriting: "))
i = son
while i >= 1:
    print(i, end=", " if i > 1 else "")
    i -= 1

son = int(input("Sonni kiriting: "))
i = 1
yigindi = 0

while i <= son:
    yigindi += i
    i += 1

print(yigindi)

yigindi = 0

while True:
    son = int(input("Sonni kiriting (0 kiritilganda tugaydi): "))
    if son == 0:
        break
    yigindi += son

print(yigindi)
