"""
https://www.acmicpc.net/problem/11659
백준 실버3 11659 구간 합 구하기 4
"""
N, M = map(int, input().split())
nums = list(map(int, input().split()))
smLst = [0] * (N + 1)
for n in range(1, N + 1):
    smLst[n] = smLst[n - 1] + nums[n - 1]

for m in range(M):
    s, e = map(int, input().split())
    print(smLst[e] - smLst[s - 1])
