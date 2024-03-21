N = int(input())

for n in range(1, N + 1):
    st = ' ' * (N - n) + '*'

    if 1 < n < N:
        st += ' ' * (2 * n - 3) + '*'
    elif n == N:
        st += '*' * (n - 1) * 2

    print(st)
