a = 1
r = 0.5
s = 0
k = 0

while True:
    s += a*r**k
    k += 1
    print(s, end = " ")
    if (2-s) < 0.000001 :
        break