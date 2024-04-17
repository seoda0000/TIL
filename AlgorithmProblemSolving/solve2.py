import sys
from collections import deque, defaultdict

sys.stdin = open("input.txt", "r")


def get_score(si, sj, cd):
    score = 0
    ci, cj = si, sj
    while True:
        ni, nj = ci + di[cd], cj + dj[cd]  # 다음 위치

        if ni == si and nj == sj:  # 시작 좌표
            return score
        elif arr[ni][nj] == -1:  # 블랙홀
            return score
        elif arr[ni][nj] >= 6:  # 웜홀
            ni, nj = list(worm_dic[arr[ni][nj]] - {(ni, nj)})[0]  # 상대 웜홀로 나오기
        elif 1 <= arr[ni][nj] <= 5:  # 블럭 위치
            score += 1  # 점수 획득
            cd = block_dic[arr[ni][nj]][cd]  # 방향 전환
        ci, cj = ni, nj
    return score


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
block_dic = {  # 블록 별 방향에 따른 다음 방향 리스트
    1: (2, 3, 1, 0),
    2: (1, 3, 0, 2),
    3: (3, 2, 0, 1),
    4: (2, 0, 3, 1),
    5: (2, 3, 0, 1)
}
# 번호: {좌표, 좌표}
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) + 2
    worm_dic = defaultdict(set)
    arr = [[5] * N] \
          + [[5] + list(map(int, input().split())) + [5] for _ in range(N - 2)] \
          + [[5] * N]
    blank_lst = []
    for i in range(N):  # 빈칸이면 4방향 다 넣기 (초기 점수: 1점)
        for j in range(N):
            if arr[i][j] == 0:
                blank_lst.append((i, j))
            elif 6 <= arr[i][j]:
                worm_dic[arr[i][j]].add((i, j))
    ans = 0
    for i, j in blank_lst:
        for d in range(4):
            ans = max(ans, get_score(i, j, d))

    print(f'#{test_case} {ans}')
