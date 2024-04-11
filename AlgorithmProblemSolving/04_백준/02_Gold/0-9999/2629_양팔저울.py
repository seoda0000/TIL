"""
백준 골드3 2629
양팔저울
https://www.acmicpc.net/problem/2629

양팔 저울과 몇 개의 추가 주어졌을 때, 이를 이용하여 입력으로 주어진 구슬의 무게를 확인할 수 있는지를 결정하려고 한다.

무게가 각각 1g과 4g인 두 개의 추가 있을 경우, 주어진 구슬과 1g 추 하나를 양팔 저울의 양쪽에 각각 올려놓아 수평을 이루면 구슬의 무게는 1g이다. 또 다른 구슬이 4g인지를 확인하려면 1g 추 대신 4g 추를 올려놓으면 된다.

구슬이 3g인 경우 아래 <그림 1>과 같이 구슬과 추를 올려놓으면 양팔 저울이 수평을 이루게 된다. 따라서 각각 1g과 4g인 추가 하나씩 있을 경우 주어진 구슬이 3g인지도 확인해 볼 수 있다.



<그림 1> 구슬이 3g인지 확인하는 방법 (
$\boxed{1}$은 1g인 추,
$\boxed{4}$는 4g인 추, ●은 무게를 확인할 구슬)

<그림 2>와 같은 방법을 사용하면 구슬이 5g인지도 확인할 수 있다. 구슬이 2g이면 주어진 추를 가지고는 확인할 수 없다.

추들의 무게와 확인할 구슬들의 무게가 입력되었을 때, 주어진 추만을 사용하여 구슬의 무게를 확인 할 수 있는지를 결정하는 프로그램을 작성하시오.

"""
import sys
input = sys.stdin.readline

def f(num, w):
    if num > N:
        return

    if dp[num][w]:
        return

    dp[num][w] = 1

    if num == N:
        return

    f(num + 1, w)
    f(num + 1, w + weights[num])
    f(num + 1, abs(w - weights[num]))

N = int(input())
weights = list(map(int, input().split()))
M = int(input())
questions = list(map(int, input().split()))
answer = []
dp = [[0 for j in range((i + 1) * 500 + 1)] for i in range(N+1)]
f(0, 0)

for m in range(M):
    tw = questions[m]
    if tw > 50*300:
        answer.append('N')
    elif dp[N][tw]:
        answer.append('Y')
    else:
        answer.append('N')
print(*answer)