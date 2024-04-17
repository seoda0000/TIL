N,M,P,C,D = map(int,input().split())
r_move = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
move = [(-1,0),(0,1),(1,0),(0,-1)]


graph = [[0 for _ in range(N)] for _ in range(N)]

ri,rj = map(int,input().split())
ri,rj = ri-1,rj-1
graph[ri][rj] = -1

santa_status = {}

for _ in range(1,P+1):
    santa,si,sj = map(int,input().split())
    si,sj = si-1,sj-1

    graph[si][sj] = santa

    santa_status[santa] = (si,sj,-2)

score = [0 for _ in range(P+1)]

total = P



for turn in range(M):

    if total ==0 :
        break

    #루돌프의 움직임
    dist = 1000000
    can_santa = []

    for santa in range(1,P+1):
        if santa_status[santa] == -1: continue
        si,sj,_ = santa_status[santa]

        temp_dist = (si-ri)**2 + (sj-rj)**2

        if temp_dist < dist:
            dist = temp_dist
            can_santa.clear()
            can_santa.append((si,sj,santa))

        elif temp_dist == dist:
            can_santa.append((si,sj,santa))
    if can_santa ==[]:
        break

    can_santa.sort(key=lambda x: -x[1])
    can_santa.sort(key = lambda x: -x[0])

    mi,mj,santa = can_santa[0]
    ni,nj = ri,rj

    for DIR in range(8):
        di = ri + r_move[DIR][0]
        dj = rj + r_move[DIR][1]

        if di < 0 or di >= N or dj < 0 or dj >= N:
            continue

        temp_dist = (di-mi)**2 + (dj-mj)**2
        if temp_dist < dist:
            r_DIR = DIR
            dist = temp_dist
            ni,nj = di,dj

    if graph[ni][nj] == 0:
        graph[ri][rj] = 0
        graph[ni][nj] = -1
        ri,rj = ni,nj

    else:
        score[graph[ni][nj]] += C

        sdi = ni + r_move[r_DIR][0]*C
        sdj = nj + r_move[r_DIR][1]*C

        if sdi < 0 or sdi >= N or sdj < 0 or sdj >= N:
            total-=1
            santa_status[graph[ni][nj]] = -1
            graph[ri][rj] = 0
            graph[ni][nj] = -1
            ri, rj = ni, nj

        elif graph[sdi][sdj] == 0:
            santa_status[graph[ni][nj]] = (sdi,sdj,turn)
            graph[sdi][sdj],graph[ni][nj],graph[ri][rj] = graph[ni][nj],graph[ri][rj],0
            ri, rj = ni, nj

        else:
            graph[ri][rj] = 0
            ri, rj = ni, nj

            santa_status[graph[ni][nj]] = (sdi, sdj, turn)

            now_santa = graph[ni][nj]
            graph[ni][nj] = -1

            while True:
                ndi = sdi + r_move[r_DIR][0]
                ndj = sdj + r_move[r_DIR][1]

                if ndi < 0 or ndi >= N or ndj < 0 or ndj >= N:
                    total -=1
                    santa_status[graph[sdi][sdj]] = -1
                    graph[sdi][sdj] = now_santa
                    santa_status[now_santa] = (sdi,sdj,santa_status[now_santa][2])
                    break

                elif graph[ndi][ndj] == 0:
                    graph[ndi][ndj] = graph[sdi][sdj]
                    graph[sdi][sdj] = now_santa

                    santa_status[now_santa] = (sdi,sdj,santa_status[now_santa][2])
                    santa_status[graph[ndi][ndj]] = (ndi,ndj,santa_status[graph[ndi][ndj]][2])

                    break
                else:
                    santa_status[now_santa] = (sdi, sdj, santa_status[now_santa][2])
                    now_santa,graph[sdi][sdj] = graph[sdi][sdj],now_santa

                    sdi,sdj = ndi,ndj

    print('-----------------')
    for line in graph:
        print(line)



    #산타의 움직임
    for santa in range(1,P+1):
        if santa_status[santa] == -1: continue
        si,sj,stun = santa_status[santa]

        if stun +2 > turn: continue

        dist = (ri-si)**2 + (rj-sj)**2
        ni,nj = si,sj
        S_DIR = -1
        for SDIR in range(4):
            di = si + move[SDIR][0]
            dj = sj + move[SDIR][1]

            if di < 0 or di >=N or dj < 0 or dj >= N or graph[di][dj] not in (-1,0): continue

            temp_dist = (di-ri)**2 + (dj-rj)**2

            if temp_dist < dist:
                ni,nj = di,dj
                dist = temp_dist
                S_DIR = SDIR

        if ni == si and nj == sj: continue

        if graph[ni][nj] == 0:
            graph[si][sj] = 0
            graph[ni][nj] = santa

            santa_status[santa] = (ni,nj,santa_status[santa][2])

        elif graph[ni][nj] == -1:
            score[santa] += D

            sdi = ni + move[(S_DIR+2)%4][0]*D
            sdj = nj + move[(S_DIR+2)%4][1]*D
            graph[si][sj] = 0

            if sdi < 0 or sdi >=N or sdj < 0 or sdj >= N:
                santa_status[santa] = -1


            elif graph[sdi][sdj] == 0:

                graph[sdi][sdj] = santa
                santa_status[santa] = (sdi,sdj,turn)

            else:

                now_santa = graph[sdi][sdj]
                graph[sdi][sdj] = santa
                santa_status[santa] = (sdi, sdj, turn)

                while True:
                    nsdi = sdi + move[(S_DIR+2)%4][0]
                    nsdj = sdj + move[(S_DIR+2)%4][1]

                    if nsdi < 0 or nsdi >=N or nsdj <0 or nsdj>=N:
                        total -=1
                        santa_status[now_santa] = -1
                        break

                    elif graph[nsdi][nsdj] == 0 :
                        graph[nsdi][nsdj] = now_santa
                        santa_status[now_santa] = (nsdi,nsdj,santa_status[now_santa][2])
                        break
                    else:
                        santa_status[now_santa] = (nsdi, nsdj, santa_status[now_santa][2])
                        now_santa,graph[nsdi][nsdj] = graph[nsdi][nsdj],now_santa
                        sdi,sdj = nsdi,nsdj
    print('-----------------')
    for line in graph:
        print(line)

    for santa in range(1, P + 1):
        if santa_status[santa] == -1: continue
        score[santa] +=1




print(*score[1:])