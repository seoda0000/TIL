/*
월간 코드 챌린지 시즌2
약수의 개수와 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/77884?language=java

두 정수 left와 right가 매개변수로 주어집니다.
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
 */

class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i <= right; i++) {
            int tmp = 0;
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    tmp += 1;
                } 
            }
            if (tmp % 2 == 0) {
                answer += i;
            } else {
                answer -= i;
            }
        }
        return answer;
    }
}