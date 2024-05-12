"""
실행시간: 868 -> 2700(최적화 192)
풀이시간: 24분 -> 30분

일전에는 도미노를 배열로 일일이 만들었다면 이번에는 준혁 프로님에게 들은대로 dfs를 활용해보았다.
기존 도미노 리스트의 인접한 칸을 한 칸씩 포함하며 체크하는 방식이다.
탐색했던 곳도 또 탐색하는 바람에 시간초과가 났다. 왼쪽 위부터 차례대로 해당 칸을 포함하는 모든 경우를 탐색한 후 v 배열을 이용해 이후부터는 배제했다.

처음엔 v_set을 활용해 기존에 순회했던 조합이면 중지시켰는데, 사실 dfs이므로 v배열에 표시만 잘한다면 같은 조합을 순회할 일은 드물다.
dfs를 차례대로 그려보면서 작동 원리를 이해한 후에 써야 한다. (스터디에서 내가 강조했는데 내가 안 하고 있다!!)
조합 체크는 최후의 수단으로 쓰자
"""


def solve(blocks, sm, cnt):
    global ans

    if sm + (4 - cnt) * mx <= ans:
        return

    if cnt == 4:
        ans = max(ans, sm)
        return

    # blocks.sort()
    # if str(blocks) in v_set:
    #     return
    # else:
    #     v_set.add(str(blocks))

    for b in blocks:
        bi, bj = divmod(b, M)
        for d in range(3):
            ni, nj = bi + di[d], bj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue

            v[ni][nj] = 1
            solve(blocks + [ni * M + nj], sm + arr[ni][nj], cnt + 1)
            v[ni][nj] = 0

    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = max([max(a) for a in arr])
ans = 0
# v_set = set()
v = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        v[i][j] = 1
        solve([i * M + j], arr[i][j], 1)
print(ans)

"""
15:16~15:24 구상
15:24~15:40 구현

list(zip(*arr))를 쓸 때 *를 빼먹었다! *를 잊지 말자.
도미노 리스트를 함수로 만드니까 IDE에서 코드를 접어서 생략할 수 있어서 깔끔하게 풀 수 있었다.
다음에는 주석을 먼저 적고 코딩하면 더욱 깔끔할 것 같다.

if문 판정이 *배열 연산보다 빠르다
zip은 느리지만 동작이 명확하므로 계속 사용할 것 같다
"""


def get_dominos():  # 도미노 리스트 얻기
    dominos = [
        [[1, 1],
         [1, 1]],
        [[1, 1, 1, 1]],
        [[1], [1], [1], [1]]
    ]

    # 4번 돌리기 + 뒤집어서 4번 돌리기
    domino_a = [
        [1, 0],
        [1, 0],
        [1, 1]
    ]
    for i in range(4):
        domino_a = list(zip(*domino_a[::-1]))
        dominos.append(domino_a)
    domino_a = [row[::-1] for row in domino_a]
    for i in range(4):
        domino_a = list(zip(*domino_a[::-1]))
        dominos.append(domino_a)

    # 2번 돌리기 + 뒤집어서 2번 돌리기
    domino_b = [
        [1, 0],
        [1, 1],
        [0, 1]
    ]
    for i in range(2):
        domino_b = list(zip(*domino_b[::-1]))
        dominos.append(domino_b)
    domino_b = [row[::-1] for row in domino_b]
    for i in range(2):
        domino_b = list(zip(*domino_b[::-1]))
        dominos.append(domino_b)

    # 4번 돌리기
    domino_c = [
        [1, 1, 1],
        [0, 1, 0]
    ]
    for i in range(4):
        domino_c = list(zip(*domino_c[::-1]))
        dominos.append(domino_c)

    return dominos


def check_domino(domino):  # 판에 도미노 대보고 최대합 갱신
    R = len(domino)
    C = len(domino[0])

    for si in range(N - R + 1):
        for sj in range(M - C + 1):
            check_sum(si, sj, domino)
    return


def check_sum(si, sj, domino):  # 판 si, sj 위치부터 시작해서 총합 구하고 최대합 갱신
    global ans

    R = len(domino)
    C = len(domino[0])

    sm = 0

    for i in range(R):
        for j in range(C):
            if domino[i][j]:
                sm += arr[si + i][sj + j]

    ans = max(sm, ans)
    return


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dominos = get_dominos()
ans = 0

for domino in dominos:
    check_domino(domino)  # 판에 도미노 대보기

print(ans)
