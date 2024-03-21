N = int(input())

for i, n in enumerate(range(N)[::-1]):
    print(' ' * n + '*' * (i * 2 + 1))
