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