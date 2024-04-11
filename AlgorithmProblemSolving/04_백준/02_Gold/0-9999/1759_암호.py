def fill_pw(nth):
    if nth == L + 1:
        pw = "".join([words[i] for i in idx])
        mcnt = sum([pw.count(m) for m in mowords])
        jcnt = L - mcnt
        if mcnt and jcnt >= 2:
            ans.append(pw)
        return
    for i in range(idx[nth - 1] + 1, C + 1):
        if v[i]: continue
        idx[nth] = i
        v[i] = 1
        fill_pw(nth + 1)
        v[i] = 0


mowords = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
words = [""] + list(input().split())
words.sort()
idx = [0] * (L + 1)
v = [0] * (C + 1)
ans = []
fill_pw(1)
print(*ans, sep="\n")
