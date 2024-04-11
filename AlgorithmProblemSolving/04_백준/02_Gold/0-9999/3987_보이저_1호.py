N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
si, sj = map(int, input().split())
si -= 1
sj -= 1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ansdir = ["U", "R", "D", "L"]
dic = {(-1, 0): 0, (0, 1): 1, (1, 0): 2, (0, -1): 3}
ans = []
Voyager = "Voyager"
for d in range(4):
    ci, cj = si, sj  # 초기 데이터 세팅
    dir_i, dir_j = di[d], dj[d]
    v = [[0] * M for _ in range(N)]  # 방문 횟수 기록
    v[ci][cj] = 1
    t = 1
    while True:
        ni, nj = ci + dir_i, cj + dir_j

        if not (0 <= ni < N and 0 <= nj < M):
            ans.append(t)
            break

        if arr[ni][nj] == 'C':
            ans.append(t)
            break

        if v[ni][nj] == 2:
            ans.append(Voyager)
            break

        if arr[ni][nj] == '/':
            dir_i, dir_j = -dir_j, -dir_i

        if arr[ni][nj] == '\\':
            dir_i, dir_j = dir_j, dir_i

        v[ni][nj] += 1

        ci, cj = ni, nj
        t += 1

if Voyager in ans:
    target = Voyager
else:
    target = max(ans)
print(ansdir[ans.index(target)])
print(target)
