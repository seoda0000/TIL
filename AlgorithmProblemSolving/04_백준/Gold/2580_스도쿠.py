def fill_nth_zero(nth):
    if nth == N:
        for a in arr:
            print(*a)
        return True

    ti, tj = zero_lst[nth]

    # 빈칸에 기입 가능한 숫자
    able_nums = num_set - row_sets[ti] - col_sets[tj] - table_sets[(ti // 3) * 3 + tj // 3]

    for num in able_nums:

        # 기입
        arr[ti][tj] = num
        row_sets[ti].add(num)
        col_sets[tj].add(num)
        table_sets[(ti // 3) * 3 + tj // 3].add(num)

        if fill_nth_zero(nth + 1): return True

        # 초기화
        row_sets[ti].remove(num)
        col_sets[tj].remove(num)
        table_sets[(ti // 3) * 3 + tj // 3].remove(num)

    return False


arr = [list(map(int, input().split())) for _ in range(9)]
num_set = set(range(1, 10))
row_sets = [set() for _ in range(9)]
col_sets = [set() for _ in range(9)]
table_sets = [set() for _ in range(9)]
zero_lst = []

for i in range(9):
    row_sets[i] = set(arr[i])
    for j in range(9):
        n = arr[i][j]
        if n == 0:  # 빈칸 체크
            zero_lst.append((i, j))
        else:  # 숫자면 가로, 세로, 칸 set에 기입
            col_sets[j].add(n)
            table_sets[(i // 3) * 3 + j // 3].add(n)

N = len(zero_lst)
fill_nth_zero(0)
