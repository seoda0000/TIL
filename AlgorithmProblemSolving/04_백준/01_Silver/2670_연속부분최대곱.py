"""
https://www.acmicpc.net/problem/2670
백준 실버4 연속부분최대곱
N개의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아, 그 곱을 출력하는 프로그램을 작성하시오.
예를 들어 아래와 같이 8개의 양의 실수가 주어진다면,
색칠된 부분의 곱이 최대가 되며, 그 값은 1.638이다.
"""
N = int(input())
lst = [float(input()) for _ in range(N)]
mx = max(lst)
pre = []
for n in range(N):
    mid = [lst[n]]
    for p in pre:
        mid.append(p*lst[n])
    pre = mid
    mx = max(max(mid), mx)


print(f'{round(mx, 3):.3f}')
