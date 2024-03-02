def find_cross(si, sj):  # si, sj 다음 칸부터 십자가 찾음
    global ans

    if len(temp) >= 2:  # 모두 찾음
        ans = max(ans, temp[0] * temp[1])
        return

    else:  # 십자가 찾아야 함
        i = si
        for j in range(sj + 1, M):
            # 십자가 찾기
            if arr[i][j] == '.': continue
            if v[i][j]: continue
            mxk = find_mx_len(i, j)

            v[i][j] = 1
            for k in range(mxk + 1):
                check_4th(i, j, k, 1)
                temp.append(1 + k * 4)
                find_cross(i, j)
                temp.pop()
            for k in range(mxk + 1):
                check_4th(i, j, k, 0)
            v[i][j] = 0

        for i in range(si + 1, N):
            for j in range(M):
                # 십자가 찾기
                if arr[i][j] == '.': continue
                if v[i][j]: continue
                mxk = find_mx_len(i, j)

                v[i][j] = 1
                for k in range(mxk + 1):
                    check_4th(i, j, k, 1)
                    temp.append(1 + k * 4)
                    find_cross(i, j)
                    temp.pop()
                for k in range(mxk + 1):
                    check_4th(i, j, k, 0)
                v[i][j] = 0

    return


def find_mx_len(si, sj):  # si, sj를 중심으로 한 최대 십자가 길이 찾기
    p = 1
    while True:
        for d in range(4):
            ni, nj = si + di[d] * p, sj + dj[d] * p
            if not (0 <= ni < N and 0 <= nj < M): break
            if arr[ni][nj] == '.': break
            if v[ni][nj]: break
        else:
            p += 1
            continue
        break
    return p - 1


def check_4th(i, j, k, num):  # i, j로부터 k칸 거리에 있는 4방향 칸 check
    for d in range(4):
        ni, nj = i + di[d] * k, j + dj[d] * k
        v[ni][nj] = num
    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = 1
temp = []
find_cross(0, -1)
print(ans)
