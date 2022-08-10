'''
9489. 고대 유적 D2
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXAd8-d6MRoDFARP
땅속의 구조물을 촬영할 수 있는 특수 위성 카메라에 땅속에 묻힌 고대 구조물이 발견되었다. 구조물은 폭 1m, 길이 2m 이상의 직선 형태로 서로 평행 또는 직각으로만 자리하고 있으며, 1mx1m의 해상도의 사진데이터에 구조물이 있는 자리는 1로 나타난다.

사진의 해상도는 NxM이며, 구조물이 있는 곳은 1, 빈 땅은 0으로 표시된다. 위 그림의 경우 가장 긴 구조물은 노란색으로 표시된 영역이며, 길이는 6이다. 교차하거나 만나는 것처럼 보이는 구조물은 서로 다른 깊이에 묻힌 것이므로 직선인 구조물만 고려하면 된다.
평행한 모든 구조물은 서로 1m이상 떨어져 있고, 구조물의 최소 크기는 1x2m이다.

여러 구역의 사진 데이터가 주어질 때, 각 구역 별로 가장 긴 구조물의 길이를 찾는 프로그램을 만드시오.
'''

import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 끝 초기화를 위해 오른쪽과 아래에 0행, 0열 추가
    ary = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(M+1)]
    ans = 0

    # 행 기준
    for i in range(N+1):
        tmp = 0
        for j in range(M+1):
            if ary[i][j] == 1:  # 1이면 합계에 더하기
                tmp += 1
            else:  # 0이면 최대값 판별 이후 합계 초기화
                if ans < tmp:
                    ans = tmp
                tmp = 0

    # 열 기준
    for j in range(M+1):
        tmp = 0
        for i in range(N+1):
            if ary[i][j] == 1:  # 1이면 합계에 더하기
                tmp += 1
            else:  # 0이면 최대값 판별 이후 합계 초기화
                if ans < tmp:
                    ans = tmp
                tmp = 0
    print(f'#{tc} {ans}')




