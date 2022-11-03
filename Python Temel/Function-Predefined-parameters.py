def hello(end,start="Hello"):
    print(start+" "+end)
hello("Denis")

def power(x,y=1): #power(y=1,x) şeklinde yazamıyoruz
    return x**y
print(power(5,2)) 
print(power(5)) # y belirtilmediği sürece y=1 alınacak.

def f(x,y=2,z=-2):
    return x+y+z

print(f(5))      # x=5 y=2 z=-2
print(f(5,2))    # x=5 y=2 z=-2
print(f(5,2,-3))  # x=5 y=2 z=-3

def h(x,y=True):
    if x%2==0:
        y=False
        return y
    return y

print(h(8,9))
print(h(9,6))
print(h(5,True))
print(h(5,False))
