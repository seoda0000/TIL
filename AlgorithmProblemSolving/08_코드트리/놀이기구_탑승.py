"""
11:33 시작
11:36 구상 완료
11:44 구현 완료
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
N = int(input())
arr = [[0] * N for _ in range(N)]
favor_dic = dict()
for _ in range(N * N):
    ipt = list(map(int, input().split()))
    id, favor_lst = ipt[0], ipt[1:]
    favor_dic[id] = favor_lst

    # 칸 찾기
    blank_lst = []

    for i in range(N):
        for j in range(N):
            if arr[i][j]: continue  # 이미 찬 경우
            blank, favor = 0, 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj): continue
                if arr[ni][nj] == 0:
                    blank += 1
                elif arr[ni][nj] in favor_lst:
                    favor += 1
            blank_lst.append((-favor, -blank, i, j))

    blank_lst.sort()

    ei, ej = blank_lst[0][2], blank_lst[0][3]  # 결정
    arr[ei][ej] = id

ans = 0
for i in range(N):
    for j in range(N):
        id = arr[i][j]
        favor_lst = favor_dic[id]
        favor = 0

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if OOB(ni, nj): continue
            if arr[ni][nj] in favor_lst:
                favor += 1

        if favor: ans += 10 ** (favor - 1)
print(ans)
