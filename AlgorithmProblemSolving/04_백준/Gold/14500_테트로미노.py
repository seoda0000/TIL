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
