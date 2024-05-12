def make_combination(num):
    lst = []
    for i in range(N):
        if num & 1 << i:
            lst.append(i)
    check_menu_lst(lst)


def check_menu_lst(lst):
    global ans, best

    nutrients = [0] * 5
    for l in lst:
        menu = menus[l]
        for i in range(5):
            nutrients[i] += menu[i]

    is_sufficient = True

    for i in range(4):
        if target[i] > nutrients[i]:
            is_sufficient = False
            break

    if is_sufficient:
        if ans > nutrients[4]:
            ans = nutrients[4]
            best = [lst]
        elif ans == nutrients[4]:
            best.append(lst)

    return


N = int(input())
target = list(map(int, input().split()))
menus = [list(map(int, input().split())) for _ in range(N)]
ans = 500 * N
best = []

for i in range(1, 2 ** N):
    make_combination(i)

if ans == 500 * N:
    print(-1)
else:
    print(ans)
    best.sort()
    print(*[b + 1 for b in best[0]])
