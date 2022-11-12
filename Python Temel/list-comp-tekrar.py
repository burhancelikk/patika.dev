squares1=[]

for i in range(1,11):
    squares1.append(i*i)
print(squares1)


squares2=[i*i for i in range(1,7)]
print(squares2)


cubes1=[j**3 for j in range(4)]
print(cubes1)


even_squares1=[k for k in squares1 if k%2==0]
odd_squares1=[e for e in squares1 if e%2==1]
print(even_squares1)
print(odd_squares1)

print("--------------------------------------")

def is_odd(x):
    if x%2==0:
        return False
    else:
        return True

def is_even(x):
    if x%2==0:
        return True
    else:
        return False

odd_squares2=[d for d in squares1 if is_odd(d)]
print(odd_squares2)

print("--------------------------------------")

def empty(x):
    if x%2==0:
        False
    if x%2==1:
        False

empty_squares=[f for f in squares1 if empty(f)]
print(empty_squares)

print("--------------------------------------")

weird_squares=[e if e%2==0 else -1 for e in squares1]
print(weird_squares)

ultra_weird_squares=[c if c%2==0 else -1 for c in squares1 if is_even(c)]
print(ultra_weird_squares)

print("--------------------------------------")

squares_dict={b:b*b for b in range(1,11)}
print(squares_dict)

print("--------------------------------------")

m=[[j for j in range(7)] for _ in range(5)]
print(m)

print("--------------------------------------")

n=[]
for x in range(10,13):
    n.append(x)
print(n)

o=[]
for y in range(13,15):
    o.append(y)
print(o)

p=[]
for z in range(15,19):
    p.append(z)
print(p)

tlist=[]
tlist.append(n)
tlist.append(o)
tlist.append(p)
print(tlist)

print("--------------------------------------")

for l in tlist:
    print(l)

print("\n")

new_m=[]
for l in tlist:
    print(l)
    for e in l:
        new_m.append(e)
        print(e)

print("\n")

flatten_m=[e for l in tlist for e in l]
print(flatten_m)

print("--------------------------------------")


flatten_n=[e for l in tlist for e in l if e%2==0]
print(flatten_n)
