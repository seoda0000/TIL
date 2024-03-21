# 백준 14929 실버 5
# https://www.acmicpc.net/problem/14929
# 누적합, 분배법칙을 이용해서 풀면 된다.

N = int(input())
lst = list(map(int, input().split()))
pre_sum = 0
ans = 0
for i in range(N-1):
    pre_sum += lst[i]
    ans += lst[i+1] * pre_sum
print(ans)