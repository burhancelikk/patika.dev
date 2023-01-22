x=0 # x değişkeni global
def fonk(): 
    x=1 # x değişkeni local
    return x
print(fonk())
print(x)
# namespace alanı sayesinde fonksiyon içindeki ve dışındaki aynı adlı değişkenler birbirine karışmıyor.

x=[]
print("x\ 'in ilk hali", x)

def degistir():
    print("x\ 'i degistiriyoruz...")
    x.append(1)
    return x

degistir()
print("x\ 'in son hali: ",x)
print(type("Hello world"))
print(complex(54.5),end="\n")

txt="  Hello world guys "
x=txt.strip()
print(x)

a = {"brand": "Ford","model": "Mustang","year": 1964}

print(a.keys())

