N=int(input())
A=[]
for x in range(N):
    A.append(int(input()))
k=0
for x in range(N):
    if A[x]==5:
        k-=1
    if A[x]>5:
        k+=(A[x]//5)-1
if k<0:
    print(0)
if k>=0:
    print(k)
