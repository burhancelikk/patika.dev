l=[(1,2),(10,20)]

for e in l:
    print(e)

print("l[0]=(1,2)",type(l[0]))

for e in l:
    a,b=e
    print(a)
    print(b)
    print("******")

for a,b in l:
    print("tuple'ın ilk elemanı",a)
    print("tuple'ın ikinci elemanı",b)
    print("----------------")

# enumare() bize (index,element) olarak verecek

adlar=['Tyler','Blake','Cory','Cameron']

for e in adlar:
    print(e)

print("\n")

for i,e in enumerate(adlar):
    print(i,"inci eleman:",e)

print("\n")

for i,e in enumerate(adlar,start=1):
    print(i,"indexindeki eleman:",e)

print("\n")

for i,e in enumerate(adlar,start=10):
    print(i,"lokasyonunda bulunan eleman:",e)

print("--------------------")

# zip() farklı yapıların içinde paralel iteration

ogrenci=["ogrenci-1","ogrenci-2","ogrenci-3"]
notlar=[87,55,93]

for i in range(len(ogrenci)):
    s=ogrenci[i]
    g=notlar[i]
    print(s,g)

for s,g in zip(ogrenci,notlar):
    print(s,g)


#zip() örnek

# Her ayki karı hesapalamak

satis=[3500.00,76300.00,67.200]
maliyet=[56700.00,21900.00,12100.00]

for i in range(len(maliyet)):
    s=satis[i]
    c=maliyet[i]
    kar=s-c
    print(f'Total profit:{kar}')

print("---------veya----------")

for s,c in zip(satis,maliyet):
    kar=s-c
    print(f'Total profit:{kar}')

# zip() ile Dictionary Yaratmak

keys=['isim','soyisim','ulke','meslek']
values=['Denis','Walker','Turkey','data scientist']

d={}
for k,v in zip(keys,values):
    d[k]=v
print(d)

#Veya
print("-------veya--------")

b={}
for i in range(len(keys)):
    k=keys[i]
    v=values[i]
    b[k]=v
print(b)