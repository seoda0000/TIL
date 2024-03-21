"""
https://www.acmicpc.net/problem/4963
백준 실버2 4963 섬의 개수
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.



한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
"""
def search(si, sj):  # 섬에 해당하는 면적을 찾아 visited 표시
    v[si][sj] = 1
    q = [(si, sj)]
    while q:
        ci, cj = q.pop()
        for d in range(8):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 1 and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj))
    return


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]
    di = [0, 0, 1, -1, -1, -1, 1, 1]
    dj = [1, -1, 0, 0, -1, 1, -1, 1]
    ans = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and v[i][j] == 0:  # 새로운 섬 발견
                search(i, j)
                ans += 1
    print(ans)
