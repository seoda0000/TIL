def find_group_two():
    return

def pick_two(pick):
    if pick == 0:
        two_rock = []
        for t in temp:
            two_rock.append(all_border_lst[t])
        two_rock_lst.append(two_rock)
        return
    for n in range(temp[-1], bN):
        if n in temp: continue
        temp.append(n)
        pick_two(pick - 1)
        temp.pop()

    return


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]
all_border_set = set()
border_dic = dict()
large_with_idx = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 2: continue
        if v[i][j]: continue
        find_group_two(i, j)

if len(all_border_set) == 2 * len(large_with_idx):
    ans = max(large_with_idx)
else:
    all_border_lst = list(all_border_set)
    bN = len(all_border_lst)
    two_rock_lst = []
    temp = [-1]
    pick_two(2)
    ans = 0

    for two_rock in two_rock_lst:

        for key, values in border_dic:
            for vi, vj in values:
                if (vi, vj) not in two_rock:
                    break

            else:
                ans += large_with_idx[key]
