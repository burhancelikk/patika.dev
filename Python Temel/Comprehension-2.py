'''
squares=[]

for i in range(1,11):
    squares.append(i*i)
print(squares)
'''

squares=[i*i for i in range(1,11)]
print(squares)

def is_even(x):
    if x%2==0:
        return True
    if x%2==1:
        return False
# even_squares=[c for in squares if c&2==0]
even_squares=[c for c in squares if is_even(c)]
print(even_squares)
print(squares)
print("--------------------------")
# squares dizisinin içindeki elemanları sırasıyla if döngüsünde kontrol et.
# Koşul doğruysa(yani kalan 0 ise)(True) diziye yazdır.
# Koşul yanlışsa(yani kalan 0 dan farklı ise)(False) -1 yazdır.
weird_squares=[e if e%2==0 else -1 for e in squares]

print(weird_squares)
print(squares)


weird_squares1=[]

for k in squares:
    if k%2==0:
        weird_squares1.append(k)
    else:
        weird_squares1.append(-1)

print(weird_squares1)
print(squares)

print("---------------------------")

# ultra_wierd_squares=[e for e in squares if is_even(e)]
# Yukarıdaki gibi yazmamız yeterli olurdu.
# if koşul tarafını hiç okumayacak.
# for döngüsü içerisinde true ya da false döndürerek e yazdırıyor
                     #                       ############    #########
ultra_weird_squares=[e if e%2==0 else -1 for e in squares if is_even(e)]
print(ultra_weird_squares)