"""
9:39 시작
9:44 구상 완료
9:53 제출
"""
import sys

sys.stdin = open("input.txt", "r")


def turn(n, d):
    v[n] = 1

    # 양옆 확인
    if n > 0 and wheels[n - 1][2] != wheels[n][6]:
        if not v[n-1]: turn(n - 1, -d)
    if n < 3 and wheels[n + 1][6] != wheels[n][2]:
        if not v[n+1]: turn(n + 1, -d)

    # 돈다
    if d == 1:
        wheels[n].insert(0, wheels[n].pop())
    else:
        wheels[n].append(wheels[n].pop(0))

    return


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K = int(input())
    wheels = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        n, d = map(int, input().split())
        n -= 1
        v = [0] * 4
        turn(n, d)
    ans = 0
    for i in range(4):
        ans += wheels[i][0] * (2 ** i)
    print(f'#{test_case} {ans}')
