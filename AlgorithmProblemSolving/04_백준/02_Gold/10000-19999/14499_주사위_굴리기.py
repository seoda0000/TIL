"""
15:26 문제 읽기 시작
15:55 구상 완료
16:10 구현 완료

나는 입체 도형이 싫다...
공간지각력이 없어서 단순히 주사위 굴리는 것 자체도 머릿속에서 구현이 되지 않았다...
처음엔 주사위 전개도 배열을 만드려고 했는데 전개도도 이해 못해서 포기했다.
(이 방법 쓰신 분(준환 프로님, 석의 프로님)도 계시는데 여쭤봐야 할듯... 이해 못했다)
이쯤에서 머리 쓰는 걸 포기하고 겸허하게 천천히 모두 그리기 시작했다.
그림을 그려서 겨우 이해했다. 천장이 중심인 십자가를 단계 별로 하나하나 그렸다. 회전 시 각 위치별 규칙을 확인해서 겨우 풀었다...
정말 괴롭다

주사위 돌리기만 해결하면 다른 조건은 구현하기 쉽다.
함수를 만들까 싶었는데 값 6개를 바꿔야 해서 오히려 복잡할 것 같았다.
명확한 변수명이 도움이 되었다.
"""

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]
N, M, si, sj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

front = back = ceiling = ground = left = right = 0
ans = []
ci, cj = si, sj
for order in orders:
    ni, nj = ci + di[order], cj + dj[order]

    if not (0 <= ni < N and 0 <= nj < M): continue

    if order == 1:  # 동
        ceiling, ground, left, right = left, right, ground, ceiling

    elif order == 2:  # 서
        ceiling, ground, left, right = right, left, ceiling, ground

    elif order == 3:  # 북
        ceiling, ground, front, back = front, back, ground, ceiling

    elif order == 4:  # 남
        ceiling, ground, front, back = back, front, ceiling, ground

    ans.append(ceiling)
    if arr[ni][nj] == 0:
        arr[ni][nj] = ground
    else:
        ground = arr[ni][nj]
        arr[ni][nj] = 0

    ci, cj = ni, nj

print(*ans, sep='\n')
