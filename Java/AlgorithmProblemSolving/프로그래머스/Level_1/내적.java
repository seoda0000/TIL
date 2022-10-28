/*
월간코드챌린지 시즌1
내적
https://school.programmers.co.kr/learn/courses/30/lessons/70128

길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
 */


class Solution {
  public int solution(int[] a, int[] b) {
      int answer = 0;
      int n = a.length;
      for (int i = 0; i < n; i++) {
          answer += a[i]*b[i];
      }
      return answer;
  }
}