"""
https://www.acmicpc.net/problem/1331
실버 4 1331 나이트 투어
"""


def checkKnight(bi, bj, ci, cj):
    if abs(bi - ci) == 2:
        if abs(bj - cj) != 1:
            return False

    elif abs(bi - ci) == 1:
        if abs(bj - cj) != 2:
            return False

    else:
        return False

    return True


ans = "Valid"
ipts = list(input() for _ in range(36))

if len(set(ipts)) != 36: # 중복 방문 제거
    ans = "Invalid"
else:
    si, sj = ord(ipts[0][0]) + 1 - ord("A"), int(ipts[0][1])

    # 시작점에서 출발
    bi, bj = si, sj

    for n in range(1, 36):
        ci, cj = ipts[n]
        ci, cj = ord(ci) + 1 - ord("A"), int(cj)

        if not checkKnight(bi, bj, ci, cj): # 다음 이동지점 체크
            ans = "Invalid"
            break

        bi, bj = ci, cj # 이동

    # 마지막에서 시작점으로 돌아오기
    ci, cj = si, sj
    if not checkKnight(bi, bj, ci, cj):
        ans = "Invalid"

print(ans)
