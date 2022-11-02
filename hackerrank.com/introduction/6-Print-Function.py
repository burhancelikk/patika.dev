import functools
# I.YONTEM
n=int(input("1<= n <=150 n degeri giriniz! (I.Yontem): "))
if 1<=n<=150:
    for i in range(1,n+1):
        print(i,end="")
else:
    print("lutfen 1<= n <=150 deger araliginda giriniz!")
    n=int(input())

# II.YONTEM
x=int(input("\n1<= x <=150 n degeri giriniz! (II.Yontem): "))
if 1<=x<=150:
    print(*range(1,x+1), sep='')
else:
    x=int(input("1<= x <=150 deger araliginda giriniz:"))

# III.YONTEM
# Sınırlama konulacak!!!  1<= x <=150
print(functools.reduce(lambda x, y: x+y, map(lambda x: str(x+1), range(int(input("Sayi Gir:"))))))

# IV.YONTEM
list(map(lambda k: print(k,end=''), [k for k in range(1,int(input("Bir Sayi gir: "))+1)]))
