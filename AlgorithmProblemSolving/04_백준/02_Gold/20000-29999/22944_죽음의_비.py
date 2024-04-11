def go(ci, cj, stemina, umbrella, cnt):
    global ans

    es, ecnt = get_stemina_at_target(ci, cj, ei, ej, stemina, umbrella)
    if es > 0:
        ans = min(ans, cnt + ecnt)
        return

    for u in range(Nu):
        if v[u]: continue
        ui, uj = umbrellas[u]
        us, ucnt = get_stemina_at_target(ci, cj, ui, uj, stemina, umbrella)
        if us > 0:
            v[u] = 1
            go(ui, uj, us, D, cnt + ucnt)
            v[u] = 0

    return


def get_stemina_at_target(ci, cj, ti, tj, s, u):  # ci,cj에서 ti, tj에 간 후의 체력, 이동횟수 반환
    cnt = abs(ci - ti) + abs(cj - tj)
    if ci == si and cj == sj:
        s += 1
    a = u - cnt
    if a < 0:
        s += a
    return s, cnt


N, H, D = map(int, input().split())
umbrellas = []
for i in range(N):
    ipt = input()
    for j in range(N):
        if ipt[j] == 'S':
            si, sj = i, j
        elif ipt[j] == 'E':
            ei, ej = i, j
        elif ipt[j] == 'U':
            umbrellas.append((i, j))

Nu = len(umbrellas)
v = [0] * Nu
INF = 500*500+1
ans = INF
go(si, sj, H, 0, 0)
if ans == INF:
    print(-1)
else:
    print(ans)
