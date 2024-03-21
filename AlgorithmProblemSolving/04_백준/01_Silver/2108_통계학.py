import sys

input = sys.stdin.readline

N = int(input())
lst = [0]*8001
for n in range(N):
    lst[int(input())+4000] += 1
mn = 4000
mx = -4000
sm = 0
manyCan = max(lst)
cnt = 0
median = -4001
isFindMany = False
many = -4001
for n in range(8001):
    if lst[n] != 0 and mn == 4000:
        mn = n-4000
    if lst[n] != 0:
        mx = n-4000
        cnt += lst[n]
        if cnt >= int(N/2)+1 and median == -4001:
            median = n-4000
    if lst[n] == manyCan and many == -4001 and not isFindMany:
        many = n-4000
    elif lst[n] == manyCan and not isFindMany:
        many = n-4000
        isFindMany = True

    sm += (n-4000) * lst[n]


mean = round(sm / N)
range = mx - mn
print(mean)
print(median)
print(many)
print(range)