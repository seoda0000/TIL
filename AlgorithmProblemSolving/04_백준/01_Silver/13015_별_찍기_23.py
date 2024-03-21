N = int(input())
arr = ['*' * N + ' ' * (N - 1)]
for n in range(1, N):
    arr.append(' ' * n
               + '*'
               + ' ' * (N - 2)
               + '*'
               + ' ' * (N - 1 - n))

for n in range(N):
    arr[n] = arr[n] + arr[n][::-1][1:]

arr = arr + arr[::-1][1:]

for a in arr:
    print(a.rstrip())
