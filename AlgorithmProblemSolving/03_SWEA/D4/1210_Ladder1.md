# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
https://swexpertacademy.com/main/code/problem/problemDetail.do

점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라 (‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).

---

```python

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    ary = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ary[99][i] == 2:
            x = i  # 출구 x 좌표
            break
    y = 99
    while y:
        ary[y][x] = 0  # 왔던 길 표시
        if x>=1 and ary[y][x-1]:  # 범위 내 왼쪽에 길이 있을 때 이동
            x -= 1
        elif x<=98 and ary[y][x+1]:  # 범위 내 오른쪽에 길이 있을 때 이동
            x += 1
        else:  # 양옆에 길이 없으면 위로 이동
            y -= 1
    print(f'#{tc}', x)
```

* 왔던 길을 표시하니까 런타임 에러가 떴다.
* 왔던 길을 표시하지 않고 탐색을 최소화 하도록 방향 전환시 길 끝까지 이동하는 방법으로 돌렸다. (while 사용)

```python
import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    ary = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    for i in range(102):
        if ary[99][i] == 2:
            x = i # 출구 x 좌표
            break
    y = 99
    while y:
        if ary[y][x-1]: # 왼쪽에 길이 있을 경우
            while ary[y][x-1]: # 길이 끊길 때까지 이동
                x -= 1
        elif ary[y][x+1]: # 오른쪽에 길이 있을 경우
            while ary[y][x+1]: # 길이 끊길 때까지 이동
                x += 1
        y -= 1 # 위로 이동
    print(f'#{tc}', x-1) # 0으로 둘러싸줬으므로 1 빼주기
```

* range 값을 실수로 11로 넣어서 계속 런타임 에러가 떴다. 주의하자...
* 0으로 둘러쌌다는 사실을 잊고 마지막에 x 좌표 처리를 하지 않았다. 늘 인덱스에 주의하자.

