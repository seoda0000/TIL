import sys

sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = list(map(int, input().split()))
    # 접수시간
    recep_info = [0] + list(map(int, input().split()))
    # 정비시간
    repair_info = [0] + list(map(int, input().split()))
    # 고객시간
    custom_time_lst = [0] + list(map(int, input().split()))
    customers = []

    for k in range(1, K + 1):
        customers.append((custom_time_lst[k], k))

    customers.sort(reverse=True)

    # 접수 대기리스트
    recep_wait_lst = []
    # 정비 대기리스트
    repair_wait_lst = []
    # 접수창구
    recep = [-1] + [0] * N
    # 정비창구
    repair = [(-1, -1)] + [(0, 0)] * M
    # 접수창구별 남은 시간
    recep_t = [0] * (N + 1)
    # 정비창구별 남은 시간
    repair_t = [0] * (M + 1)

    t = 0
    ans = 0
    cnt = 0

    while cnt < K:
        pass

        # 시간이 간다...
        for i in range(1, N + 1):
            if recep_t[i]:
                recep_t[i] -= 1

        for i in range(1, M + 1):
            if repair_t[i]:
                repair_t[i] -= 1

        # 정비 완료된 고객 처리
        for m in range(1, M + 1):
            if repair[m] != (0, 0) and repair[m] != (-1, -1) and not repair_t[m]:
                ck, recep_id = repair[m]
                if recep_id == A and m == B:
                    ans += ck
                repair[m] = (0, 0)
                cnt += 1

        # 접수 완료된 고객 처리
        for n in range(1, N + 1):
            if recep[n] and not recep_t[n]:
                repair_wait_lst.append((t, n, recep[n]))  # 기다리기 시작한 시간, 접수창구 번호, 고객 번호
                recep[n] = 0

        # 접수
        # 새로운 고객 입장
        while customers and customers[-1][0] == t:
            ct, ck = customers.pop()
            recep_wait_lst.append(ck)

        recep_wait_lst.sort(reverse=True)

        while recep_wait_lst and 0 in recep:  # 빈자리 있음 -> 접수
            ck = recep_wait_lst.pop()
            recep_id = recep.index(0)
            recep[recep_id] = ck
            recep_t[recep_id] = recep_info[recep_id]

        # 정비
        repair_wait_lst.sort(reverse=True)

        while repair_wait_lst and (0, 0) in repair:  # 빈자리 있음 -> 정비
            wt, recep_id, ck = repair_wait_lst.pop()
            repair_id = repair.index((0, 0))
            repair[repair_id] = (ck, recep_id)
            repair_t[repair_id] = repair_info[repair_id]

        t += 1

    if not ans:
        ans = -1
    print(f'#{tc} {ans}')
