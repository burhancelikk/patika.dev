l=[1,2,3,4]

def apply(l,f):
    n=len(l)
    for i in range(n):
        l[i]=f(l[i])
        
def kare(x):
    return x**2


print(apply(l,kare))