from collections import defaultdict

# N = int(input())
# columns = list(map(int, input().split()))
N = len(list(range(1, 10**9+1, 3500)))
columns = list(range(1, 10**9+1, 3500))
mx = max(columns)
cnts = [0]*(mx+1)
ans = 0
for h in columns:
    print('...')
    for i in range(ans, h+1):
        cnts[i] += 1
        if cnts[i] >= i:
            ans = i
    cnts[h+1:] = [0]*(mx-h)
print(ans)
