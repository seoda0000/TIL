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


v = [[0] * 7 for _ in range(7)]
ans = "Valid"
ipts = list(input() for _ in range(36))

if len(set(ipts)) != 36:
    ans = "Invalid"
else:
    bi, bj = ord(ipts[0][0]) + 1 - ord("A"), int(ipts[0][1])
    v[bi][bj] = 1

    for n in range(1, 36):
        ci, cj = ipts[n]
        ci, cj = ord(ci) + 1 - ord("A"), int(cj)

        if v[ci][cj]:
            ans = "Invalid"
            break

        if not checkKnight(bi, bj, ci, cj):
            ans = "Invalid"
            break

        v[ci][cj] = 1

        bi, bj = ci, cj

    ci, cj = ord(ipts[0][0]) + 1 - ord("A"), int(ipts[0][1])

    if not checkKnight(bi, bj, ci, cj):
        ans = "Invalid"

print(ans)
