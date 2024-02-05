"""
https://www.acmicpc.net/problem/12851
백준 골드4 12851 숨바꼭질2
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고,
가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
"""

"""
출력 형식에 늘 유의하자
"""

from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    print(1)
else:
    INF = 2 * K
    v = [[INF, 0] for _ in range(INF)]  # 위치당 시간, cnt

    q = deque([N])
    v[N] = [0, 1]

    while q:
        cur = q.popleft()
        curT, curCnt = v[cur]

        if cur == K:
            print(v)
            print(curT)
            print(curCnt)
            break

        for nxt in [cur - 1, cur + 1, cur * 2]:
            if nxt < 0 or nxt >= INF: continue  # 범위 밖

            # 이미 더 빠른 시간에 방문했을 경우 무시
            if v[nxt][0] < curT + 1:
                continue

            # 이미 같은 시간에 방문했을 경우 cnt 증가
            elif v[nxt][0] == curT + 1:
                v[nxt][1] += curCnt

            # 지금 가장 빨리 방문했을 경우 갱신 후 q에 push
            else:
                v[nxt] = [curT + 1, curCnt]
                q.append(nxt)
