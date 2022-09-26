N = int(input())
lst = list(map(int, input().split()))
n = max(lst)
for i in range(N):
    if lst[i] != n:
        lst[i] = lst[i]/n*100
ans = sum(lst)/N
print(ans)