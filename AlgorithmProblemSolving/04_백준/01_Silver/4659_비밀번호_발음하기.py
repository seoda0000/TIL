'''
비밀번호 발음하기
https://www.acmicpc.net/problem/4659
백준 실버5 4659

좋은 패스워드를 만드는것은 어려운 일이다. 대부분의 사용자들은 buddy처럼 발음하기 좋고 기억하기 쉬운 패스워드를 원하나, 이런 패스워드들은 보안의 문제가 발생한다. 어떤 사이트들은 xvtpzyo 같은 비밀번호를 무작위로 부여해 주기도 하지만, 사용자들은 이를 외우는데 어려움을 느끼고 심지어는 포스트잇에 적어 컴퓨터에 붙여놓는다. 가장 이상적인 해결법은 '발음이 가능한' 패스워드를 만드는 것으로 적당히 외우기 쉬우면서도 안전하게 계정을 지킬 수 있다.

회사 FnordCom은 그런 패스워드 생성기를 만들려고 계획중이다. 당신은 그 회사 품질 관리 부서의 직원으로 생성기를 테스트해보고 생성되는 패스워드의 품질을 평가하여야 한다. 높은 품질을 가진 비밀번호의 조건은 다음과 같다.

1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

이 규칙은 완벽하지 않다;우리에게 친숙하거나 발음이 쉬운 단어 중에서도 품질이 낮게 평가되는 경우가 많이 있다.

'''


import sys
def input():
	return sys.stdin.readline().rstrip()

za = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
mo = ['a', 'e', 'i', 'o', 'u']
dd = ['aa', 'bb', 'cc', 'dd', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
while True:
    word = input()
    if word == 'end': # 종료 조건
        break
    accpt = True      # 허용 여부
    for m in mo:      # 1. 모음이 하나 이상 있어야 한다.
        if m in word:
            break
    else:
        accpt = False

    if accpt:          # 2. ee, oo 제외 중복된 문자가 없어야 한다.
        for d in dd:
            if d in word:
                accpt = False
                break
    if accpt:          # 3. 자음, 모음이 3개 연속 이어지면 안된다.
        flag = 0
        for w in word:
            if w in mo:
                flag = max(flag, 0)
                flag += 1
            if w in za:
                flag = min(flag, 0)
                flag -= 1
            if abs(flag) >= 3:
                accpt = False
                break

    if accpt:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')