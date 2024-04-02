"""
실행시간: 648(532) -> 464
풀이시간: 45분 -> 36분

원래 i, j로 모두 순회했는데 이번엔 dict의 keys만 순회했다. 그래서 더 빨라진 것 같다.
또한 이전엔 새로운 리스트를 만들어 append 해주었는데, 이번엔 슬라이싱을 활용했다.
append 방식은 실수할 수가 없는 구조다. 그러나 슬라이싱의 경우 동시 처리해주지 않는 경우 실수할 수 있다.
이번에 실수했다!! 괜히 새로운 방식으로 빨리 처리하려고 하다가 실수한 것이다. 실수하지 않을 방식을 선택하자...
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

"""
9:40 1차 구현 완료
9:45 코드 검토 후 제출

변수명부터 자료의 구성 요소까지 설계한 후에야 코딩했고 딱히 어려움은 없었다.
list의 요소로 무엇이 들어갈지 정하고, 또 잘 나타낼 수 있도록 age 등 직관적인 변수를 썼던 게 도움이 되었던 것 같다.

N이 10이고 K가 1000이라 시간복잡도도 문제 없을 거라 생각했다.
다만 가을에 번식하는 나무를 바로 처리하면 불필요한 연산이 늘어날 수도 있어서 cnt를 기록하는 배열을 따로 만들었다.
한눈에 보는 게 편한 로직(코드 전체가 공유하는 변수가 많음)이라 함수는 딱히 만들지 않았다.

죽은 나무 체크하는 로직 효율화 시도 -> 죽은 나무를 발견하자마자 뒷나무를 다 죽은 나무로 판단.
시간이 줄었다
"""

from collections import defaultdict

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]
ground = [[5] * N for _ in range(N)]  # 초기 밭
dic = defaultdict(list)

for _ in range(M):  # 나무 심기
    x, y, z = map(int, input().split())
    dic[(x - 1, y - 1)].append(z)

for _ in range(K):  # K년 동안 경작

    # 봄 & 여름
    for i in range(N):
        for j in range(N):

            if not dic[(i, j)]: continue  # 나무 없는 경우 skip

            trees = sorted(dic[(i, j)])
            alive_trees = []  # 살아남은 나무
            dead_point = -1

            for t in range(trees):  # 봄

                if ground[i][j] < trees[t]:
                    dead_point = t  # 첫번째 죽은 나무 (이후는 다 죽는다)
                    break
                else:
                    ground[i][j] -= trees[t]
                    alive_trees.append(trees[t] + 1)

            if dead_point >= 0:  # 여름
                dead_trees = trees[dead_point:]
                for age in dead_trees:
                    ground[i][j] += age // 2

            dic[(i, j)] = alive_trees

    # 가을 & 겨울
    fall_trees = [[0] * N for _ in range(N)]  # 가을에 새로 태어나는 나무의 수

    for i in range(N):
        for j in range(N):

            trees = dic[(i, j)]

            for age in trees:

                if age % 5 == 0:  # 나이 5의 배수 나무

                    for d in range(8):
                        ni, nj = i + di[d], j + dj[d]
                        if not (0 <= ni < N and 0 <= nj < N): continue

                        fall_trees[ni][nj] += 1

    for i in range(N):
        for j in range(N):
            new_tree_cnt = fall_trees[i][j]  # 가을
            dic[(i, j)] += [1] * new_tree_cnt

            ground[i][j] += A[i][j]  # 겨울

# 최종 나무 세기
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(dic[(i, j)])
print(ans)
