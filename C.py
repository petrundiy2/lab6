with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        N = int(inp.readline())
        A = list(map(int, inp.readline().split()))
        k=N+1
        for x in range (N):
            for y in range(N):
                if (A[x])==-(A[y]) and A[x]<0 and x<y:
                    if abs(x-y)<k:
                        k=abs(x-y)
        if k!=N+1:
            print (k,file=out)
        if k==N+1:
            print(0,file=out)
