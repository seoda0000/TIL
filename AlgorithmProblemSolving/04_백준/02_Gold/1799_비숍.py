"""
https://www.acmicpc.net/problem/1799
백준 골드1 1799 비숍
"""

import sys
from collections import defaultdict

input = sys.stdin.readline


# import math
# import time

# 시간 측정
# start = time.time()


def bishop(nth, cnt):
    global ansOdd, ansEven

    if nth >= 2 * N - 1:
        if nth % 2:
            ansOdd = max(ansOdd, cnt)
        else:
            ansEven = max(ansEven, cnt)
        return

    if nth % 2 and (cnt + 2 * N - 1 - nth <= ansOdd):
        return
    elif not (nth % 2) and (cnt + 2 * N - 1 - nth <= ansEven):
        return

    for item in rightDownDic[nth]:
        i, j = item
        if leftDown[i + j]: continue
        leftDown[i + j] = 1
        bishop(nth + 2, cnt + 1)
        leftDown[i + j] = 0
    bishop(nth + 2, cnt)


N = int(input())
ansOdd = 0
ansEven = 0
rightDownDic = defaultdict(list)
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]:
            rightDownDic[N - 1 + i - j].append((i, j))
Nr = len(rightDownDic)
leftDown = [0] * (2 * N - 1)
bishop(0, 0)
bishop(1, 0)
print(ansOdd + ansEven)

# 시간 측정
# end = time.time()
# print(f"{end - start:.5f} sec")
