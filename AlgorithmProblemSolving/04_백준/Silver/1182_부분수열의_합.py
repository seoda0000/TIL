"""
https://www.acmicpc.net/problem/1182
백준 실버2 1182 부분수열의 합

N개의 정수로 이루어진 수열이 있을 때,
크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""


def findNums(nth, sm):
    global ans

    if nth == N:
        if sm == M:
            ans += 1
        return

    findNums(nth + 1, sm)
    findNums(nth + 1, sm + nums[nth])
    return


N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
findNums(0, 0)
if M == 0:
    ans -= 1
print(ans)
