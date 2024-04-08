di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    inactive_lst = []  # 비활성 바이러스
    active_lst = []  # 활성 바이러스
    ij_set = set()  # 바이러스 위치 기록
    N, M, K = map(int, input().split())
    for i in range(N):
        ipt = list(map(int, input().split()))
        for j in range(M):
            if ipt[j]:  # 바이러스 발견
                inactive_lst.append((i, j, ipt[j], 0))  # 위치, 생명력, 태어난 시간
                ij_set.add((i, j))

    for k in range(1, K+1):
        li = len(inactive_lst)
        for i in range(li)[::-1]:
            vi, vj, vs, vt = inactive_lst[i]
            if vt + vs == k:  # 지금 활성화된 바이러스
                active_lst.append((vi, vj, vs, vt))
                inactive_lst.pop(i)

        new_virus_lst = []
        la = len(active_lst)
        for i in range(la)[::-1]:
            vi, vj, vs, vt = active_lst[i]

            if vt + vs + 1 == k:  # 번식할 바이러스
                for d in range(4):  # 4방향 번식
                    ni, nj = vi + di[d], vj + dj[d]
                    if (ni, nj) in ij_set: continue  # 이미 바이러스가 있다
                    new_virus_lst.append((ni, nj, vs, k))  # 바이러스가 태어난다

            if vt + vs + vs == k:  # 죽을 바이러스
                active_lst.pop(i)

        if new_virus_lst:
            ln = len(new_virus_lst)
            new_virus_lst.sort(key=lambda x: (x[0], x[1], -x[2]))
            for i in range(1, ln)[::-1]:
                vi, vj, _, _ = new_virus_lst[i]
                bi, bj, _, _ = new_virus_lst[i - 1]

                if vi == bi and vj == bj:
                    new_virus_lst.pop(i)
                else:
                    ij_set.add((vi, vj))
            ij_set.add((new_virus_lst[0][0], new_virus_lst[0][1]))

            inactive_lst.extend(new_virus_lst)  # 비활성에 추가

    print(f'#{test_case} {len(inactive_lst) + len(active_lst)}')
