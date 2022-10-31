# def fonksiyon_adi(input):

def square(x):
    kuvvet=x**3
    print("return oncesi")
    return kuvvet
    print("return sonrasi")
print(square(3))

print(square(square(2)))
print("--------------")

def squarey(y):
    res=y*y
    print("Square of "+ str(y) + ": " + str(res))
    return res
    print("Square of "+ str(y) + ": " + str(res))
print(squarey(3))