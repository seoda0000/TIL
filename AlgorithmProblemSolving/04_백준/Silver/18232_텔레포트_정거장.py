from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())
dic = defaultdict(list)

v = [0] * (N + 1)
for _ in range(M):
    x, y = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)

v[S] = 1
q = deque([S])
ans = -1
while q:
    cur = q.popleft()

    if cur == E:
        ans = v[E] - 1
        break

    for nxt in dic[cur] + [cur - 1, cur + 1]:
        if nxt < 1 or nxt > N: continue
        if v[nxt]: continue
        v[nxt] = v[cur] + 1
        q.append(nxt)

print(ans)
