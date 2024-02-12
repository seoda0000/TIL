def chooseSkill(nth):
    global ans
    if nth == N:
        cnt = 0

        for quest in quests:
            for q in quest:
                if q not in keyboard:
                    break
            else:
                cnt += 1
        ans = max(ans, cnt)
        return

    for i in range(keyboard[nth]+1, 2*N+1):
        keyboard[nth+1] = i
        chooseSkill(nth+1)

    return
N, M, K = map(int, input().split())
quests = [list(map(int, input().split())) for _ in range(M)]
ans = 0
keyboard = [0]*(N+1)
chooseSkill(0)
print(ans)

