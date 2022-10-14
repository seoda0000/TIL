'''
기타콘서트
https://www.acmicpc.net/problem/1497
백준 실버2 1497

강토는 Day Of Mourning의 기타리스트로, 다가오는 공연을 준비하고 있다.

어느 날 강토의 집에 도둑이 들어서 기타를 모두 도둑맞고 말았다. 기타를 사야 한다.

강토는 공연 때 연주할 노래의 목록을 뽑아 놓았다. 하지만, 하나의 기타로 모든 곡을 연주할 수는 없다. 어떤 기타는 어떤 곡을 연주할 때, 이상한 소리가 나기 때문이다. 항상 완벽을 추구하는 강토는 이런 일을 용납하지 않는다.

최대한 많은 곡을 제대로 연주하려고 할 때, 필요한 기타의 최소 개수를 구하는 프로그램을 작성하시오.

예를 들어, GIBSON으로 1, 2, 3번 곡을 제대로 연주할 수 있고, FENDER로 1, 2, 5번 곡을 제대로 연주할 수 있고, EPIPHONE으로 4, 5번 곡을 제대로 연주할 수 있고, ESP로 1번곡을 제대로 연주할 수 있다면, 세준이는 EPIPHONE과 GIBSON을 사면 최소의 개수로 모든 곡을 연주할 수 있다. 
'''


# 비트연산자로 풀었습니다.

def f(nth, s, cnt): # nth번째 기타 고려, 연주할 수 있는 곡, 기타의 수
    global mn, mxs
    if nth >= N:    # 마지막 요소까지 고려했다면 종료
        s = bin(s).count('1')
        if mxs < s:     # 만약 곡 수가 최대라면
            mn = cnt        # 바로 mn, mxs 갱신
            mxs = s
        if mxs == s:    # 만약 곡 수가 현재 최대값과 같다면
            if cnt < mn:    # 기타 수가 적을 경우 mn 갱신
                mn = cnt
        return
    f(nth+1, s|glst[nth], cnt+1)   # n번째 기타를 포함하는 경우
    f(nth+1, s, cnt)               # n번째 기타를 포함하지 않는 경우



N, M = map(int, input().split())
glst = []
for _ in range(N):
    _, song = input().split()
    song = song.replace('Y', '1').replace('N', '0')  # Y, N을 1, 0으로 변경
    glst.append(int('0b'+song, 2))                   # 10진수로 변환하여 저장
mxs, mn = 0, N # 초기값 설정 : 연주할 수 있는 최대 곡, 그 경우의 기타 수
f(0, 0, 0)
if mxs == 0:   # 연주할 수 있는 곡이 없다면 -1
    mn = -1
print(mn)