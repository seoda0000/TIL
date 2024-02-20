from collections import deque

T = int(input())
INF = 10_000_000
for _ in range(T):
    target = int(input())
    v = [INF] * 61  # (N//60)*60 ~ (N//60+1)*60
    ans = [0] * 5
    mn_sixty = target // 60  # +60버튼을 눌러야할 최소한의 횟수
    v[0] = ans[0] = mn_sixty
    s = mn_sixty * 60  # 시작 숫자
    target -= s  # 남은 숫자
    q = deque([(0, '')])

    while q:
        cur, st = q.popleft()

        if cur == target:
            for i in range(5):
                ans[i] += st.count(str(i))
            break

        for i, d in enumerate([-1, 1, -10, 10, 60]):
            nxt = max(0, cur + d)
            if nxt > 60: continue
            if v[nxt] <= v[cur] + 1: continue

            v[nxt] = v[cur] + 1
            q.append((nxt, st + str(4 - i)))
    print(*ans)
