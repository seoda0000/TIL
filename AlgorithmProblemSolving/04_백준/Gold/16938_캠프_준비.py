def pick(nth, sm, mx, mn):  # nth번째 문제를 고려: 여태까지의 (합, 최솟값, 최댓값)
    global ans

    if nth == N:
        if L <= sm <= R and mx - mn >= X:  # 문제 조건 check
            ans += 1
        return

    if sm > R:  # 가지치기: 조건 충족 불가
        return

    # nth번째 문제를 포함하지 않는 경우
    pick(nth + 1, sm, mx, mn)
    # nth번째 문제를 포함하는 경우
    pick(nth + 1, sm + problems[nth], max(mx, problems[nth]), min(mn, problems[nth]))

    return


N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
INF = 10 ** 6 * 15 + 1
ans = 0

pick(0, 0, 0, INF)

print(ans)
