"""
https://www.acmicpc.net/problem/2468
백준 실버1 2468 안전 영역
"""

def f(w, v):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:  # 방문하지 않았다면 탐색
                v[i][j] = 1
                if arr[i][j] <= w:  # 수위보다 높은 건물만
                    continue

                q = [(i, j)]  # 시작점

                while q:
                    a, b = q.pop(0)

                    for n in range(4):  # 4방향 탐색
                        na, nb = a + dx[n], b + dy[n]

                        if 0 <= na < N and 0 <= nb < N and v[na][nb] == 0:  # 범위 내이고 방문하지 않았다면
                            v[na][nb] = 1
                            if arr[na][nb] > w:  # 수위보다 높으면 같은 영역
                                q.append((na, nb))

                cnt += 1  # 영역 파악 종료 후 개수 추가

    return cnt


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1
mxh = 0
mnh = 101
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for a in arr:
    mxh = max(mxh, max(a))
    mnh = min(mnh, min(a))

for w in range(mnh, mxh):
    v = [[0] * N for _ in range(N)]
    ans = max(ans, f(w, v))

print(ans)

"""
함수화 적용한 풀이
"""
def searchArea(si, sj, h):
    stk = [(si, sj)]
    v[si][sj] = h
    while stk:
        ci, cj = stk.pop(0)
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if arr[ni][nj] > h > v[ni][nj]:
                v[ni][nj] = h
                stk.append((ni, nj))

    return


def findAreaCnt(h):
    cnt = 0
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] > h > v[i][j]:
                searchArea(i, j, h)
                cnt += 1
    return cnt


N = int(input()) + 2
arr = [[0] * N] + [[0] + list(map(int, input().split())) + [0] for _ in range(N - 2)] + [[0] * N]
v = [[0] * N for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
hset = set()
for a in arr:
    hset |= set(a)
hlst = sorted(list(hset))
ans = 1

for height in hlst[1:]:
    ans = max(ans, findAreaCnt(height))
print(ans)
