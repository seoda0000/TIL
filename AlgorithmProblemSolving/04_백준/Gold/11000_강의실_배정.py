import sys

input = sys.stdin.readline

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort()
v = [0] * N
ans = 0


print(ans)
