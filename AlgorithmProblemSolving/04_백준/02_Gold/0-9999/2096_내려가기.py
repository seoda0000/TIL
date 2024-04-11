"""
https://www.acmicpc.net/problem/2096
백준 2096 골드 5 내려가기

메모리 이슈 주의
"""

N = int(input())
arr = list(map(int, input().split()))

mnarr = [x for x in arr]
mxarr = [x for x in arr]

for n in range(1, N):
    arr = list(map(int, input().split()))

    mn0, mn1, mn2 = mnarr
    mx0, mx1, mx2 = mxarr

    mnarr[0] = arr[0] + min(mn0, mn1)
    mxarr[0] = arr[0] + max(mx0, mx1)

    mnarr[1] = arr[1] + min(mn0, mn1, mn2)
    mxarr[1] = arr[1] + max(mx0, mx1, mx2)

    mnarr[2] = arr[2] + min(mn1, mn2)
    mxarr[2] = arr[2] + max(mx1, mx2)

print(max(mxarr), min(mnarr))
