from collections import defaultdict

N = int(input())
M = int(input())
dic = defaultdict(list)
v = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

v[1] = 1

for friend in dic[1]:
    v[friend] = 1
    for ffriend in dic[friend]:
        v[ffriend] = 1

print(sum(v) - 1)
