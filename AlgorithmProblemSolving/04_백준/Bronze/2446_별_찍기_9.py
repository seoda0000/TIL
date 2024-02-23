N = int(input())

for n in range(1, 2 * N):
    scnt = abs(N - n) * 2 + 1
    bcnt = (2 * N - 1 - scnt)//2
    print(" " * bcnt + "*" * scnt)
