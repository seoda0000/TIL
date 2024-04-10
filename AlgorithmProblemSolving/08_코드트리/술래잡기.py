"""
실행시간: 319 -> 263
풀이시간: 67분 -> 33분

자체 tc로 디버깅 했던 것이 기억나서 이번에도 했다. 아니나 다를까 오류를 잡을 수 있었다!
(0, N//2 중 하나면 돌도록 -> 0, 0 or N//2, N//2면 돌도록)
특정 지점은 귀찮다고 리스트로 하지 말고 무조건 ==으로 비교하자.
이전에는 딕셔너리로 구현했는데, 이번엔 그냥 3차원 배열로 구현했다. 로직은 완전히 동일하다.
"""

"""
10:15 시작
10:22 구상 완료
10:43 1차 구현 완료
10:48 자체 tc 디버깅 완료
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, runner_cnt, tree_cnt, K = map(int, input().split())
arr = [[list() for _ in range(N)] for _ in range(N)]
tree_arr = [[0] * N for _ in range(N)]
v = [[0] * N for _ in range(N)]
for _ in range(runner_cnt):
    x, y, d = map(int, input().split())
    if d == 1:
        d = 0
    else:
        d = 1
    arr[x - 1][y - 1].append(d)
for _ in range(tree_cnt):
    x, y = map(int, input().split())
    tree_arr[x - 1][y - 1] = 1

si, sj = N // 2, N // 2
sd = 3
status = 0
v[si][sj] = 1
ans = 0

for k in range(1, K + 1):

    # 도망자 이동
    new_arr = [[list() for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not arr[i][j]: continue
            if abs(i - si) + abs(j - sj) > 3:  # 이동 x
                new_arr[i][j].extend(arr[i][j])
                continue

            for rd in arr[i][j]:
                ni, nj = i + di[rd], j + dj[rd]
                if OOB(ni, nj):
                    rd = (rd + 2) % 4  # 반대로
                    ni, nj = i + di[rd], j + dj[rd]

                if ni == si and nj == sj:
                    new_arr[i][j].append(rd)  # 이동 x
                else:
                    new_arr[ni][nj].append(rd)

    arr = new_arr

    # 술래 이동
    si, sj = si + di[sd], sj + dj[sd]  # 일단 간다
    if (si == 0 and sj == 0) or (si == N // 2 and sj == N // 2):  # 반환점
        status ^= 1
        sd = (sd + 2) % 4
        v = [[0] * N for _ in range(N)]
    elif not status:  # 안에서 밖으로
        nd = (sd + 1) % 4  # 그리고 돈다
        ni, nj = si + di[nd], sj + dj[nd]
        if not v[ni][nj]:
            sd = nd
    else:  # 밖에서 안으로
        ni, nj = si + di[sd], sj + dj[sd]
        if OOB(ni, nj) or v[ni][nj]:
            sd = (sd - 1) % 4

    v[si][sj] = 1

    # 도망자 잡기
    ei, ej = si, sj
    for _ in range(3):
        if OOB(ei, ej): break
        if not tree_arr[ei][ej] and arr[ei][ej]:  # 잡는다
            ans += k * len(arr[ei][ej])
            arr[ei][ej] = []
        ei, ej = ei + di[sd], ej + dj[sd]

print(ans)

"""
9:00 시작
9:14 구상 완료
9:51 1차 구현 완료, 휴식 시작
9: 54 휴식 끝
10:00 자체 테스트 케이스 점검 -> 범위 오류 디버깅
10:07 코드 검토 완료

달팽이 이동+방향 전환이 까다로운 문제였다. 바깥/안으로 나누고 어떤 경우에 방향이 전환되는지 차근차근 확인했다.
단순무식한 방법으로 모든 곳에서 적용 가능하도록 조건문으로 처리했다.

처음에 도망자의 위치를 3차원 array에 표시했는데, N이 99로 커서 시간초과가 날 수도 있겠다는 생각이 구현 중에 들었다.
따라서 중간에 defaultdic으로 자료구조를 바꿨다. 이 생각을 구현중에 했다면 조금 덜 긴장하며 풀 수 있었겠지...

<잘한 점>
제출 전에 잘 돌아가는지 디버거를 통해 술래의 경로를 체크했다. (N=3 50턴) 그러다가 술래의 시야에서 인덱스 에러가 나서 범위 조건을 추가했다.
체크하지 않았다면 틀렸을 것 같다...
꼭 극단적인 input으로 디버깅 해보도록 하자

배영석 프로님께 OOB, dictionary.pop등을 배워서 적용했다
"""
from collections import defaultdict


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


di = [-1, 0, 1, 0]  # 위, 오, 아, 왼
dj = [0, 1, 0, -1]
N, runner_cnt, tree_cnt, K = map(int, input().split())
tree_arr = [[0] * N for _ in range(N)]
runner_dic = defaultdict(list)
for _ in range(runner_cnt):
    x, y, d = map(int, input().split())
    runner_dic[(x - 1, y - 1)].append(d)
for _ in range(tree_cnt):
    x, y = map(int, input().split())
    tree_arr[x - 1][y - 1] = 1

si, sj = N // 2, N // 2  # 술래 위치
sd = 0  # 술래 방향
state = 0  # 술래 상태: 0-바깥쪽으로, 1-안쪽으로
v = [[0] * N for _ in range(N)]  # 술래가 왔던 길 표시
v[si][sj] = 1

ans = 0
for turn in range(1, K + 1):
    # 도망자가 이동한다
    nxt_runner_dic = defaultdict(list)

    for key, values in runner_dic.items():
        i, j = key
        if abs(si - i) + abs(sj - j) > 3:  # 술래와의 거리가 3 초과
            nxt_runner_dic[key].extend(values)
        else:  # 이동할 도망자들
            for rd in values:
                ni, nj = i + di[rd], j + dj[rd]

                if OOB(ni, nj):  # 범위 밖 -> 반대로
                    rd = (rd + 2) % 4
                    ni, nj = i + di[rd], j + dj[rd]

                if ni == si and nj == sj:  # 술래칸
                    nxt_runner_dic[(i, j)].append(rd)  # 이동 x
                else:  # 빈칸
                    nxt_runner_dic[(ni, nj)].append(rd)  # 이동 o

    runner_dic = nxt_runner_dic

    # 술래가 이동한다
    si += di[sd]
    sj += dj[sd]

    # 술래의 방향 조정
    if (si == 0 and sj == 0) or (si == N // 2 and sj == N // 2):  # 끝점 도달: 뒤돌아선다
        state ^= 1
        sd = 2 * state
        v = [[0] * N for _ in range(N)]

    else:
        if state:  # 안쪽으로 움직일 때
            ni, nj = si + di[sd], sj + dj[sd]  # 시야각 확인
            if OOB(ni, nj) or v[ni][nj]: sd = (sd - 1) % 4  # 방향 전환

        else:  # 바깥쪽으로 움직일 때
            nd = (sd + 1) % 4
            ni, nj = si + di[nd], sj + dj[nd]  # 시야각 확인
            if not v[ni][nj]: sd = nd  # 방향 전환

    v[si][sj] = 1  # 이동 표시

    # 도망자를 잡는다
    vi, vj = si, sj
    for _ in range(3):
        if OOB(vi, vj): break
        if not tree_arr[vi][vj] and runner_dic[(vi, vj)]:  # 나무가 없고 도망자가 있으면 잡는다
            ans += turn * len(runner_dic.pop((vi, vj)))
        vi += di[sd]
        vj += dj[sd]

print(ans)
