'''
4366. 정식이의 은행업무 D4
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd

삼성은행의 신입사원 정식이는 실수를 저질렀다.

은행 업무가 마감되기 직전인 지금, 송금할 금액을 까먹고 말았다.

하지만 다행스럽게도 정식이는 평소 금액을 2진수와 3진수의 두 가지 형태로 기억하고 다니며, 기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것만은 알고 있다.

예를 들어 현재 기억이 2진수 1010과 3진수 212을 말해주고 있다면 이는 14의 2진수인 1110와 14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.

정식이는 실수를 바로잡기 위해 당신에게 부탁을 하였다.

정식이가 송금액을 추측하는 프로그램을 만들어주자.

( 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.  추측할 수 없는 경우는 주어지지 않는다. )
'''


T = int(input())
for tc in range(1, T+1):
    n2 = list(map(int, list(input())))
    n3 = list(map(int, list(input())))
    s2 = []
    s3 = []



    for i in range(1, len(n2)):
        tmp = n2[:]
        tmp[i] = (tmp[i]+1)%2
        ss2 = 0
        for t in range(1, len(n2)+1):
            ss2 += (2**(t-1) * tmp[-t])
        s2.append(ss2)

    for i in range(len(n3)):
        tmp = n3[:]
        tmp[i] = (tmp[i]+1)%3
        if tmp[i] == 1 and tmp[i] == 0:
            pass
        else:
            ss3 = 0
            for t in range(1, len(n3)+1):
                ss3+=(3**(t-1) * tmp[-t])
            s3.append(ss3)
        tmp = n3[:]
        tmp[i] = (tmp[i] + 2) % 3
        if tmp[i] == 1 and tmp[i] == 0:
            pass
        else:
            ss3 = 0
            for t in range(1, len(n3)+1):
                ss3 += (3 ** (t - 1) * tmp[-t])
            s3.append(ss3)

    ans = set(s2)&set(s3)
    print(f'#{tc}', *ans)

