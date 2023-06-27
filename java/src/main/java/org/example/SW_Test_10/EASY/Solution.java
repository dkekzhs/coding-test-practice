package org.example.SW_Test_10.EASY;

import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int answer = 0;
            for (int i = 0; i < 10; i++) {
                int Temp = sc.nextInt();
                if(Temp%2 == 0){
                    continue;
                }
                answer += Temp;
            }
            System.out.println("#"+test_case+" " + answer);
        }

    }
}
