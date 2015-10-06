N=int(input())
A=[]
p=0
for x in range(N):
    A.append(int(input()))
for x in range(N):
    k=0
    for y in range(N):
        if A[x]==A[y] and x!=y:
            k+=1
    if k==1:
        p=A[x]
print(p)
