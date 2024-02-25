"""
시간복잡도 정확히 계산하기
문제 풀기 전에 엣지 케이스 만들기
엣지케이스 파일 만들기
zip 써보기
"""

import sys

input = sys.stdin.readline


def stick_stickers(nth):  # nth번째 스티커를 붙일 수 있으면 붙인다
    sticker = stickers[nth]
    for d in range(4):
        r = len(sticker)
        c = len(sticker[0])
        for ni in range(N - r + 1):
            for nj in range(M - c + 1):
                if check_with_note_point(ni, nj, sticker):
                    stick_with_note_point(ni, nj, sticker)
                    return
        sticker = turn_sticker(sticker)

    return


def turn_sticker(sticker):  # 90도 돌리기
    return list(zip(*sticker[::-1]))


def check_with_note_point(ni, nj, sticker):  # 노트북 ni, nj에 맞춰서 스티커를 붙일 수 있으면 True return
    r = len(sticker)
    c = len(sticker[0])
    for si in range(r):
        for sj in range(c):
            if sticker[si][sj] == 1 and note[ni + si][nj + sj] == 1:
                return False
    return True


def stick_with_note_point(ni, nj, sticker):  # 노트북 ni, nj에 맞춰서 스티커를 붙인다
    r = len(sticker)
    c = len(sticker[0])
    for si in range(r):
        for sj in range(c):
            if sticker[si][sj] == 1:
                note[ni + si][nj + sj] = 1
    return


N, M, K = map(int, input().split())
stickers = []
for _ in range(K):
    Ri, Ci = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(Ri)]
    stickers.append(sticker)
note = [[0] * M for _ in range(N)]

for k in range(K):
    stick_stickers(k)

ans = 0
for n in range(N):
    ans += sum(note[n])
print(ans)