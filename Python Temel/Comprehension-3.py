#SET COMPREHENSION

numbers=[1,2,3,4,5,6,7,1,2]

set_numbers1={s for s in numbers if s in [1,2,3,4,5,6,1,2]}
set_numbers2={s for s in numbers if s in [1,2,3,4,5,6]}
print(set_numbers1)
print(set_numbers2)

#DICTIONARY COMPREHENSION
square_dict={e:e*e for e in range(1,11)}
print(square_dict)



#NESTED LIST COMPREHENSION

m=[[j for j in range(7)] for i in range(5)]
# m=[[j for j in range(7)] for _ in range(5)]
print(m)

for l in m:
    print(l)

print("-----------------")

k=[[10,11,12],[13,14],[15,16,17,18]]

new_m=[]

for l in k:
    print(l)
    for e in l:
        new_m.append(e)
        print(e)

print("-------------------")

# Matrixi list comprehension ile flat etme
k=[[10,11,12],[13,14],[15,16,17,18]]
flatten_k1=[e for l in k for e in l]
print(flatten_k1)

#Sadece çift değerleri kabul edecek
flatten_k2=[e for l in k for e in l if e%2==0]
print(flatten_k2)

n=[[[25,36,62],[28,38,64],[30,40,67]],[[1,27,56],[1,25,55],[2,21,51]]]

flatten_n=[i for x in n for y in x for i in y]
print(flatten_n)

