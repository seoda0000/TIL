def find_shortcut(n, arr):
    v = [0] * (N + 1)
    v[n] = 1

    for _ in range(N-1):
        mn = INF
        nxt = -1
        for i in range(1, N + 1):
            if v[i]: continue
            if arr[n][i] < mn:
                mn = arr[n][i]
                nxt = i

        v[nxt] = 1
        for i in range(1, N + 1):
            if arr[n][i] > arr[n][nxt] + arr[nxt][i]:
                arr[n][i] = arr[i][n] = arr[n][nxt] + arr[nxt][i]

    return


N, M = map(int, input().split())
INF = 99999
arr = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    arr[i][i] = 0
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for n in range(1, N + 1):
    find_shortcut(n, arr)

ans = INF * N
ans_a = ans_b = -1
for a in range(1, N):
    for b in range(a + 1, N + 1):
        sm = 0
        for i in range(1, N + 1):
            sm += min(arr[a][i], arr[b][i])

        if sm < ans:
            ans = sm
            ans_a, ans_b = a, b

print(ans_a, ans_b, ans * 2)
