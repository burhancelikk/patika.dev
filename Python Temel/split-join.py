### split() belirli bir bölme kriterine göre string'in alt parçalarını listenin elemanları olarak dönüştürebiliriz.
###
s="merhaba nasılsın, ben çok iyiyim ?"
s.split()
s2="limon,portakal,elma"
s2.split()
s2.split(",") #virgüle göre döndürür

#join
# listenin elemanları arasına belirtilen yapıyı koyup string'e dönüştürür.

l=['limon','Portakal','Elma']
s3=",".join(l)
s3
type(s3)
"-".join(l)
"/".join(l)
" ".join(l)

#Soru

mailler={kisi1:"ad1.soyad1@gmail.com",kisi2:"ad2soyad2@gmail.com",kisi3:"ad3.soyad3@gmail.com"}

x=l.append(1)
x