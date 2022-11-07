/*
위클리 챌린지
부족한 금액 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=java

새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다.
이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.
*/

class Solution {
    public long solution(int price, int money, int count) {
        long cnt = 0;
        for (long i = 0; i <= count; i++) {
            cnt += i;
        }
        cnt *= price;
        long answer = cnt - money;
        if (answer <= 0) {
            answer = 0;
        }
        return answer;
    }
}