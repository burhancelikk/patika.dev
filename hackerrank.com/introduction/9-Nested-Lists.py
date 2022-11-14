n=int(input())
res=[]
grade=[]
for i in range(n):
    name=input()
    mark=float(input())
    res.append([name,mark])
    grade.append(mark) # calculation 2nd lowest
print(res)
print(grade)
grade=sorted(set(grade)) # sorted uniqe
print(grade)
m=grade[1]
print(m)
name=[]
for val in res:
    if m==val[1]:
        name.append(val[0])
print(name) # unsorted
name.sort()
print(name) #sorted
for nm in name:
    print(nm)
