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
