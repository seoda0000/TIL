'''
참외밭
https://www.acmicpc.net/problem/2477
백준 실버3 2477

시골에 있는 태양이의 삼촌 댁에는 커다란 참외밭이 있다. 문득 태양이는 이 밭에서 자라는 참외가 도대체 몇 개나 되는지 궁금해졌다.
어떻게 알아낼 수 있는지 골똘히 생각하다가 드디어 좋은 아이디어가 떠올랐다. 유레카!
1m2의 넓이에 자라는 참외 개수를 헤아린 다음, 참외밭의 넓이를 구하면 비례식을 이용하여 참외의 총개수를 구할 수 있다.
1m2의 넓이에 자라는 참외의 개수는 헤아렸고, 이제 참외밭의 넓이만 구하면 된다.
참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형이다.
다행히도 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향이었다. 밭의 한 모퉁이에서 출발하여 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하였다.
1m2의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어진다. 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오.

'''

n = int(input())
lst = []
for i in range(6):
    d, k = map(int, input().split())
    lst.append((d, k, i))

# 큰 사각형 변 구하기
mxh, mxhidx = max([(j[1], j[2]) for j in lst if j[0] in (1, 2)])
mxw, mxwidx = max([(j[1], j[2]) for j in lst if j[0] in (3, 4)])

if abs(mxhidx - mxwidx) == 1:
    mnidx1 = max(mxhidx, mxwidx) + 2  # 항상 두 칸 떨어져 있음.
    mnidx2 = max(mxhidx, mxwidx) + 3
    if mnidx1 > 5:                    # 인덱스 조정
        mnidx1 -= 6
    if mnidx2 > 5:
        mnidx2 -= 6
else:                                 # 큰 사각형 변의 인덱스가 (0, 5)인 경우
    mnidx1, mnidx2 = 2, 3
ans = mxw*mxh - lst[mnidx1][1]*lst[mnidx2][1]
print(ans*n)