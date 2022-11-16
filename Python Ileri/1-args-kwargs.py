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
    print(type(a))
    print(len(a))
    for e in a:
        if type(e)==int:
            res+=e
        if type(e)==str:
            res+=e
        if type(e)==list:
            for j in e:
                res+=j
    return res

print(sum_2([1,2],5,[4,5,7]))
