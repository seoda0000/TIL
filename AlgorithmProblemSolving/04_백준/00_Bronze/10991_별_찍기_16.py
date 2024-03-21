N = int(input())

for n in range(1, N + 1):
    print(' '*(N-n) + '*' + ' *'*(n-1))