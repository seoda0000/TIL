"""
https://www.acmicpc.net/problem/15654

백준 실버3 15654 N과 M (5)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열
"""


def f(nth):
    if nth == M:
        ans = []
        for m in range(M):  # 인덱스 순열 완성 후 인덱스에 해당하는 숫자를 채워준다
            ans.append(numbers[nthLst[m]])
        ansLst.append(ans)
        return

    for n in range(N):
        if n not in nthLst:
            nthLst.append(n)  # 아직 쓰지 않은 인덱스라면 기입
            f(nth + 1)  # 다음 인덱스 채우기
            nthLst.pop()  # clear


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
ansLst = []
nthLst = []  # 인덱스의 순열 표시
f(0)
ansLst.sort()

for ans in ansLst:
    print(*ans)
