"""
https://www.acmicpc.net/problem/19940
백준 골드5 19940 피자 오븐
"""

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

        if cur == target:  # 종료조건
            for i in range(5):
                ans[i] += st.count(str(i))
            break

        for i, d in enumerate([-1, 1, -10, 10, 60]):  # 사전순 고려하여 거꾸로
            nxt = max(0, cur + d)
            if nxt > 60: continue
            if v[nxt] <= v[cur] + 1: continue

            v[nxt] = v[cur] + 1
            q.append((nxt, st + str(4 - i)))  # 버튼 string으로 기록

    print(*ans)
