N = int(input())
INF = N
lst = [INF] * (N + 1)
lst[1] = 0

for i in range(1, N):
    for j in [i + 1, i * 2, i * 3]:
        if j <= N and lst[j] > lst[i] + 1:
            lst[j] = lst[i] + 1

print(lst[N])
