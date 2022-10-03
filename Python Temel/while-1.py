x=int(input("Bir sayı girin:"))

while x<0:
    print("Sayı negatiftir.")
    x=int(input("Lütfen negatif olmayan bir sayı girin:"))
if x==0:
    print("Sayınız",x)
else:
    print("Sayınız pozitif ve",x)