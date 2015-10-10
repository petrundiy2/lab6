__author__ = 'Petr'
with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        N,K = list(map(int, inp.readline().split()))
        D = [0 for i in range(int(N))]
        for i in range(int(K)):
            G = list(map(int, inp.readline().split()))
            d = G[0]-1
            c = G[1]-1
            s = G[2]
            D[d] -= s
            D[c] += s
        print(' '.join(map(str, D)), file=out)
