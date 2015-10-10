with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        k,n = list(map(int, inp.readline().split()))
        e=0
        C=[]
        for x in range(int(k)):
            A=list(map(int, inp.readline().split()))
            C+=[A]
        B=[]
        K=[]
        E=[]
        for x in range(int(n)):
            for y in range(int(k)):
                K.append(C[y][x])
            B+=[K]
            K=[]
        for x in range(len(B)):
            E.append(min(B[x]))
        print(' '.join(map(str, E)),file=out)
