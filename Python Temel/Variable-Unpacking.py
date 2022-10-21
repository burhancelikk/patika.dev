x,y=(5,6)
print(x)
print(y)
print(x,y)

a,b,c=(4,7,8)
print(a)
print(b)
print(c)
print(a,b,c,x,y)

#Kullanmayacağımız değişkene _ diyebiliriz.
x1,_=(7,8)

x,y,*z=(4,7,11,16,5,0)
print(x)
print(y)
print(z)
print("z'nin sinifi => ",type(z))

# Geriye kalanları kullanmayacaksak *_ şeklinde tanımlayabiliriz.
x,y,*_=(4,7,11,12,13)

x,y,*z,t=(4,7,11,5,89,0,2)
print(x,y,t)
print(z,type(z))

#it will give an error
x,*y,*t=(4,7,11,4) # şeklinde bir kullanım hatalıdır.
