"""
첫번째 풀이
"""


def printMagicStar():
    p = 0
    for i in range(5):
        for j in range(9):
            if magicStarPrint[i][j] == 'x':
                magicStarPrint[i][j] = chr(points[p][0] + ord('A') - 1)
                p += 1
        print("".join(magicStarPrint[i]))
    return


def fillIdx(nth, magicStar, visitedNum):  # nth번째 idx의 값 채우기
    global findAnswer
    if findAnswer:
        return
    if nth == N:
        isMagic = True

        for c in range(6):
            sm = 0
            for k in magicStar[c]:
                sm += k[0]
            if sm != 26:
                isMagic = False

        if isMagic:
            printMagicStar()
            findAnswer = True
        return

    for i in range(N):  # 아직 사용하지 않은 num으로
        if visitedNum[i]: continue

        visitedNum[i] = 1
        points[idxLst[nth]][0] = numLst[i]

        fillIdx(nth + 1, magicStar, visitedNum)
        visitedNum[i] = 0
    return


points = [[0] for _ in range(12)]
magicStar = [
    [points[0], points[2], points[5], points[7]],
    [points[1], points[2], points[3], points[4]],
    [points[0], points[3], points[6], points[10]],
    [points[7], points[8], points[9], points[10]],
    [points[1], points[5], points[8], points[11]],
    [points[4], points[6], points[9], points[11]],
]
magicStarPrint = [list("....x...."),
                  list(".x.x.x.x."),
                  list("..x...x.."),
                  list(".x.x.x.x."),
                  list("....x....")]
arr = [list(input()) for _ in range(5)]
p = 0
idxLst = list(range(12))
numLst = list(range(1, 13))
for row in arr:
    for r in row:
        if r != '.':
            if r != 'x':
                points[p][0] = ord(r) + 1 - ord('A')
                numLst.pop(numLst.index(ord(r) + 1 - ord('A')))
                idxLst.pop(idxLst.index(p))
            p += 1
N = len(idxLst)
visitedNum = [0] * N
findAnswer = False
fillIdx(0, magicStar, visitedNum)

"""
두번째 풀이
"""


def printMagicStar():
    p = 0
    for i in range(5):
        for j in range(9):
            if magicStarPrint[i][j] == 'x':
                magicStarPrint[i][j] = chr(points[p] + ord('A') - 1)
                p += 1
        print("".join(magicStarPrint[i]))
    return


def checkLineSum(lineNum):
    sm = 0
    for idx in magicStarRowIdx[lineNum]:
        sm += points[idx]
    if sm == 26:
        return True
    return False


def makeMagicStar(idx):
    # 인덱스 0~4번째까지 채운 후
    # 첫번째 줄 합이 26인지 체크
    if idx == 5:
        if checkLineSum(0) is False:
            return

    # 인덱스 5~7번째까지 채운 후
    # 두번째 줄 합이 26인지 체크
    elif idx == 8:
        if checkLineSum(1) is False:
            return

    # 인덱스 8~10번째까지 채운 후
    # 세번째 줄 합이 26인지 체크
    # 네번째 줄 합이 26인지 체크
    elif idx == 11:
        if checkLineSum(2) is False:
            return
        if checkLineSum(3) is False:
            return

    # 인덱스 11번까지 채운 후
    # 다섯번째 줄 합이 26인지 체크
    # 여섯번째 줄 합이 26인지 체크
    elif idx == 12:
        if checkLineSum(4) is False:
            return
        if checkLineSum(5) is False:
            return
        # 프린트
        printMagicStar()
        exit()

    # idx번째 포인트가 채워져 있으면 다음 포인트로
    if visitedIdx[idx]:
        makeMagicStar(idx + 1)

    # idx번째 포인트를 채운다
    else:
        for n in range(1, 13):
            if visitedNum[n]: continue
            visitedNum[n] = 1  # 사용한 숫자 check
            points[idx] = n
            makeMagicStar(idx + 1)
            visitedNum[n] = 0

    return


points = [0] * 12
magicStarRowIdx = [
    [1, 2, 3, 4],
    [0, 2, 5, 7],
    [7, 8, 9, 10],
    [0, 3, 6, 10],
    [1, 5, 8, 11],
    [4, 6, 9, 11]
]
magicStarPrint = [list("....x...."),
                  list(".x.x.x.x."),
                  list("..x...x.."),
                  list(".x.x.x.x."),
                  list("....x....")]
arr = [list(input()) for _ in range(5)]
p = 0
visitedNum = [0] * 13
visitedIdx = [0] * 12
numLst = list(range(1, 13))
idxLst = list(range(12))
for row in arr:
    for r in row:
        if r != '.':
            if r != 'x':  # 채워진 자리와 알파벳 표시
                num = ord(r) + 1 - ord('A')
                points[p] = num
                visitedNum[num] = 1
                visitedIdx[p] = 1
            p += 1
N = len(idxLst)
makeMagicStar(0)
