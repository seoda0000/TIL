def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def pprint():
    parr = [['O'] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] and ci == i and cj == j:
                parr[i][j] = 'X'

            elif arr[i][j]:
                parr[i][j] = 'Z'
            elif ci == i and cj == j:
                parr[i][j] = 'A'
    for a in parr:
        print(*a)
    print()


di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]
ei = [1, 0, -1, 0, 1, 1, -1, -1]
ej = [0, -1, 0, 1, 1, -1, 1, -1]
N = int(input())
orders = input()
arr = [[list() for _ in range(N)] for _ in range(N)]
light = [[0] * N for _ in range(N)]
ipts = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if ipts[i][j] == 'Z':  # 좀비 발견
            arr[i][j].append(0)

ci, cj = 0, 0
cd = 0
ans = "Phew..."
if ipts[ci][cj] == 'S':  # 스위치
    light[ci][cj] = 1
    for e in range(8):
        si, sj = ci + ei[e], cj + ej[e]
        if OOB(si, sj): continue
        light[si][sj] = 1
if not light[i][j] and ipts[ci][cj] == 'Z':
    ans = "Aaaaaah!"
else:
    for order in orders:
        if order == 'L':
            cd = (cd - 1) % 4

        elif order == 'R':
            cd = (cd + 1) % 4

        else:  # 앞 1칸 전진
            ni, nj = ci + di[cd], cj + dj[cd]
            if OOB(ni, nj): ni, nj = ci, cj  # 벽
            if ipts[ni][nj] == 'S':  # 스위치
                light[ni][nj] = 1
                for e in range(8):
                    si, sj = ni + ei[e], nj + ej[e]
                    if OOB(si, sj): continue
                    light[si][sj] = 1

            ci, cj = ni, nj

        if not light[ci][cj] and arr[ci][cj]:
            ans = "Aaaaaah!"
            break

        # 좀비 이동
        new_arr = [[list() for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if not arr[i][j]: continue
                for zd in arr[i][j]:
                    ni, nj = i + di[zd], j + dj[zd]
                    if OOB(ni, nj):  # 벽
                        new_arr[i][j].append((zd + 2) % 4)
                    else:
                        new_arr[ni][nj].append(zd)
        arr = new_arr

        if not light[ci][cj] and arr[ci][cj]:
            ans = "Aaaaaah!"
            break

print(ans)
