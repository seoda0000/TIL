import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[N] * (N+1) for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A][B] = arr[B][A] = 1

for a in range(1, N+1):
    for b in range(1, N+1):
        for c in range(1, N+1):
            if arr[b][c] > arr[b][a] + arr[a][c]:
                arr[b][c] = arr[b][a] + arr[a][c]
answer = 0
mn = N*(N+1)
for i in range(1, N+1):
    if sum(arr[i]) < mn:
        mn = sum(arr[i])
        answer = i
print(answer)