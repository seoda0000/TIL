# 6098 : [기초-리스트] 성실한 개미
"""
미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
"""
# 미로상자 입력 받기

ans = []
for _ in range(10):
    ans.append(list(map(int, input().split())))

a = 1
c = True
for i in range(1, 10):
    b = True
    while a < 9 and b == True:

        # 0 이면 9로 바꾸고 오른쪽으로 한칸 이동
        if ans[i][a] == 0:
            ans[i][a] = 9
            a += 1

        # 1 이면 다시 왼쪽으로 이동. 그리고 아래쪽으로 한칸 이동.
        elif ans[i][a] == 1:
            a -= 1
            b = False

        # 2 면 종료
        elif ans[i][a] == 2:
            ans[i][a] = 9
            c = False
            break
    
    # 이중 break 처리
    if c == False:
        break

# 개미경로 출력
for i in ans:
    for j in i:
        print(j, end = " ")
    print()