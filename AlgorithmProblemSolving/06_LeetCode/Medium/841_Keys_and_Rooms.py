rooms = [[1],[2],[3],[]]
stk = [0]
visited = [0]*len(rooms)
visited[0] = 1

while stk:
    here = stk.pop()
    print(here)
    for nxt in rooms[here]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            stk.append(nxt)



print(0 not in visited)