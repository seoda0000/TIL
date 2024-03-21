N = int(input())

for n in range(1, 2 * N):
    bcnt = abs(N - n)
    scnt = N - bcnt
    print(' ' * bcnt + '*' * scnt)
