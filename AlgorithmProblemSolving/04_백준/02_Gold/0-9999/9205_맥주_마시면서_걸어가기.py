from collections import deque


def bfs():
    q = deque([(sx, sy)])

    while q:
        cx, cy = q.popleft()

        for a in range(len(stores))[::-1]:
            nx, ny = stores[a]
            if abs(nx - cx) + abs(ny - cy) <= distance:
                if nx == ex and ny == ey:
                    return 'happy'
                stores.pop(a)
                q.append((nx, ny))
    return 'sad'


T = int(input())
for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(N + 1)]
    ex, ey = stores[-1]
    distance = 50 * 20

    print(bfs())
