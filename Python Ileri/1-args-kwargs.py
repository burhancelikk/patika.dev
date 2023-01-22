# args
def sum(numbers):
    res=0
    for e in numbers:
        res+=e
    return res

numbers=[1,2,3,4]
print(sum(numbers))


print("---------------------------")
print("\n")

def sum (*args):
    res=0
    for e in args:
        res+=e
    return res
print(sum(1,2,3,4,5))

print("---------------------------")
print("\n")

def sum(*numbers):
    res=0
    print(type(numbers))
    print(numbers)
    for e in numbers:
        res+=e
    return res

print(sum(1,2,3,4))

print(sum(3,5,6,7,8,9))

print("---------------------------")
print("\n")

def sum_2(*a):
    res=0
    print("type a :",type(a))
    print("a =",a)
    print("len(a) =",len(a))
    for e in a:
        if type(e)==int:
            res+=e
        if type(e)==str:
            estr=int(e)
            res+=estr
        if type(e)==list:
            for j in e:
                res+=j
    return res

print("sum_2([1,2],5,[4,5,7],'10')=",sum_2([1,2],5,[4,5,7],"10"))




print("---------------------------")
print("\n")

#=====================================
#kwargs
#=====================================

def students(**kwargs):
    print(type(kwargs))
    for v in kwargs.values():
        print(v)

d={"name":"jake","student_number":"401"}
print(students(name="jake",student_number="401"))
print(d)


print("---------------------------")
print("\n")

def studef(**stuin):
    print(stuin)
    for v in stuin:
        print(v)
studef(name="Jake",student_number="401")
print(studef)


print("---------------------------")
print("\n")

def weird(*ar,**kwar):
    res=0
    for e in ar:
        res+=e
    for k,v in kwar.items():
        print(k,":",v)
    return res

print(weird(1,2,3,name="jake",student_number=401))

print("---------------------------")
print("\n")

l1=[1,2,3,4]
print(l1)
print(*l1)

l2=[20,21]
merge_l=[*l1,*l2]
print("type(merge_l):",type(merge_l))
# print("type(*merge_l):",type(*merge_l)) Hata verdi

d1={"name":"Fıstık","age":"3","number":6}
d2={"last_name":"Celik","Color":"Yellow","number":5}
d3={"birdcage Color":"White","number":4}
merge_d={**d1,**d2,**d3}
print(merge_d)
#print(**merge_d)

print("---------------------------")

str_list=[*"Hello world"]
print(str_list) # "Hello world" unpack edildi
print(*str_list) # Oluşturulan liste tekrar unpack edildi

merge_d2={"d1":d1,"d2":d2}
print(merge_d2)
print(*merge_d2)
print(*merge_d2.values())
