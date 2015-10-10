__author__ = 'Petr'
with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        N = int(inp.readline())
        A = list(map(int, inp.readline().split()))
        nf = 0
        hf = 0
        for i in range(N):
            if A[i] == 5:
                hf += 1
            else:
                hf -= (A[i]-5)//5
                if hf < 0:
                    nf -= hf
                    hf = 0
        print(nf, file=out)
