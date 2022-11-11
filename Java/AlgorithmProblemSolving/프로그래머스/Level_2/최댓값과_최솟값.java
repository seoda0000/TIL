/*
연습문제
최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=java

문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
 */


class Solution {
    public String solution(String s) {
        String[] lst = s.split("\\s");
        int min_s = Integer.parseInt(lst[0]);
        int max_s = Integer.parseInt(lst[0]);
        for (int i = 0; i < lst.length; i++) {
            max_s = Math.max(max_s, 	Integer.parseInt(lst[i]));
            min_s = Math.min(min_s, Integer.parseInt(lst[i]));
        }
        String answer = Integer.toString(min_s) + ' ' + Integer.toString(max_s);
        return answer;
    }
}