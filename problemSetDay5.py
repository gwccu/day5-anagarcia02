# File name: problemSetDay5.py

# problem 1

for a in range(5):
    print(a)

for b in range(5, 8):
    print(b)

for c in range(5, 20, 3):
    print(c)

for d in range(0, 35, 5):
    print(d)

# problem 2

a = 0
while a < 5:
    print(a)
    a += 1

b = 5
while b < 8:
    print(b)
    b += 1

c = 5
while c < 20:
    print(c)
    c += 3

d = 0
while d < 35:
    print(d)
    d += 5

# Using a for loop is easier because it requires less calculations.
# Also, it can get tricky because you can get caught in infinite loops.

# Problem 3

stars = "*"
for s in range(1, 9, 2):
    print(str(stars) * s)

# Problem 4

for n in range(1500, 1715, 5):
    if n % 7 == 0:
        print(n)

# Problem 5

n = input("Pick a number.")
box = "*"

if n >= 1:
    for n in range(n):
        print(box * n)
