"""
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
"""

T = int(input())

for case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    # 초기값 설정
    mn = 1000000
    mx = 0



    for n in lst:
        if n < mn: # 최소값 찾기
            mn = n
        if n > mx: # 최대값 찾기
            mx = n
    ans = mx - mn
    print(f"#{case} {ans}")
