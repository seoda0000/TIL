"""
https://www.acmicpc.net/problem/1686
백준 골드4 1686 복날

오늘은 복날이다!

해빈이는 복날을 맞아 순살치킨 파티를 하기 위해 닭을 잡으려고 한다. 하지만 이번에도 쉽게 잡힐까보냐. 용감한 닭 한 마리가 해빈이에게서 도망치려 한다. 닭은 v m/sec의 속도로 이동할 수 있고, (xs, ys)에서 (xt, yt)에 존재하는 벙커까지 이동하면 해빈이에게서 도망칠 수 있다. 하지만 닭이 m분 이상 벙커 밖을 돌아다닌다면 바로 해빈이에게 잡혀 치킨이 되고 말 것이다.

과연 닭은 해빈이에게서 도망칠 수 있을까?
"""

from collections import deque


def go(si, sj):
    q = deque([(si, sj)])
    cnt = -1

    while q:
        cnt += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            if ci == xt and cj == yt:  # 종료 조건
                return cnt - 1

            for i in range(N + 1):
                if v[i]: continue
                ni, nj = bunkers[i]
                if (ci - ni) ** 2 + (cj - nj) ** 2 >= able ** 2: continue

                # 이동 가능
                v[i] = 1
                q.append((ni, nj))
    return -1


V, M = map(int, input().split())
xs, ys = map(float, input().split())
xt, yt = map(float, input().split())
bunkers = []
able = V * 60 * M

while True:
    try:
        x, y = map(float, input().split())
        bunkers.append((x, y))
    except:
        break

N = len(bunkers)
bunkers = bunkers + [(xt, yt)]
v = [0] * (N + 1)
ans = go(xs, ys)

if ans >= 0:
    print(f'Yes, visiting {ans} other holes.')
else:
    print('No.')
