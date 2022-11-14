def kare(x):
    return x**2
a=kare
print(a(5))


def f2(x,f):
    return f(x)+4

print(f2(3,kare))


def f3(x):
    return x**5

print(f2(2,f3))