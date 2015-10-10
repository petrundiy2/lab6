__author__ = 'Petr'
with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        N = int(inp.readline())
        A = inp.readline().split()
        A.sort()
        for x in range(N-1):
            if A[x] == A[x+1]:
                print(A[x], file=out)
                break
