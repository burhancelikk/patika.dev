n=int(input())
arr=list(map(int,input().split())) # Input:1 3 4 6 8 9 6 Output:[1,3,4,6,8,9,6]

print(arr)
A=sorted(arr[:n])
print(A)
print(max(A))

i=1
for i in range(n):
    if A[A.index(max(A))-i] < A[A.index(max(A))]:
        print(A[A.index(max(A))-i])
        break
    else:
        i+=1
