"""
https://www.acmicpc.net/problem/20529

백준 20529 실버1 가장 가까운 세 사람의 심리적 거리

ㅂㄷㄱㅈ ㅇㄹ  참고
"""

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(input().split())
    if N > 32:
        print(0)
    else:
        ans = 100001
        for i in range(N - 1):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    sm = len(set(lst[i]) - set(lst[j])) + len(set(lst[i]) - set(lst[k])) + len(
                        set(lst[k]) - set(lst[j]))
                    if sm < ans:
                        ans = sm
        print(ans)
