'''
dic=dict(list())
dic['a'].append(99)
print(dic.items())
'''

from collections import defaultdict
d=defaultdict(list)
d['a'].append(99)
print(d.items())
# dict_items([('a', [99])])

n=int(input())
d=dict()  # {}
for i in range(1,n+1):
    v=input()
    if v in d:  # checking the key v is present in my dict d or not
        d[v].append(i)
    else:
        d[v]=[i] # assign the key as v and value as [i]
print(d.items())
for key,val in d.items():
    print(key,val)

print("\n")
print("--------")

from collections import defaultdict
d=defaultdict(list)
n=int(input())

for i in range(1,n+1):
    v=input()
    d[v].append(i) # here we are not assigning key and value,

print(d.items())
for key,val in d.items():
    print(key,val)

print("\n")
print("--------")

from collections import defaultdict
d=defaultdict(list)

n,m=map(int,input().split())

for i in range(1,n+1):
    v=input()
    d[v].append(i) # here we are not assigning key and value,

for i in range(m):
    k=input()
    if k in d:
        print(*d[k],sep=" ")
    else:
        print(-1)
