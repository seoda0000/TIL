/*
월간 코드 챌린지 시즌1

3진법 뒤집기
https://school.programmers.co.kr/learn/courses/30/lessons/68935

자연수 n이 매개변수로 주어집니다.
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
 */

class Solution {
    public int solution(int n) {
        String third = Integer.toString(n,3);
        String opo_third = "";
        for (int i = third.length()-1; i >= 0; i--) {
            opo_third += third.charAt(i);
        }
        int answer = Integer.parseInt(opo_third, 3);
        return answer;
    }
}
