'''
무기 공학
https://www.acmicpc.net/problem/18430
백준 골드5 18430

공학자 길동이는 외부의 침략으로부터 마을을 지킬 수 있는 부메랑 무기를 개발하는 공학자다. 길동이는 부메랑 제작을 위한 고급 나무 재료를 구했다.
이 나무 재료는 NxM크기의 직사각형 형태이며 나무 재료의 부위마다 그 강도가 조금씩 다르다.

예를 들어 나무 재료의 크기가 2x3일 때는 다음과 같이 총 6칸으로 구성된다.

길동이는 이처럼 넓은 사각형 형태의 나무 재료를 잘라서 여러 개의 부메랑을 만들고자 한다.
그리고 부메랑은 항상 3칸을 차지하는 ‘ㄱ’모양으로 만들어야 한다. 따라서 부메랑의 가능한 모양은 다음과 같이 총 4가지다.

이때 부메랑의 중심이 되는 칸은 강도의 영향을 2배로 받는다. 위 그림에서 노란색으로 칠한 부분이 ‘중심이 되는 칸’이다.

나무 재료의 형태와 각 칸의 강도가 주어졌을 때, 길동이가 만들 수 있는 부메랑들의 강도 합의 최댓값을 출력하는 프로그램을 작성하시오.
'''

def dfs(ii, jj, dps):
    global ans
    dlst = ((0, -1, 1, 0), (0, -1, -1, 0), (0, 1, -1, 0), (0, 1, 1, 0))  # 블럭 조합
    if ii >= N or jj >= M:                                               # 종료 조건
        if dps > ans:
            ans = dps
        return

    if not visited[ii][jj]:  # 아직 사용하지 않은 블럭이라면 확인
        for D in dlst:
            a, b, c, d = D
            if 0<=ii+a<N and 0<=jj+b<M and 0<=ii+c<N and 0<=jj+d<M:  # 범위 내라면
                if not visited[ii+a][jj+b] and not visited[ii+c][jj+d]:
                    visited[ii][jj] = visited[ii + a][jj + b] = visited[ii + c][jj + d] = True   # 사용 표시
                    plus = 2*arr[ii][jj] + arr[ii + a][jj + b] + arr[ii + c][jj + d]  # 무기 강도
                    if jj == M-1:                                    # 행의 끝이라면 줄 바꿈
                        dfs(ii+1, 0, dps+plus)
                    else:
                        dfs(ii, jj+1, dps+plus)
                    visited[ii][jj] = visited[ii + a][jj + b] = visited[ii + c][jj + d] = False  # clear
    if jj == M - 1:          # 사용한 블럭이라면 다음 블럭으로
        dfs(ii + 1, 0, dps)
    else:
        dfs(ii, jj + 1, dps)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[False]*M for _ in range(N)]
dfs(0, 0, 0)
print(ans)



