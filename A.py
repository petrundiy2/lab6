a=open('input.txt','r')
b=open('output.txt','w')
s=a.readline()
f=a.readline()
A=[]
h=''
for x in range(int(s)*2):
    if f[x]!=' ':
        A.append(f[x])
for x in range(len(A)):
    k=0
    for y in range(len(A)):
        if A[x]==A[y] and x!=y:
            k+=1
    if k==1:
        h=A[x]
print(eval(h),file=b)
