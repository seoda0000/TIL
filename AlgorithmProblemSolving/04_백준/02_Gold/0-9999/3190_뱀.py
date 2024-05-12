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

"""
2차 풀이
"""

"""
3:28 시작
3:33 구상 완료
3:55 디버깅 완료

풀이시간: 31분 -> 27분 (단축)
실행시간: 148 -> 140 (단축)
메모리: 113164 (유지)

1차 와는 달리 set을 쓰지 않고 dic.keys를 사용하여 딕셔너리만으로 풀었다.
매 턴 시작마다 큐를 기준으로 머리와 꼬리 위치를 파악해줘서 구조는 간단해진 것 같다.
예전 설계가 기억나서 쉽게 풀었는데, 그래서 문제를 잘 읽지 않고 대충 풀어서 헤맨 감이 있다. (머리+꼬리 동시 이동 처리 오류)
문제를 제대로 읽는 연습도 함께 해야 한다. 처음 푸는 것처럼 꼼꼼히 읽자.
"""
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
SNAKE, APPLE = 1, 2
N = int(input())
apple_cnt = int(input())
arr = [[0] * N for _ in range(N)]

for _ in range(apple_cnt):
    i, j = map(int, input().split())
    arr[i - 1][j - 1] = APPLE
L = int(input())
order_dic = dict()  # 시점: 방향
for _ in range(L):
    x, c = input().split()
    order_dic[int(x)] = c
t = 1  # 시간
d = 0  # 방향
q = deque([(0, 0)])  # 뱀 좌표 큐
arr[0][0] = SNAKE
while True:

    hi, hj = q[0]
    ti, tj = q[-1]

    ni, nj = hi + di[d], hj + dj[d]

    if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] == SNAKE:  # 벽&뱀
        break
    elif arr[ni][nj] == APPLE:  # 사과
        q.appendleft((ni, nj))
        arr[ni][nj] = SNAKE
    else:  # 빈칸
        q.appendleft((ni, nj))
        arr[ni][nj] = SNAKE
        arr[ti][tj] = 0
        q.pop()

    if t in order_dic.keys():
        if order_dic[t] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

    t += 1

print(t)
