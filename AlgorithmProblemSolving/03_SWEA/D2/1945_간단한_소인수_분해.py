"""
1945 간단한 소인수 분해

숫자 N은 아래와 같다.

N=2^a x 3^b x 5^c x 7^d x 11^e

N이 주어질 때 a, b, c, d, e 를 출력하라.
"""


T = int(input())

for case in range(1, T + 1):
    N = int(input())

    lst = [2, 3, 5, 7, 11]
    ans = [0] * 5

    for n in range(5):
        while N % lst[n] == 0:  # 나머지가 생길 때까지 나누기
            N /= lst[n]  # 소인수분해
            ans[n] += 1  # 계수 증가
    print(f"#{case}", *ans)
