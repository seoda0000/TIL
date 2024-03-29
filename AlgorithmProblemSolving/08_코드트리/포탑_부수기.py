"""
9:01 시작
9:15 구상 완료
9:46 1차 구현 완료
9:50 tc 디버깅 완료 및 코드 정리 시작
10:01 코드 점검 중 v 체크 실수 발견
10:07 공격자 제외 공격 오류 디버깅
10:14 공격자와 대상이 붙어있는 엣지 케이스 디버깅
10:15 제출

<실수한 부분>
제출 전 문제를 정독했어야 했는데 그러지 않았다.
처음 문제를 읽을 때 당연하다고 생각하고 건너띈 ' 공격자는 공격의 영향을 받지 않는다'를 빼먹어서 틀렸다.
이걸 처리하면서 불현듯 공격자와 대상이 바로 붙어 있는 경우를 떠올렸고 이 역시 디버깅했다.
엣지 케이스를 생각해보는 습관을 키워야 한다...

어제 bfs 방문 체크를 실수해서 한번 더 점검했다. 황당하게도 방문체크를 0으로 하고 있었다! 바로 바꿨다.
실수한 부분은 어처구니 없이 또 실수하니 주의깊게 살피자

마지막에 N, M의 개수를 꼭 세어보는데 도움이 되는 것 같다

<주의사항>
제출 이후 리펙토링으로 코드 정리랍시고 코드 순서를 수정했는데 또 오류가 났다!
완성 이후에 코드 로직 순서는 변경하지 말자!! 최적화하지 말고 문제 그대로 구현하자!!!!!


"""
from collections import deque


def laser(si, sj, ei, ej):  # si, sj에서 ei, ej로 가는 경로 리스트 return
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    q = deque([(si, sj, [(si, sj)])])  # (위치, 경로 리스트)

    while q:
        ci, cj, clst = q.popleft()
        for d in range(4):
            ni, nj = (ci + di[d]) % N, (cj + dj[d]) % M
            if v[ni][nj]: continue
            if arr[ni][nj] == 0: continue
            if ni == ei and nj == ej: return clst
            v[ni][nj] = 1
            q.append((ni, nj, clst + [(ni, nj)]))

    return []


def attck(i, j, power):  # i, j에 있는 포탑을 power의 공격력으로 공격 + 파괴 처리
    dic[(i, j)][0] -= power
    if dic[(i, j)][0] <= 0:
        dic.pop((i, j))
        arr[i][j] = 0
    return


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
tdi = [0, 1, 0, -1, 1, 1, -1, -1]
tdj = [1, 0, -1, 0, 1, -1, 1, -1]
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]  # 0: 이동불가, 1: 이동가능
dic = dict()  # 좌표: [공격력, 공격 시점]

for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(M):
        if ipt[j] > 0:
            arr[i][j] = 1
            dic[(i, j)] = [ipt[j], 0]

for k in range(1, K + 1):

    # 공격자, 공격대상 선정
    towers = []
    for key, value in dic.items():
        i, j = key
        atk_power, atk_time = value
        towers.append((atk_power, atk_time, i, j))

    if len(towers) == 1:  # 종료
        break
        
    towers.sort(key=lambda x: (x[0], -x[1], -(x[2] + x[3]), -x[3]))
    ap, _, ai, aj = towers[0]  # 공격자
    _, _, ti, tj = towers[-1]  # 공격 대상

    # 레이저 공격(경로)
    routes = laser(ai, aj, ti, tj)  # 공격에 휘말린 탑들

    if not routes:  # 레이저 공격 불가 -> 포탑 공격(주변)
        for d in range(8):
            ri, rj = (ti + tdi[d]) % N, (tj + tdj[d]) % M
            routes.append((ri, rj))

    # 공격
    battle_v = [[0] * M for _ in range(N)]  # 공격 연관 visited
    battle_v[ai][aj] = battle_v[ti][tj] = 1

    atk_power = ap + (N + M)  # 공격력
    dic[(ai, aj)] = [atk_power, k]  # 공격 기록
    attck(ti, tj, atk_power)  # 공격 대상 공격

    for ri, rj in routes:  # 대상 경로/주변 공격
        if arr[ri][rj] == 0: continue
        if ri == ai and rj == aj: continue
        battle_v[ri][rj] = 1
        attck(ri, rj, atk_power // 2)

    for i, j in dic.keys():  # 포탄 정비
        if battle_v[i][j]: continue
        dic[(i, j)][0] += 1

ans = max([value[0] for value in dic.values()])
print(ans)
