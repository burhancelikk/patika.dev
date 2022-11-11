l=[1,2,3,4]
print(l[0:3])
l[0:3]=30,40,60
print(l[0:3])
print(l)
l[0:3]=70,68
print(l)

s="hey"

print(len(s))
print(len(l))

l.append(200)
print(l)

l.extend([100,200,300])
print(l)
l.insert(0,5)
print(l)

l.insert(3,25)
print(l)

l.remove(200)
print(l)

print(l[:-10])
