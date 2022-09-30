'''
1953. [모의 SW 역량테스트] 탈주범 검거
https://swexpertacademy.com/main/code/problem/problemDetail.do

교도소로 이송 중이던 흉악범이 탈출하는 사건이 발생하여 수색에 나섰다.

탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,

지하 터널 어딘가에서 은신 중인 것으로 추정된다.

터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산하여야 한다.

탈주범은 시간당 1의 거리를 움직일 수 있다.

지하 터널은 총 7 종류의 터널 구조물로 구성되어 있으며 각 구조물 별 설명은 [표 1]과 같다.

탈주범이 탈출 한 시간 뒤 도달할 수 있는 지점은 한 곳이다.

지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산하는 프로그램을 작성하라.

'''


def bfs():
    q = [(R, C)]
    v[R][C] = 1
    t = 0

    while True:
        if t == L-1:
            break
        t += 1
        for _ in range(len(q)):
            ci, cj = q.pop(0)
            for a, b in dr[arr[ci][cj]]:
                ni, nj = ci + a, cj + b
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]>0 and v[ni][nj] == 0:
                    if (-a, -b) in dr[arr[ni][nj]]:
                        v[ni][nj] = 1
                        q.append((ni, nj))


dr = {1:[(0, 1), (1, 0), (-1, 0), (0, -1)], 2:[(1, 0), (-1, 0)],
      3:[(0, 1), (0, -1)], 4:[(-1, 0), (0, 1)], 5:[(1, 0), (0, 1)],
      6:[(0, -1), (1, 0)], 7:[(-1, 0), (0, -1)]}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    bfs()
    ans = 0
    for vv in v:
        ans += sum(vv)
    print(f'#{tc}', ans)



