a=2
def f(x):
    x=4
    return x

print(f(a),a)

print("\n")

l=["elma","portakal","armut"]
m=l
def f(y):
    y[0]="limon"
    return y
f(l)
print(m)

