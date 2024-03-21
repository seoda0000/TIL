def is_left(i, j):
    if i == 2:
        if j <= 3:
            return True
    else:
        if j <= 4:
            return True
    return False


keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
dic = dict()
for i in range(3):
    key = keys[i]
    for j in range(len(key)):
        dic[key[j]] = (i, j)

s_l, s_r = input().split()
st = input()

li, lj = dic[s_l]
ri, rj = dic[s_r]
ans = 0

for s in st:
    si, sj = dic[s]
    if is_left(si, sj):
        ans += abs(li - si) + abs(lj - sj) + 1
        li, lj = si, sj
    else:
        ans += abs(ri - si) + abs(rj - sj) + 1
        ri, rj = si, sj

print(ans)
