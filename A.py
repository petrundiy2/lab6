__author__ = 'Petr'
with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        N = int(inp.readline())
        A = inp.readline().split()
        B=[]
        x=0
        while x<=N:
            for y in range(N):
                if x!=y and A[x]==A[y]:
                    print(A[x],file=out)
                    x=N
                    break
            x+=1
