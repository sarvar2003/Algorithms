N, M = [int(n) for n in input().split(' ')]
tight_dominos = 0

if N == 1:
    tight_dominos = M-1
elif M == 1:
    tight_dominos = N-1
else:
    tight_dominos = N * (M-1)
print(tight_dominos)