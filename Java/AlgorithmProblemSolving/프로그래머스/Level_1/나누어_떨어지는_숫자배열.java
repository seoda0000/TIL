/*
나누어 떨어지는 숫자배열
https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=java
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
 */


import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] ans = new int[arr.length];
        int p = 1;
        for (int i = 0; i<arr.length; i++) {
            if (arr[i] % divisor == 0) {
                ans[p-1] = arr[i];
                p += 1;
                }
        }
        int[] answer = new int[p];
        if (p == 1) {
            answer = Arrays.copyOfRange(ans, 0, 1);
            answer[0] = -1;
        } else {
            answer = Arrays.copyOfRange(ans, 0, p-1);
            Arrays.sort(answer);
            }
        return answer;
        }
        
    }
