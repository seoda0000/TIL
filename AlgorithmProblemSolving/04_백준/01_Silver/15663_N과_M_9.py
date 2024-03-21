"""
https://www.acmicpc.net/problem/15663

백준 실버3 15654 N과 M (9)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

"""
str과 int의 정렬 기준이 다르다.
str : 10 < 9
int : 10 > 9
"""


def f(nth):
    if nth == M:
        # 인덱스 순열 완성 후 인덱스에 해당하는 숫자를 채워준다
        ans = [numbers[nthLst[m]] for m in range(M)]
        ansLst.append(tuple(ans))  # set 처리를 위해 tuple로
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
ansLst = list(set(ansLst))
ansLst.sort()

for ans in ansLst:
    print(*ans)
