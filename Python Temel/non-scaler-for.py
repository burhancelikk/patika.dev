
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
# break
for n in range(len(notlar)):
    print(notlar[n])
    break

print("------------")
#break
for c in range(len(notlar)):
    print(notlar[c])
    break

print("------------")
#continue
print(notlar)
for i in range(len(notlar)):
    if i==1:
        continue
    notlar[i]+=5
print(notlar,"2. ogrencinin notu artmadı")

print("------------")

x=int(input("Hangi sayiyi kontrol edeyim?"))
sayi=[1,2,3,4,5,6,7,8,9]

for s in sayi:
    print(s)
    if s==x:
        print("Buldum!")
        break

print("------------")

d={"student_1":[98,89],"student_2":[80,83],"student_3":[72,71]}

for j in d: # iterasyon keyword ler üzerinden oluyor.
    print(j) 

for j in d:  # iterasyon value ler üzerinden oluyor.
    d_val=d[j]
    print(d_val)

for j in d.values(): # iterasyon value ler üzerinden oluyor.
    print(j)

print("------------")

d_vize={"student_1":98,"student_2":80,"student_3":72,"student_4":86}

for j in d_vize:
    d_val=d_vize[j]
    if d_val>85:
        print(j,":",d_val)

print("------------")

for j,d_val in d_vize.items():
    print("keyword degeri:",j,"\nvalue degeri  :",d_val)

for p in range(1,9,3): # 1 'den 9'a kadar(9 hariç) 3'er 3'er say
    print(p)
