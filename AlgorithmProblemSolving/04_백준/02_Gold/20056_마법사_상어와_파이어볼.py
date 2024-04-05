"""
실행시간: 288 -> 316
풀이시간: 48분 -> 14분

풀이방식은 이전과 완전히 동일하다. 함수화를 안한 정도?
질량 합을 개수로 잘못 봐서 틀렸다. 다 푼 후에 구상과의 일치 여부를 검토하자.
"""

"""
9:27 시작
9:31 구상 완료
9:45 구현 완료
9:47 dic.items 디버깅
9:51 개수 -> 질량합 디버깅
"""
from collections import defaultdict

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
N, atom_cnt, K = map(int, input().split())
dic = defaultdict(list)  # (질량, 속력, 방향)

for _ in range(atom_cnt):
    x, y, m, s, d = map(int, input().split())
    dic[(x - 1, y - 1)].append((m, s, d))

for _ in range(K):

    # 모든 원자 동시 이동
    moved_dic = defaultdict(list)

    for key, values in dic.items():
        ci, cj = key

        for m, s, d in values:
            ni, nj = (ci + di[d] * s) % N, (cj + dj[d] * s) % N
            moved_dic[(ni, nj)].append((m, s, d))

    dic = moved_dic

    # 쪼개진다...
    dic_item_lst = list(dic.items())
    for key, values in dic_item_lst:
        if len(values) <= 1: continue
        sm_m = sm_s = 0
        d_set = set()

        for m, s, d in values:  # (질량, 속력, 방향)
            sm_m += m
            sm_s += s
            d_set.add(d % 2)
        nm = sm_m // 5  # 질량
        ns = sm_s // len(values)  # 속력

        if not nm:  # 소멸
            dic.pop(key)
            continue

        atom_lst = []
        if len(d_set) == 1:  # 상하좌우
            d_lst = [0, 2, 4, 6]
        else:
            d_lst = [1, 3, 5, 7]

        for d in d_lst:
            atom_lst.append((nm, ns, d))

        dic[key] = atom_lst

ans = 0
for values in dic.values():
    for value in values:
        ans += value[0]

print(ans)

"""
구상은 언제 끝났는지 영상 확인해봐야 할듯
15:48 풀이 완료

구현 후에 시간 복잡도를 계산했다. 솔직히 아직도 모르겠음... 기출이라 배 째고 푼 것 같다...
인덱스 감소 처리헤서 input을 받는 등 설계를 세세하게 하려고 노력했고 도움이 되었다.

테스트케이스를 손으로 그려본 것도 도움이 되었다. -> 구현 이후 테케 확인에 큰 도움!
생각하지 않고 문제를 그대로 구현하는 것... 그것이 구현

defaultdict을 쓸지 v 배열을 이용할지 엄청 고민하다가 확실하고 익숙한 방법인 defaultdict을 사용했다.
같은 자리에 몇개 있는지 체크하기 위해 defaultdict를 사용했다. {좌표:[파이어볼 목록]}
이동 처리에는 순회하기 편하도록 defaultdict을 단순 list로 변환하여 구현하였다.
굳이 그랬어야 했는지...? 코드는 깔끔해졌지만 dict와 list의 데이터 형태가 통일되지 않아서 살짝 신경쓰였다.
-> 하지만 기존 방법이 덜 헷갈리는 것 같다... 형태는 꼼꼼히 체크하자

손코딩 시 K마다 defaultdict를 만들어야 하는지 등 디테일까지 모두 설계했다. 훨씬 명쾌함! 코드로 고민하지 말고 필기로 고민하자.

방향 처리의 경우 이전 전준혁 프로님 코드를 참고했다. (0-1)%N -> N-1이 나온다. 덕분에 훨씬 쉽게 구현한 것 같다
테스트케이스, 파이썬 동작 확인 파일 등 따로 만드니까 편리하다.
변수명도... 일전에 d 때문에 헷갈렸는데 for d 까지 치고 고쳤다. 길어도 되니까 명확한 변수명을 활용하자

value -> values로 변경
복수 변수명은 꼭 복수 표현을 하자

dict 대신 3차원 배열 쓰기 시도 -> dict가 더 빠름
"""
from collections import defaultdict
import sys

input = sys.stdin.readline


def move(lst):  # fireballs lst로 다음 위치를 담은 dic 얻기
    dic = defaultdict(list)

    for fireball in lst:
        ci, cj, cm, cs, cd = fireball
        ni, nj = (ci + di[cd] * cs) % N, (cj + dj[cd] * cs) % N
        dic[(ni, nj)].append((cm, cs, cd))

    return dic


def bbang(dic):  # fireballs dic로 남은 파이어볼을 담은 lst 얻기
    lst = []
    for key, values in dic.items():
        if len(values) >= 2:  # 2개 이상 같은 칸
            sm_m = 0
            sm_s = 0
            sm_d = []

            for v in values:
                sm_m += v[0]
                sm_s += v[1]
                sm_d.append(v[2] % 2)

            m = int(sm_m / 5)
            if m:  # 질량 1 이상인 경우
                s = int(sm_s / len(values))
                if len(set(sm_d)) == 1:
                    d_lst = [0, 2, 4, 6]
                else:
                    d_lst = [1, 3, 5, 7]

                i, j = key
                for d in range(4):
                    lst.append((i, j, m, s, d_lst[d]))
            else:  # 질량 0인 경우
                continue

        else:  # 한 칸에 하나
            i, j = key
            m, s, d = values[0]
            lst.append((i, j, m, s, d))
    return lst


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    i, j, m, s, d = map(int, input().split())
    fireballs.append(((i - 1) % N, (j - 1) % N, m, s, d))

for _ in range(K):
    fire_dic = move(fireballs)
    fireballs = bbang(fire_dic)

ans = 0
for fireball in fireballs:
    ans += fireball[2]  # 질량의 합

print(ans)

"""
dict 대신 3차원 배열 쓰기 시도
"""


def move(lst):  # fireballs lst로 다음 위치를 담은 arr 얻기
    arr = [[list() for _ in range(N)] for _ in range(N)]

    for fireball in lst:
        ci, cj, cm, cs, cd = fireball
        ni, nj = (ci + di[cd] * cs) % N, (cj + dj[cd] * cs) % N
        arr[ni][nj].append((cm, cs, cd))

    return arr


def bbang(arr):  # fireballs arr로 남은 파이어볼을 담은 lst 얻기
    lst = []
    for i in range(N):
        for j in range(N):
            values = arr[i][j]
            if not values:
                continue

            elif len(values) >= 2:  # 2개 이상 같은 칸
                sm_m = 0
                sm_s = 0
                sm_d = []

                for v in values:
                    sm_m += v[0]
                    sm_s += v[1]
                    sm_d.append(v[2] % 2)

                m = int(sm_m / 5)
                if m:  # 질량 1 이상인 경우
                    s = int(sm_s / len(values))
                    if len(set(sm_d)) == 1:
                        d_lst = [0, 2, 4, 6]
                    else:
                        d_lst = [1, 3, 5, 7]

                    for d in range(4):
                        lst.append((i, j, m, s, d_lst[d]))
                else:  # 질량 0인 경우
                    continue

            else:  # 한 칸에 하나
                m, s, d = values[0]
                lst.append((i, j, m, s, d))
    return lst


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    i, j, m, s, d = map(int, input().split())
    fireballs.append(((i - 1) % N, (j - 1) % N, m, s, d))

for _ in range(K):
    fireballs = bbang(move(fireballs))

ans = 0
for fireball in fireballs:
    ans += fireball[2]  # 질량의 합

print(ans)
