from collections import deque


def attack(ai: int, aj: int, ad: str):
    global ans
    if arr[ai][aj] == 0:
        return

    di, dj = dic[ad]
    q = deque([(ai, aj)])

    arr[ai][aj] = 0
    ans += 1

    while q:
        ci, cj = q.popleft()

        ck = domino[ci][cj]

        for k in range(1, ck):
            ni, nj = ci + di * k, cj + dj * k

            if not (0 <= ni < N and 0 <= nj < M): break

            if arr[ni][nj]:
                arr[ni][nj] = 0
                ans += 1
                q.append((ni, nj))

    return


N, M, R = map(int, input().split())
dic = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
domino = []  # 초기 상태
arr = []  # 진행 판
ans = 0

for _ in range(N):
    ipt = tuple(map(int, input().split()))
    domino.append(ipt)
    arr.append(list(ipt))

for _ in range(R):
    # 공격
    ax, ay, ad = input().split()
    ax, ay = int(ax) - 1, int(ay) - 1
    attack(ax, ay, ad)

    # 방어
    bx, by = map(int, input().split())
    bx, by = bx - 1, by - 1
    arr[bx][by] = domino[bx][by]

print(ans)
for row in arr:
    p = ['S' if r > 0 else 'F' for r in row]
    print(*p)
