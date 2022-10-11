konum=(10,34)
konum # değerleri değiştirilemez

# tuple lar (element1,element2) şeklinde tanımlanır.

konum[0]
konum[1]

t=([1,2],3,"a")

t[0]
t[0][0]=23
t[0][1]=24
t[0]

#x ve y nin değerlerini değiştirmek
x=2
y=3
#1.yol
temp=x
x=y
y=temp
x
y
#2.yol
(x,y)=(y,x)
x
y

a=1,2,3,4,5,6,7
a
type(a)

[x,y]=[y,x]
x
y

# in keywords

l=[1,2,3,4,5,6,7]
40 in l
3 in l
k=1,2
2 in k
3 in k

#Dictionaries
# {key1:value1, key2:value2}

# notlar=[70,80,90]
#isim=["Deniz","Ege","Gizem"]
# og_no=[703,408,690]

notlar = {"Deniz":80, "Ege":72, "Gizem":95}
ogrenciler={"Deniz":{"not":80, "ogrenci_no":703},"Ege":{"not":72,"ogrenci_no":408},"Gizem":{"not":95,"ogrenci_no":690}}
ogrenciler["Deniz"]
ogrenciler["Ege"]["not"]
ogrenciler["Ege"]["ogrenci_no"]

len(ogrenciler)
notlar["Mert"]=75
notlar["Deniz"]
notlar
del notlar["Mert"]
notlar

d={1:2,"3":5,15:"Deniz","Ali":"Veli",(5,6):[1,2,3]}
d[1]
d["3"]
d[15]
d["Ali"]
d[(5,6)]
# list ler key olamıyor
#e={[1,2]:5} olamaz
f={"i":{2}}
f["i"]