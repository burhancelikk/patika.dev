def weird():
    return 5
a=weird()
print(a)

def square(x):
    res=x*x
    print("square of " + str(x) + ": " + str(res))
    return res
    print("square of" + str(x) + ": " + str(res)) # return den sonra print fonksiyonunu okumaz
print(square(4)+5)

def f(x):
    res=x*x
    if x%2==0:
        return res #sayı çift ise karesini alacam
    else:
        return res +10 #sayı tek ise karesini alıp 10 ekleyecem

print(f(int(input("Çift veya Tek Sayi Giriniz: "))))


def g(x):
    kare=x*x
    for _ in range(10):
        kare+=20
        return kare

print(g(int(input("Bir sayi giriniz: "))))

def h(x):
    kare=x*x
    for _ in range(10):
        kare+=20
    return kare

print(h(int(input("Bir sayi giriniz: "))))
print(h(10)+20)

def k(x):
    l=[]
    kup=x**3
    for _ in range(10):
        kup+=20
        l.append(kup)
    return l

print(k(int(input("Lutfen kupu alinip for 'a girecek sayiyi giriniz: "))))


# Void Fonksiyonlar (Değer Döndürmeyen Fonksiyonları)

def m(x):  # deger dondurmuyor o yüzden void
    x=2
print(m(5))

def selam(n): # Deger dondurdugu icin void degil
    kupi=n**3
    print(n,"'in/un kupu: ", n**3)
    return kupi
print(selam(int(input("Kupu alinacak: "))))

