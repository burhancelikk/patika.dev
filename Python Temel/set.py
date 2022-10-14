s1={1,2,3,4,5}
s2={1,1,3,5,8,6,8}
s1
s2
type(s1)
l=set(s1)
set(l)
message="Merhaba, orda mısın?"
a=set(message)
a
# " " (boşluk) karakterini de sayıyor
# setler sıralı değildir

len(s2)
s2
# setler indexlenemez

s1.add("a")
s1
s1.remove("a")
s1
# Eğer hata silmek istediğimiz eleman yoksa hata almak istemiyorsak, discard()'ı kullanabiliriz.

s1.discard(10)
s1.add(10)
s1
s1.discard(10)
s1.difference(s2)
s1
s2
s1.difference(s2)
s2.difference(s1)
s1-s2
s2-s1

#symetric difference
# (s1\s2)U(s2\s1) = (s1 U s2)-(s1 n s2) sonucu verir 
# s1.symmetric_difference(s2)=s2.symmetric_difference(s1) aynı sonucu vermiş oluyor

s1.symmetric_difference(s2)
s2.symmetric_difference(s1)

# intersection
# s1 n s2 kesişim için
s1.intersection(s2)
s1&s2
s2&s1
s1 - (s1-s2) # yine kesişimi veriyor
s1
2 in s1
7 in s1
s1
s1.add(5)
s1
s1.remove(8)
s1.discard(8)
s1
s2
s1-s2
s2-s1

# union (Birleşim)
# (s1 U s2)=(s2 U s1)

s1.union(s2)
s2.union(s1)

#Disjoint Sets
# s1 n s2 =! Boş küme olup olmadığını kontrol eder.
# Boş küme ise True, boş küme değilse False döndürür 
s1.isdisjoint(s2)
s2.isdisjoint(s1)

len(s1.isdisjoint(s2))
s3=set([24,25,26])
s1
s2
s3
len(s1.intersection(s3))==0
len(s1.intersection(s3))==1

# Subset (Alt Küme)
s1.issubset(s2)
s2.issubset(s1)
s4=set(s1.union(s2))
s4
s1
s1.issubset(s4)
s4.issubset(s1)

#Superset (Üst Küme)
s1
s2
s3
s4
s1.issuperset(s4)
s4.issuperset(s1)
s4.issuperset(s2)
s2.issuperset(s4)
