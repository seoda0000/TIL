def go(s, now, cnt, money):
    global ans
    if money >= ans:
        return

    if cnt == N - 1:
        if arr[now][s]:
            ans = min(ans, money + arr[now][s])

        return

    for i in range(N):
        if arr[now][i] == 0: continue
        if v[i]: continue
        v[i] = 1
        go(s, i, cnt + 1, money + arr[now][i])
        v[i] = 0

    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [0] * N
ans = 1000_000 * 11

for i in range(N):
    v[i] = 1
    go(i, i, 0, 0)
    v[i] = 0

print(ans)
