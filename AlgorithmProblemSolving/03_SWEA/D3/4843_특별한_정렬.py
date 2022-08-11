'''
4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬 D3
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.

10 1 9 2 8 3 7 4 6 5

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''
import sys
sys.stdin = open('s_input.txt', 'r')

# 최대값 인덱스 0, 최소값 인덱스 1로 옮기는 함수
def maxmin(ary):
    n = len(ary)
    mx = 0
    mn = 0
    for i in range(n):
        if ary[i] > ary[mx]:
            mx = i
    ary[0], ary[mx] = ary[mx], ary[0]
    for i in range(n):
        if ary[i] < ary[mn]:
            mn = i
    ary[1], ary[mn] = ary[mn], ary[1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = [0] * 10
    i = 0
    for i in range(5):
        maxmin(lst)
        ans[2*i+0] += lst[0] # 최대값 추가
        ans[2*i+1] += lst[1] # 최소값 추가

        # 길이 2 이상 줄이기
        if len(lst)>2:
            lst = lst[2:]

    print(f'#{tc}', *ans)
