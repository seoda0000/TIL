from collections import deque

N, K = map(int, input().split())
q = deque(list(range(1, N+1)))
p = 1
ans = []
while q:
    if p == K:
        ans.append(q.popleft())
        p = 1
    else:
        q.append(q.popleft())
        p += 1
print("<", end="")
for a in ans[:-1]:
    print(a, end=", ")
print(ans[-1], end="")
print(">")

