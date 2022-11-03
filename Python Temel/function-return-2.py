x=7
def f(x):
    res=5
    res*=res
    if x%2==0:
        print("Sonuc:",res)
        return res
    else:
        print("Sonuc: ",res)
        return res+10
print(f(3))
print(f(4))

# Birden fazla değer döndürme

def power(x,y):
    return x**y
print(power(2,8))

def g(x):
    return 2*x,10*x,x-10

print(g(5))
a,b,c=g(5)
print("a=",a)
print("b=",b)
print("c=",c)

def h(k,n):
    return 2*k*n,(10**k)+n
print(h(4,5))

def O(c,d):
    e=c+2
    f=d+3
    return e,f
print(O(14,17))