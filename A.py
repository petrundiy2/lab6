a=open('input.txt','r')
b=open('output.txt','w')
s=a.readline()
f=a.readline()
g=f+' '
A=[]
h=''
y=0
for x in range(len(g)):
    if g[x]==' ':
        A.append(eval(g[y:x]))
        y=x
for x in range(len(A)):
    k=0
    for y in range(len(A)):
        if A[x]==A[y] and x!=y:
            k+=1
    if k==1:
        h=A[x]
if h!='':
    print(h,file=b)
