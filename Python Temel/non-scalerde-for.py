for i in range(1,7):
    print("iteration:",i)

notlar=[80,90,56,78]
t=0
for i in range(len(notlar)):
    t+=notlar[i]
ortalama=t/len(notlar)
print("ortalama:",ortalama)

print("------------")

for e in notlar:
    print(e)
    e+=10
    print(e)
print(notlar)

print("----------------------")
print(notlar)
for e in range(len(notlar)):
    notlar[e]+=5
print(notlar)

for i in range(len(notlar)):
    if i==1:
        continue
    notlar[i]+=5
print(notlar)

print("----------------------")

x=int(input("Hangi sayıyı kontrol edeyim?:"))

l=[2,3,40,100,10,1]

for e in l:
    print(e)
    if e==x:
        print("Buldum!!")
        break

print("----------------------")

d={"student_1":[80,90],"student_2":[85,83],"student_3":[92,97]}

for k in d:
    print(k)

for k in d:
    v=d[k]
    print(v)
    print(k)
    print(k,":",v)

for v in d.values():
    print(v)

b={"A":66,"B":89,"C":70}

for x in b:
    value = b[x]
    if value > 85:
        print(x,value)

for k,v in b.items():
    print("key degeri:",k,"value degeri:",v)

for w in b.items():
    print(w)

print("\n")
print("----------------------")

from collections import defaultdict
d=defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("Language")
for i in d.items():
    print(i)

