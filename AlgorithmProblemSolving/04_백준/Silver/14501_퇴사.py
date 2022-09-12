'''
퇴사
https://www.acmicpc.net/problem/14501
백준 실버3 14501

상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.

오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
'''


import sys
def input():
    return sys.stdin.readline().rstrip()


def dfs(nth, w):
    global ans
    if nth >= N:  # 종료 조건
        if ans < w:
            ans = w
        return
    dfs(nth+1, w)             # 해당 일에 일을 하지 않는 경우 : 그냥 넘어감
    if nth+arr[nth][0] <= N:  # 해당 일에 일을 하는 경우 : 소모 일수만큼 jump, 수익 추가
        dfs(nth+arr[nth][0], w+arr[nth][1])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, 0)
print(ans)



