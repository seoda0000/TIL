'''
4466. 최대 성적표 만들기 D3
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWOUfCJ6qVMDFAWg&

당신은 N개의 과목에 대한 시험을 쳤다. 각 과목의 점수는 정수이고 만점은 100점이다.

성적표에는 이 중에서 정확히 K개의 과목을 선택하여 넣을 수 있다. 당신은 기왕이면 성적표에 나타나는 총점이 가장 크도록 성적표를 만들고 싶다.

최대로 만들 수 있는 총점은 몇점인지 구하여라.
'''

import sys
sys.stdin = open('sample_input (1).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0  # 합계

    for i in range(K):
        mxIdx = 0  # 최대값 인덱스
        for n in range(N):
            if lst[n] > lst[mxIdx]:  # 인덱스 n 값이 더 크면 최대값 인덱스 갱신
                mxIdx = n
        ans += lst[mxIdx]  # 합계에 더하기
        lst[mxIdx] = 0  # 더한 인덱스 값 0으로 만들어서 후보에서 제외
    print(f'#{tc} {ans}')