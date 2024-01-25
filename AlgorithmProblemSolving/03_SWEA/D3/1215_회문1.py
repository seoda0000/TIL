"""
SWEA D3 1215 회문
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi
"""
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    words = [input() for _ in range(8)]
    wordsT = list(zip(*words))
    ans = 0
    for i in range(8):
        for j in range(8 - N + 1):
            word = words[i][j:j + N]
            for n in range(N // 2):
                if word[n] != word[N - 1 - n]:
                    break
            else:
                ans += 1

            word = wordsT[i][j:j + N]
            for n in range(N // 2):
                if word[n] != word[N - 1 - n]:
                    break
            else:
                ans += 1

    print(f'#{test_case} {ans}')
