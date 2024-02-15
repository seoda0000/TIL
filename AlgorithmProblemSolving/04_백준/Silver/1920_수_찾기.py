"""
https://www.acmicpc.net/problem/1920
백준 실버4 1920 수 찾기

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
"""

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
M = int(input())
mLst = list(map(int, input().split()))
ans = []
for target in mLst:
    s, e = 0, N - 1

    while s <= e:
        m = (s + e) // 2
        if lst[m] == target:
            ans.append(1)
            break
        elif lst[m] > target:
            e = m - 1
        else:
            s = m + 1
    else:
        ans.append(0)
print(*ans, sep="\n")
