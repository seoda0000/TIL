from collections import deque


def bfs():
    v = [0] * (F + 1)
    q = deque([S])
    v[S] = 1
    button = -1
    while q:
        nq = len(q)
        button += 1

        for _ in range(nq):
            c = q.popleft()
            if c == G:
                return button
            for nxt in [c + U, c - D]:
                if nxt <= 0 or nxt > F or v[nxt]: continue
                v[nxt] = 1
                q.append(nxt)
    return -1


F, S, G, U, D = map(int, input().split())
ans = bfs()
if ans >= 0:
    print(ans)
else:
    print('use the stairs')
