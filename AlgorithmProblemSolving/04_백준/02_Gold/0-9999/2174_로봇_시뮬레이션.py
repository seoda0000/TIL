def simulate():
    for order in orders:
        r, o, k = order

        for _ in range(k):
            i, j, d = robo_dic[r]

            if o == 'L':
                robo_dic[r] = (i, j, (d + 1) % 4)  # 회전 방향도 반대다...
            elif o == 'R':
                robo_dic[r] = (i, j, (d - 1) % 4)
            else:
                ni, nj = i + di[d], j + dj[d]

                if not (0 <= ni < N and 0 <= nj < M):
                    print(f'Robot {r} crashes into the wall')
                    return False

                if arr[ni][nj]:
                    print(f'Robot {r} crashes into robot {arr[ni][nj]}')
                    return False

                arr[i][j] = 0
                arr[ni][nj] = r
                robo_dic[r] = (ni, nj, d)

    return True


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
dir_dic = {'N': 1, 'S': 3, 'E': 0, 'W': 2}  # 방향 위아래 반전
M, N = map(int, input().split())
robot_cnt, order_cnt = map(int, input().split())
robo_dic = dict()
arr = [[0] * M for _ in range(N)]
orders = []

for r in range(1, robot_cnt + 1):  # 로봇 목록
    j, i, d = input().split()
    i, j, d = int(i) - 1, int(j) - 1, dir_dic[d]
    robo_dic[r] = (i, j, d)
    arr[i][j] = r

for _ in range(order_cnt):  # 명령 목록
    r, o, K = input().split()
    orders.append((int(r), o, int(K)))

if simulate():
    print('OK')
