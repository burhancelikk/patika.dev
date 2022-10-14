
notlar=[90,72,81,77]

for e in notlar:
    print(e,type(e))

print("------------")  

t=0
for i in notlar:
    t+=i
    print(t)
ortalama=t/len(notlar)
print(ortalama)

print("------------")

k=0
for y in range(len(notlar)):
    k+=notlar[y]
    print(notlar[y])
ortalama=k/len(notlar)
print(ortalama)

print("------------")

i=0
print(notlar)
for z in notlar:
    print(z)
    z+=10
    print(z)
    notlar[i]+=10
    i+=1
    print(notlar)

print("------------")

for i in range(len(notlar)):
    notlar[i]+=5
    print(notlar)

print("------------")

