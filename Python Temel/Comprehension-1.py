squares=[]

for i in range(1,11):
    squares.append(i*i)
print(squares)    


squares1=[i*i for i in range(1,11)]

print(squares1)

def cube(x):
    return x*x*x

cubes=[cube(x) for x in range(1,11)]
print(cubes)

odd_squares=[]

for e in squares:
    if e%2==1:
        odd_squares.append(e)
print(odd_squares)

odd_squares1=[y for y in squares if y%2==1]
print(odd_squares1)


t=int(input())

def is_odd(t):
    if t%2==0:
        return False 
    if t%2==1:
        return True
# Veya 
def is_odd(t):
    if t%2==0:
        return False
    return True
#Veya
def is_odd(t):
    if t%2==0:
        return False
    else:
        return True
#print(is_odd(t))


odd_squares2=[k for k in squares if is_odd(k)]
print(odd_squares2)

print("-----------is_even-------------")
def even(n):
    if n&2==0:
        return True
    if n%2==1:
        return False
print(even(5))

print("Dizimiz:",squares1)

even_squares=[a for a in squares1 if even(a)]
print(even_squares)
