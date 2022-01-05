import math


def Mystery(a, f, l):
    if f == l:
        return a[f]
    m = math.floor((f + l) / 2)
    x = Mystery(a, f, m)
    c = 0
    i = f
    while i <= l:
        if a[i] == x:
            c = c + 1
        i = i + 1
    if c > (l-f+1)/2:
        return x
    return Mystery(a, m + 1, l)

a = [1, 10, 2, 3, 4, 5, 6, 7]
f = 1
l = 4
print(Mystery(a, f, l))
