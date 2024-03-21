def exercise(nth, now):
    global ans

    if nth == N:
        ans += 1
        return

    for n in range(N):
        if v[n]: continue
        if now - K + lst[n] < 500: continue
        v[n] = 1
        exercise(nth + 1, now - K + lst[n])
        v[n] = 0

    return


N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
v = [0] * N
exercise(0, 500)
print(ans)
