package org.example.SW_Test_10.EASY;

import java.util.Arrays;
import java.util.Scanner;
public class MaxNum_2068 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int[] arrays = new int[10];
            for (int j = 0; j < arrays.length; j++) {
                arrays[j] = sc.nextInt();
            }
            int asInt = Arrays.stream(arrays).max().getAsInt();
            System.out.println("#"+test_case+" "+ asInt);
        }
    }
}
