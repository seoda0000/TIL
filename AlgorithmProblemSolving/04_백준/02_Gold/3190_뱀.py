"""
3시 18분 구상 끝
3시 31분 구현 끝

사다리를 풀다가 안되겠다 싶어서 이 문제를 시작했다.
다행히 문제를 읽자마자 바로 큐를 활용한 방안이 떠올랐고 빠르게 진행할 수 있었다.
떠오르지 않으면 배웠던 알고리즘을 하나하나 생각해보는 것도 좋을 것 같다.
"""
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    ai, aj = map(int, input().split())
    arr[ai - 1][aj - 1] = 2  # 사과

time_st = set()
time_dic = dict()
L = int(input())
for _ in range(L):
    x, c = input().split()
    time_st.add(int(x))
    time_dic[int(x)] = c

hi, hj = 0, 0  # 머리 위치
ti, tj = 0, 0  # 꼬리 위치
arr[hi][hj] = 1
d = 0  # 방향
q = deque([(hi, hj)])
time = 1
while True:
    ni, nj = hi + di[d], hj + dj[d]

    if not (0 <= ni < N and 0 <= nj < N): break  # 게임 종료
    if arr[ni][nj] == 1: break  # 게임 종료

    if arr[ni][nj] == 2:  # 사과 있다
        hi, hj = ni, nj  # 머리 이동
        arr[hi][hj] = 1
        q.append((hi, hj))

    else:  # 사과 없다

        hi, hj = ni, nj  # 머리 이동
        arr[hi][hj] = 1
        q.append((hi, hj))

        ti, tj = q.popleft()  # 꼬리 이동
        arr[ti][tj] = 0

    if time in time_st:
        direction = time_dic[time]

        if direction == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

    time += 1

    # 방향 전환
print(time)
