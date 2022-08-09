import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for case in range(1, T+1):
    N = int(input()) # 노선 개수
    ablst = [] # A, B 기록
    for _ in range(N):
        A, B = map(int, input().split())
        ablst.append((A, B))
    P = int(input()) # 정류장 개수
    clst = [] # 정류장 목록
    for _ in range(P):
        clst.append(int(input()))
    c = [0] * P # 정류장 별 노선 카운트 리스트
    for idx in range(P): # 정류장마다
        for ab in range(N): # 노선에 해당하는지 확인
            if ablst[ab][0] <= clst[idx] <= ablst[ab][1]: # 정류장이 A, B 사이에 있으면 카운트 증가
                c[idx] += 1
    print(f"#{case}", *c)

