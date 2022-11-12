sayilar = [3,5,6,7]

def karesi(sayi):
    return sayi**2

empty_list=[]
for sayi in sayilar:
    empty_list.append(karesi(sayi))

print(empty_list)
print("---------------")

sonuc0=map(karesi,sayilar)
print(list(sonuc0))

sonuc1=map(lambda x:x**3,sayilar)
print(list(sonuc1))

print("---------------")


sayilar1=[3,5,6,7]
sayilar2=[1,15,4,9]

def kucuk(x,y):
    if x<y:
        return x
    else:
        return y

sonuc2=map(kucuk,sayilar1,sayilar2)
print(list(sonuc2))

print("---------------")

n=int(input())
arr=map(int,input().split())

print(list(arr))
print(n)
print(arr)