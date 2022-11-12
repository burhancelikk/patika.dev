n=int(input())
arr=list(map(int,input().split())) # Input:1 3 4 6 8 9 6 Output:[1,3,4,6,8,9,6]

print(arr)
A=sorted(arr[:n])
print(A)

'''
if 2<=n<=10:
    for i in A:
        if -100<=A[i]<=100 & i<n:
            True
        else:
            A.remove(A[i])
else:
    n=int(input())
    arr=list(map(int,input().split()))

print(A)
'''