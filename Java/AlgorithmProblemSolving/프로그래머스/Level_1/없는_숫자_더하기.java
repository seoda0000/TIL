/*
없는 숫자 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/86051

0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
 */

class Solution {
  public int solution(int[] numbers) {
      int answer = 1+2+3+4+5+6+7+8+9;
      
      for (int i: numbers) {
          answer -= i;
      }
      return answer;
  }
}