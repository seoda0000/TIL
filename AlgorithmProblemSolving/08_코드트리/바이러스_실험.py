"""

"""

"""
3:01 시작
3:12 구상완료
3:29 제출
3:37 디버깅 완료
"""
from collections import defaultdict

di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [1, -1, 0, 0, 1, -1, 1, -1]
N, v_cnt, K = map(int, input().split())
food = [[5] * N for _ in range(N)]
plus_food = [tuple(map(int, input().split())) for _ in range(N)]
virus_dic = defaultdict(list)
for _ in range(v_cnt):
    r, c, age = map(int, input().split())
    virus_dic[(r - 1, c - 1)].append(age)

for _ in range(K):
    # 양분 섭취 + 죽은 바이러스->양분
    for key in virus_dic.keys():
        virus_lst = virus_dic[key]
        i, j = key
        virus_lst.sort()
        nv = len(virus_lst)
        dead_virus = []

        for x in range(nv):
            age = virus_lst[x]
            if food[i][j] >= age:
                food[i][j] -= age
                virus_lst[x] += 1  # 나이 증가
            else:
                virus_lst, dead_virus = virus_lst[:x], virus_lst[x:]
                break

        for age in dead_virus:
            food[i][j] += age // 2

        virus_dic[key] = virus_lst

    # 번식 + 양분 추가
    new_virus_cnt_arr = [[0] * N for _ in range(N)]
    for key, virus_lst in virus_dic.items():
        i, j = key
        for age in virus_lst:
            if age % 5: continue

            for d in range(8):
                ni, nj = i + di[d], j + dj[d]
                if not (0 <= ni < N and 0 <= nj < N): continue
                new_virus_cnt_arr[ni][nj] += 1

    for i in range(N):
        for j in range(N):
            food[i][j] += plus_food[i][j]
            if new_virus_cnt_arr[i][j]:
                virus_dic[(i, j)].extend([1] * new_virus_cnt_arr[i][j])

ans = 0
for value in virus_dic.values():
    ans += len(value)
print(ans)
