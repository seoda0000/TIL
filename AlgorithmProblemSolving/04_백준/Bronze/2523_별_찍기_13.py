N = int(input())

for n in range(1, 2 * N):
    scnt = N - abs(N - n)
    print('*' * scnt)
